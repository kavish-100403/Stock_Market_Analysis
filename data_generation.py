import yfinance as yf
import pandas as pd

# Fetch stock data from Yahoo Finance
def fetch_stock_data(ticker, start_date, end_date):
    stock_data = yf.download(ticker, start=start_date, end=end_date)
    
    # Calculating additional features
    stock_data['SMA'] = stock_data['Close'].rolling(window=20).mean()  # Simple Moving Average (SMA)
    stock_data['EMA'] = stock_data['Close'].ewm(span=20, adjust=False).mean()  # Exponential Moving Average (EMA)
    
    # Relative Strength Index (RSI)
    delta = stock_data['Close'].diff(1)
    gain = delta.where(delta > 0, 0)
    loss = -delta.where(delta < 0, 0)
    avg_gain = gain.rolling(window=14).mean()
    avg_loss = loss.rolling(window=14).mean()
    rs = avg_gain / avg_loss
    stock_data['RSI'] = 100 - (100 / (1 + rs))
    
    # Bollinger Bands
    stock_data['20_SMA'] = stock_data['Close'].rolling(window=20).mean()
    stock_data['BB_upper'] = stock_data['20_SMA'] + (stock_data['Close'].rolling(window=20).std() * 2)
    stock_data['BB_lower'] = stock_data['20_SMA'] - (stock_data['Close'].rolling(window=20).std() * 2)
    
    # Moving Average Convergence Divergence (MACD)
    stock_data['MACD'] = stock_data['Close'].ewm(span=12, adjust=False).mean() - stock_data['Close'].ewm(span=26, adjust=False).mean()
    stock_data['MACD_Signal'] = stock_data['MACD'].ewm(span=9, adjust=False).mean()
    
    # On-Balance Volume (OBV)
    stock_data['Daily Returns'] = stock_data['Close'].pct_change()  # Daily Returns (percentage change)
    stock_data['OBV'] = (stock_data['Volume'].where(stock_data['Close'] > stock_data['Close'].shift(1), -stock_data['Volume'])).cumsum()
    
    # Lag Features
    stock_data['Lag_1_Close'] = stock_data['Close'].shift(1)  # 1-day lag of Close price
    stock_data['Lag_1_Volume'] = stock_data['Volume'].shift(1)  # 1-day lag of Volume
    
    # Drop NaN values (arising due to rolling calculations)
    stock_data.dropna(inplace=True)
    
    return stock_data

# Function to save stock data to CSV
def save_to_csv(stock_data, filename):
    stock_data.to_csv(filename)
    print(f"Data exported successfully to {filename}")

# Example usage
ticker = "AAPL"
start_date = "2013-01-01"
end_date = "2023-01-01"
stock_data = fetch_stock_data(ticker, start_date, end_date)

# Export to CSV
csv_filename = f"{ticker}_stock_data.csv"
save_to_csv(stock_data, csv_filename)

import numpy as np
import pandas as pd
import yfinance as yf
import matplotlib.pyplot as plt
from keras.models import load_model
import streamlit as st


model=load_model("D:\Github\Stock_Market_Analysis\Stock_Prediction_Model.keras")

st.header("Stock Market Predictor")

stock = st.text_input("Enter Stock Symbol", "GOOG")
start='1990-01-01'
end='2021-12-31'

data=yf.download(stock,start,end)

st.subheader("Stock Data")
st.write(data)

data_train = pd.DataFrame(data.Close[0:int(len(data)*0.8)])
data_test = pd.DataFrame(data.Close[int(len(data)*0.8):len(data)])

#Scaling the data between 0 and 1
from sklearn.preprocessing import MinMaxScaler
scaler=MinMaxScaler(feature_range=(0,1))

#Fitting the data
pas_100_days=data_train.tail(100)
data_test=pd.concat([pas_100_days,data_test], ignore_index=True)
data_test_scale=scaler.fit_transform(data_test)

#Graph for MA50
st.subheader("Price vs MA50")
ma_50_days=data.Close.rolling(50).mean()
fig1=plt.figure(figsize=(8,6))
plt.plot(ma_50_days, "r", label="MA 50 days")
plt.plot(data.Close, "b", label="Closing Price")
plt.xlabel("Time")
plt.ylabel("Price")
plt.legend()
plt.show()
st.pyplot(fig1)

#Graph for MA100
st.subheader("Price vs MA50 vs MA100")
ma_100_days=data.Close.rolling(100).mean()
fig2=plt.figure(figsize=(8,6))
plt.plot(ma_50_days, "r", label="MA 50 days")
plt.plot(ma_100_days, "g", label="MA 100 days")
plt.plot(data.Close, "b", label="Closing Price")
plt.xlabel("Time")
plt.ylabel("Price")
plt.legend()
plt.show()
st.pyplot(fig2)

#Graph for MA50
st.subheader("Price vs MA100 vs MA200")
ma_200_days=data.Close.rolling(200).mean()
fig3=plt.figure(figsize=(8,6))
plt.plot(ma_100_days, "r", label="MA 100 days")
plt.plot(ma_200_days, "g", label="MA 200 days")
plt.plot(data.Close, "b", label="Closing Price")
plt.xlabel("Time")
plt.ylabel("Price")
plt.legend()
plt.show()
st.pyplot(fig3)




#Array Slicing
x=[]
y=[]
for i in range(100,data_test_scale.shape[0]):
    x.append(data_test_scale[i-100:i])
    y.append(data_test_scale[i,0])
x,y=np.array(x), np.array(y)


predict=model.predict(x)
scale=1/scaler.scale_
predict*=scale
y=y*scale

#Orignal VS Predicted Price
st.subheader("Original Price vs Predicted Price")
fig4=plt.figure(figsize=(8,6))
plt.plot(y, "b", label="Original Price")
plt.plot(predict, "g", label="Predicted Price")
plt.xlabel("Time")
plt.ylabel("Price")
plt.legend()
plt.show()
st.pyplot(fig4)

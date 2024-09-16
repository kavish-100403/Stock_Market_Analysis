# Random Forest Regression
def open_random_forest_regression():
        
    # Importing the libraries
    import numpy as np
    import matplotlib.pyplot as plt
    import pandas as pd

    # Importing the dataset
    dataset = pd.read_csv('AAPL_stock_data.csv')
    X = dataset.iloc[:, [i for i in range(dataset.shape[1]) if i not in [0, 1]]].values
    y = dataset.iloc[:, 1].values

    # Splitting the dataset into the Training set and Test set
    from sklearn.model_selection import train_test_split
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 0)

    # Training the Random Forest Regression model on the whole dataset
    from sklearn.ensemble import RandomForestRegressor
    regressor = RandomForestRegressor(n_estimators = 10, random_state = 0)
    regressor.fit(X_train, y_train)

    # Predicting the Test set results
    y_pred = regressor.predict(X_test)
    np.set_printoptions(precision=13)
    # print(np.concatenate((y_pred.reshape(len(y_pred),1), y_test.reshape(len(y_test),1)),1))

    # Evaluating the Model Performance
    from sklearn.metrics import r2_score
    rms=r2_score(y_test, y_pred)*100
    return rms, "Random Forest Regression"


def close_random_forest_regression():
        
    # Importing the libraries
    import numpy as np
    import matplotlib.pyplot as plt
    import pandas as pd

    # Importing the dataset
    dataset = pd.read_csv('AAPL_stock_data.csv')
    X = dataset.iloc[:, [i for i in range(dataset.shape[1]) if i not in [0, 4]]].values
    y = dataset.iloc[:, 4].values

    # Splitting the dataset into the Training set and Test set
    from sklearn.model_selection import train_test_split
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 0)

    # Training the Random Forest Regression model on the whole dataset
    from sklearn.ensemble import RandomForestRegressor
    regressor = RandomForestRegressor(n_estimators = 10, random_state = 0)
    regressor.fit(X_train, y_train)

    # Predicting the Test set results
    y_pred = regressor.predict(X_test)
    np.set_printoptions(precision=13)
    # print(np.concatenate((y_pred.reshape(len(y_pred),1), y_test.reshape(len(y_test),1)),1))

    # Evaluating the Model Performance
    from sklearn.metrics import r2_score
    rms=r2_score(y_test, y_pred)*100
    return rms, "Random Forest Regression"
# Decision Tree Regression
def opens_decision_tree_regression(filename):

    # from data_generation import csv_filename
    # Importing the libraries
    import numpy as np
    import matplotlib.pyplot as plt
    import pandas as pd

    # Importing the dataset
    
    dataset = pd.read_csv(filename)
    # dataset = pd.read_csv("AAPL_stock_data.csv")
    X = dataset.iloc[:, [i for i in range(dataset.shape[1]) if i not in [0, 1,4,5]]].values
    y = dataset.iloc[:, 1].values

    # Splitting the dataset into the Training set and Test set
    from sklearn.model_selection import train_test_split
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 0)

    # Training the Decision Tree Regression model on the Training set
    from sklearn.tree import DecisionTreeRegressor
    regressor = DecisionTreeRegressor(random_state = 0)
    regressor.fit(X_train, y_train)

    # Predicting the Test set results
    y_pred = regressor.predict(X_test)
    np.set_printoptions(precision=13)
    # print(np.concatenate((y_pred.reshape(len(y_pred),1), y_test.reshape(len(y_test),1)),1))

    # Evaluating the Model Performance
    from sklearn.metrics import mean_absolute_error
    MAE=mean_absolute_error(y_test, y_pred)*100
    return MAE, "Decision Tree Regression"


def close_decision_tree_regression(filename):

    # from data_generation import csv_filename
    # Importing the libraries
    import numpy as np
    import matplotlib.pyplot as plt
    import pandas as pd

    # Importing the dataset
    dataset = pd.read_csv(filename)
    # dataset = pd.read_csv("AAPL_stock_data.csv")
    X = dataset.iloc[:, [i for i in range(dataset.shape[1]) if i not in [0, 1,4,5]]].values
    y = dataset.iloc[:, 4].values

    # Splitting the dataset into the Training set and Test set
    from sklearn.model_selection import train_test_split
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 0)

    # Training the Decision Tree Regression model on the Training set
    from sklearn.tree import DecisionTreeRegressor
    regressor = DecisionTreeRegressor(random_state = 0)
    regressor.fit(X_train, y_train)

    # Predicting the Test set results
    y_pred = regressor.predict(X_test)
    np.set_printoptions(precision=13)
    # print(np.concatenate((y_pred.reshape(len(y_pred),1), y_test.reshape(len(y_test),1)),1))

    # Evaluating the Model Performance
    from sklearn.metrics import mean_absolute_error
    MAE=mean_absolute_error(y_test, y_pred)*100
    return MAE, "Decision Tree Regression"
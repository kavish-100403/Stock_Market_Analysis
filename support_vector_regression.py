# Support Vector Regression (SVR)
def open_support_vector_regression():
    # Importing the libraries
    import numpy as np
    import matplotlib.pyplot as plt
    import pandas as pd

    # Importing the dataset
    dataset = pd.read_csv('AAPL_stock_data.csv')
    X = dataset.iloc[:, [i for i in range(dataset.shape[1]) if i not in [0, 1]]].values
    y = dataset.iloc[:, 1].values
    y = y.reshape(len(y),1)

    # Splitting the dataset into the Training set and Test set
    from sklearn.model_selection import train_test_split
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 0)

    # Feature Scaling
    from sklearn.preprocessing import StandardScaler
    sc_X = StandardScaler()
    sc_y = StandardScaler()
    X_train = sc_X.fit_transform(X_train)
    y_train = sc_y.fit_transform(y_train)

    # Training the SVR model on the Training set
    from sklearn.svm import SVR
    regressor = SVR(kernel = 'rbf')
    regressor.fit(X_train, y_train)

    # Predicting the Test set results
    y_pred = sc_y.inverse_transform(regressor.predict(sc_X.transform(X_test)).reshape(-1,1))
    np.set_printoptions(precision=13)
    print(np.concatenate((y_pred.reshape(len(y_pred),1), y_test.reshape(len(y_test),1)),1))

    # Evaluating the Model Performance
    from sklearn.metrics import r2_score
    print(r2_score(y_test, y_pred)*100)


def close_support_vector_regression():
    # Importing the libraries
    import numpy as np
    import matplotlib.pyplot as plt
    import pandas as pd

    # Importing the dataset
    dataset = pd.read_csv('AAPL_stock_data.csv')
    X = dataset.iloc[:, [i for i in range(dataset.shape[1]) if i not in [0, 4]]].values
    y = dataset.iloc[:, 4].values
    y = y.reshape(len(y),1)

    # Splitting the dataset into the Training set and Test set
    from sklearn.model_selection import train_test_split
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 0)

    # Feature Scaling
    from sklearn.preprocessing import StandardScaler
    sc_X = StandardScaler()
    sc_y = StandardScaler()
    X_train = sc_X.fit_transform(X_train)
    y_train = sc_y.fit_transform(y_train)

    # Training the SVR model on the Training set
    from sklearn.svm import SVR
    regressor = SVR(kernel = 'rbf')
    regressor.fit(X_train, y_train)

    # Predicting the Test set results
    y_pred = sc_y.inverse_transform(regressor.predict(sc_X.transform(X_test)).reshape(-1,1))
    np.set_printoptions(precision=13)
    print(np.concatenate((y_pred.reshape(len(y_pred),1), y_test.reshape(len(y_test),1)),1))

    # Evaluating the Model Performance
    from sklearn.metrics import r2_score
    print(r2_score(y_test, y_pred)*100)
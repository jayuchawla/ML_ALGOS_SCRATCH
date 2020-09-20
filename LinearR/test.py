import numpy as np
from sklearn import datasets
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt

def mean_squared_error(y_actual, y_predicted):
    return np.mean((y_actual-y_predicted)**2)

def plot_scatter_and_line(X, y_pred_line, X_train, X_test, y_train, y_test):
    plt.figure(figsize = (8,6))
    plt.scatter(X_train, y_train, color = "b", s = 10)
    plt.scatter(X_test, y_test, color = "g", s = 10)
    plt.plot(X, y_pred_line, color = "black", linewidth = 1, label = "Prediction")
    plt.show()

def train_test_with_sklearn_dataset():
    X, y = datasets.make_regression(n_samples=100, n_features=1, noise = 20, random_state = 4)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 1234)
    print(y)
    return X_train, X_test, y_train, y_test

def test_with_sklearn_dataset():
    X_train, X_test, y_train, y_test = train_test_with_sklearn_dataset()

    #create object
    regressor = LinearRegression(0.01)

    #fit train set
    regressor.fit(X_train, y_train)

    #predict values for test set
    predicted_values = regressor.predict(X_test)

    #print mean square error
    print(mean_squared_error(y_test, predicted_values))

    #plot 
    X = np.concatenate((X_train, X_test))
    #y_pred_line = regressor.predict(X)
    plot_scatter_and_line(X, regressor.predict(X), X_train, X_test, y_train, y_test)

def test_with_given_dataset():
    X = [[10],[9],[2],[15],[10],[16],[11],[16]]
    y = [95,80,10,50,45,98,38,93]
    #create object
    regressor = LinearRegression(0.002)

    #fit train set
    regressor.fit(np.array(X), np.array(y))
    lin = regressor.predict(np.array(X))
    print(lin)
    print(regressor.weights)
    print(regressor.bias)

    plt.figure(figsize = (8,6))
    plt.scatter(X,y, color = "b", s = 10)
    plt.plot(X, lin, color = "black", linewidth = 1, label = "Prediction")
    plt.show()

from LR import LinearRegression
#test_with_given_dataset()
test_with_sklearn_dataset()

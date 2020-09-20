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

def test_with_sklearn_dataset():
    X, y = datasets.make_regression(n_samples=100, n_features=1, noise = 20, random_state = 4)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 1234)
    return X_train, X_test, y_train, y_test


X_train, X_test, y_train, y_test = test_with_sklearn_dataset()
from LR import LinearRegression

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
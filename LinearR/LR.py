import numpy as np

class LinearRegression():
    
    def __init__(self, learningFactor = 0.001, n_iterations = 1000):
        """Learning factor: the rate of varying values of w and b, weights: associated with dimensions, bias: y shift"""
        self.learningFactor = learningFactor
        self.n_iterations = n_iterations
        self.weights = None
        self.bias = None

    def fit(self, X, y):
        n_samples, n_features = X.shape

        #initialise all dimension specific weights(m1, m2, .. in y = m1x1 + m2x2 ...+ b) as 0
        #you can also use random weights
        self.weights = np.zeros(n_features)
        self.bias = 0

        for _ in range(self.n_iterations):
            y_predicted_for_all_samples = np.dot(X, self.weights) + self.bias

            #why X transpose::: note: X is n*f matrix and y is 1*f matrix:::: n:num of samples, f:num of features
            #check varying_w_and_b.png in same directory for formula
            dw = (2/n_samples) * np.dot(X.T, y_predicted_for_all_samples - y)
            db = (2/n_samples) * np.sum(y_predicted_for_all_samples - y)

            #varying weights using learning rate
            self.weights -= self.learningFactor * dw
            self.bias -= self.learningFactor * db


    def predict(self, X):
        y_predicted = np.dot(X, self.weights) + self.bias
        return y_predicted
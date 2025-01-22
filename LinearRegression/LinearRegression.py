import numpy as np

class LinearRegression:

    def __init__(self, learning_rate=0.01, iterations=1000):
        self.weights = None
        self.bias = 0
        self.learning_rate = learning_rate
        self.iterations = iterations

    def fit(self, X, y):
        samples, features = X.shape
        self.weights = np.zeros(features)

        for _ in range(self.iterations):
            y_pred = np.dot(X, self.weights) + self.bias
            dw = -(2 / samples) * np.dot(X.T, (y - y_pred))
            db = -(2 / samples) * np.sum(y - y_pred)
            self.weights = self.weights - self.learning_rate * dw
            self.bias = self.bias - self.learning_rate * db

    def predict(self, X):
        y_pred = np.dot(X, self.weights) + self.bias
        return y_pred
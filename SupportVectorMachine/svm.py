import numpy as np

class SupportVectorMachine: 

    def __init__(self, learning_rate=0.01, iterations=1000, regularization=0.01):
        self.learning_rate = learning_rate
        self.iterations = iterations
        self.reg_param = regularization
        self.weights = None
        self.bias = 0

    def training(self, X, y):
        samples, features = X.shape
        self.weights = np.zeros(features)
    
        for _ in range(self.iterations):
            for i in range(samples):
                margin = y[i] * (np.dot(self.weights, X[i]) + self.bias)

                if margin >= 1:
                    dw = self.weights
                    db = 0
                else:
                    dw = self.weights - self.reg_param * y[i] * X[i]
                    db = -self.reg_param * y[i]
                
                self.weights = self.weights - self.learning_rate * dw
                self.bias = self.bias - self.learning_rate * db

    def predict(self, X):
        z = np.dot(self.weights, X) + self.bias
        if z >= 0:
            return 1
        else:
            return -1
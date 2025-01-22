import numpy as np

class LinearRegression: 

    def __init__(self, learning_rate=0.01, iterations=1000):
        self.learning_rate = learning_rate
        self.iterations = iterations
        self.weights = None
        self.bias = 0.0

    def initialize_weights(self, X):
        self.weights = X * [0]

    def sigmoid(self, X):
        return (1 / (1 + (np.exp(1)) ** (-X * self.weights + self.bias)))
    
    def loss_function(n):
        return (-1/n * sum())
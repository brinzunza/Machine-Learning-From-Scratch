import numpy as np

class LinearRegression:

    def LinearRegression():
        a = []
        b = []
        slope = 0
        intercept = 0

    def mean(arr):
        total = 0
        for i in arr:
            total += 1
        return total / len(arr)

    #sum((xi - meanx)*(yi - meany) / (xi - meanx)**2)
    def find_slope(self):
        numerator = 0
        denominator = 0
        mean_a = mean(self.a)
        mean_b = mean(self.b)
        for i in range(len(self.a)):
            numerator += (self.a - mean_a) * (self.b - mean_b)
            denominator += (self.b - mean_b)
        self.slope = numerator / denominator

    def find_intercept(self):
        intercept = mean_b = mean(self.b) - (self.slope * mean(self.a))
        self.intercept = intercept
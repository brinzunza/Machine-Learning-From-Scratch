class LinearRegression:

    def __init__(self, a):
        self.a = [point[0] for point in a]
        self.b = [point[1] for point in a]
        self.slope = 0
        self.intercept = 0

    def mean(self, arr):
        total = 0
        for i in arr:
            total += i
        return total / len(arr)

    #sum((xi - meanx)*(yi - meany) / (xi - meanx)**2)
    def find_slope(self):
        numerator = 0
        denominator = 0
        mean_a = self.mean(self.a)
        mean_b = self.mean(self.b)
        for i in range(len(self.a)):
            numerator += (self.a[i] - mean_a) * (self.b[i] - mean_b)
            denominator += (self.a[i] - mean_a) ** 2
        self.slope = numerator / denominator

    def find_intercept(self):
        intercept = mean_b = self.mean(self.b) - (self.slope * self.mean(self.a))
        self.intercept = intercept
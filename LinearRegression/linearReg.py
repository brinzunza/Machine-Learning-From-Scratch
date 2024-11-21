'''
Logic 
- ?a hypothesis function for current model predictions
- from existing dataset, create a loss function to evaluate current performance (starter linear function can be 0, 0 for a, b respectively)
- compute gradient descent and adjust model parameters based on learning rate and iterations
- update parameters based on results from gradient descent
'''

class LinearReg:

    def __init__(self):
        self.weight = 0
        self.bias = 0
        self.points = []

    def loss_function(self):
        for i in range(len(self.points)):
            error += (self.points[i][1] - ('''result of current equation with input i as x'''))**2

        mse = error / len(self.points)
        return mse
    
    def update_parameters(self):
        

    def gradient_descent(self, iterations):
        for i in range(iterations):


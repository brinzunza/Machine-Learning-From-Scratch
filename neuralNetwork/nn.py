import math
import random

def initialize_network(n_inputs, n_hidden, n_outputs):
    network = []
    hidden_layer = []
    output_layer = []

    for i in range(n_hidden):
        neurons = {}
        neurons['weight'] = [random.random() * 0.1 for _ in range(n_inputs)]
        neurons['bias'] = random.random() * 0.1
        hidden_layer.append(neurons)    
    network.append(hidden_layer)

    for i in range(n_outputs):
        neurons = {}
        neurons['weight'] = [random.random() * 0.1 for _ in range(n_hidden)]
        neurons['bias'] = random.random() * 0.1
        output_layer.append(neurons)
    network.append(output_layer)

    return network

def sigmoid(x):
    return 1 / (1 + math.e ** -x)

def sigmoid_derivative(x):
    return x * (1 - x)

def forward_propagation(network, inputs):
    current_inputs = inputs
    for layer in network: 
        new_inputs = []
        for neuron in layer:
            totalSum = sum(weight * input_val for weight, input_val in zip(neuron['weight'], current_inputs)) + neuron['bias']
            neuron['output'] = sigmoid(totalSum)
            new_inputs.append(neuron['output'])
        current_inputs = new_inputs
    return current_inputs

def loss(expected_output, actual_output):
    sum_squared_differences = sum((expected_output[i] - actual_output[i])**2 for i in range(len(expected_output)))
    return sum_squared_differences

def backpropagation(network, expected_output, learning_rate):
    for neuron, expected in zip(network[-1], expected_output):
        error = expected - neuron['output']
        delta = error * sigmoid_derivative(neuron['output'])
        neuron['delta'] = delta

    for i in range(len(network) - 2, -1, -1):
        layer = network[i]
        next_layer = network[i + 1]
        for j, neuron in enumerate(layer):
            totalSum = sum(next_neuron['delta'] * next_neuron['weight'][j] for next_neuron in next_layer)
            neuron['delta'] = totalSum * sigmoid_derivative(neuron['output'])

    for i in range(1, len(network)):
        previous_layer = network[i - 1]
        for j, neuron in enumerate(network[i]): 
            for k in range(len(neuron['weight'])):
                neuron['weight'][k] += learning_rate * neuron['delta'] * previous_layer[k]['output']
            neuron['bias'] += learning_rate * neuron['delta']

def train_network(network, dataset, learning_rate, n_epochs):
    for epoch in range(n_epochs):
        total_loss = 0
        for input, expected_output in dataset:
            output = forward_propagation(network, input)
            current_loss = loss(expected_output, output)
            total_loss += current_loss
            backpropagation(network, expected_output, learning_rate)
        print ("Epoch", epoch, "Loss:", total_loss)

def predict(network, inputs):
    return forward_propagation(network, inputs)
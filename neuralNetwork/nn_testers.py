import numpy as np
from sklearn.datasets import load_digits
from nn import initialize_network, train_network, predict

digits = load_digits()

X = digits.data / 16
y = digits.target

def one_hot_encode(labels, n_classes):
    return np.eye(n_classes)[labels]

y_encoded = one_hot_encode(y, 10)

dataset = list(zip(X, y_encoded)) #tuples

n_inputs = 64 #8x8 images flattened
n_hidden = 10
n_outputs = 10 
learning_rate = 0.1
n_epochs = 100

network = initialize_network(n_inputs, n_hidden, n_outputs)

train_network(network, dataset, learning_rate, n_epochs)

print("Testing predictions...")
for i in range(5):
    output = predict(network, X[i])
    predicted_label = np.argmax(output) 
    actual_label = np.argmax(y_encoded[i])
    print(f"Predicted: {predicted_label}, Actual: {actual_label}")

import numpy as np

# Input data and output labels
X = np.array([[2, 9], [1, 5], [3, 6]], dtype=float)
y = np.array([[92], [86], [89]], dtype=float)

# Normalize the input data and output labels
X = X / np.amax(X, axis=0)  # Maximum of X array longitudinally
y = y / 100  # Normalize output labels to range [0, 1]

# Sigmoid Function
def sigmoid(x):
    return 1 / (1 + np.exp(-x))

# Derivative of Sigmoid Function
def derivatives_sigmoid(x):
    return x * (1 - x)

# Variable initialization
epoch = 5  # Setting training iterations
lr = 0.1  # Setting learning rate

inputlayer_neurons = 2  # Number of features in data set
hiddenlayer_neurons = 3  # Number of hidden layers neurons
output_neurons = 1  # Number of neurons at output layer

# Weight and bias initialization
wh = np.random.uniform(size=(inputlayer_neurons, hiddenlayer_neurons))
bh = np.random.uniform(size=(1, hiddenlayer_neurons))
wout = np.random.uniform(size=(hiddenlayer_neurons, output_neurons))
bout = np.random.uniform(size=(1, output_neurons))

# Training the neural network
for i in range(epoch):
    # Forward Propagation
    hinp1 = np.dot(X, wh)
    hinp = hinp1 + bh
    hlayer_act = sigmoid(hinp)
    outinp1 = np.dot(hlayer_act, wout)
    outinp = outinp1 + bout
    output = sigmoid(outinp)

    # Backpropagation
    EO = y - output  # Error at output
    outgrad = derivatives_sigmoid(output)  # Gradient at output
    d_output = EO * outgrad  # Adjust output error based on the gradient
    EH = d_output.dot(wout.T)  # Error at hidden layer
    hiddengrad = derivatives_sigmoid(hlayer_act)  # Gradient at hidden layer

    d_hiddenlayer = EH * hiddengrad  # Adjust hidden layer error based on the gradient

    # Update weights and biases
    wout += hlayer_act.T.dot(d_output) * lr  # Weight update for output layer
    wh += X.T.dot(d_hiddenlayer) * lr  # Weight update for hidden layer

    # Print training progress
    print(f"-----------Epoch-{i + 1} Starts----------")
    print("Input: \n", X)
    print("Actual Output: \n", y)
    print("Predicted Output: \n", output)
    print(f"-----------Epoch-{i + 1} Ends----------\n")

# Final output
print("Final Input: \n", X)
print("Final Actual Output: \n", y)
print("Final Predicted Output: \n", output)
print(np.mean(y==output))
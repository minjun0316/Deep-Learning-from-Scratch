import numpy as np
from ch3_2_4Sigmoid import sigmoid, identity

# input layer computation
X = np.array([1.0, 0.5])
W1 = np.array([[0.1, 0.3, 0.5],[0.2, 0.4, 0.6]])
B1 = np.array([0.1, 0.2, 0.3])
A1 = np.dot(X, W1) + B1
Z1 = sigmoid(A1)
print("input layer")
print("shape of X, W1, B1:", X.shape, W1.shape, B1.shape)
print("A1:", A1, "\nZ1:", Z1)
print()

# second layer computation
W2 = np.array([[0.1, 0.4], [0.2, 0.5], [0.3, 0.6]])
B2 = np.array([0.1, 0.2])
A2 = np.dot(Z1, W2) + B2
Z2 = sigmoid(A2)
print("second layer")
print("shape of Z1, W2, B2:", Z1.shape, W2.shape, B2.shape)
print("A2:", A2, "\nZ2:", Z2)
print()\

# third layer computation
W3 = np.array([[0.1, 0.3], [0.2, 0.4]])
B3 = np.array([0.1, 0.2])
A3 = np.dot(Z2, W3) + B3
Y = identity(A3)
print("output layer")
print("shape of Z2, W3, B3:", Z2.shape, W3.shape, B3.shape)
print("A3:", A3, "\nY:", Y)
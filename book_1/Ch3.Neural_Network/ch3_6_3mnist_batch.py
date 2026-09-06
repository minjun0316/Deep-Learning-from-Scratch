import numpy as np
from mnist import load_mnist
import pickle
from ch3_2_4Sigmoid import sigmoid
from ch3_5_5softmax import softmax

def get_data():
    (x_train, t_train), (x_test, t_test) = load_mnist(normalize=True, flatten=True, one_hot_label=False)

    return x_test, t_test

def init_network():
# f = open("sample_weight.pkl", 'rb')
# "sample_weight.pkl" is the file path, and 'rb' is the file mode (read binary).
# f is a file object.
# We can use open() without with, but we have to close the file manually after using it.
# By using with, the file is closed automatically when the block ends.
    with open("sample_weight.pkl", 'rb') as f:
        network = pickle.load(f)

    return network

def predict(network, x):
    W1, W2, W3 = network['W1'], network['W2'], network['W3']
    b1, b2, b3 = network['b1'], network['b2'], network['b3']

    a1 = np.dot(x, W1) + b1
    z1 = sigmoid(a1)
    a2 = np.dot(z1, W2) + b2
    z2 = sigmoid(a2)
    a3 = np.dot(z2, W3) + b3
    y = softmax(a3)

    return y

if __name__ == '__main__':
    x, t = get_data()
    network = init_network()

    accuracy_cnt = 0
    batch_size = 100
    for i in range(0, len(x), batch_size):
        x_batch = x[i:i+batch_size]
        y_batch = predict(network, x_batch)
        p = np.argmax(y_batch, axis=1)
        accuracy_cnt += np.sum(p == t[i:i+batch_size])

    print("Accuracy:", str(float(accuracy_cnt) / len(x)))
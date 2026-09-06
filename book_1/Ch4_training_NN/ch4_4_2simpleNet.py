import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
import numpy as np
from ch4_2_1CEE import CEE
from ch4_4_1partial_derivative import partial_derivative
from Ch3_Neural_Network.ch3_5_5softmax import softmax

class simpleNet:
    def __init__(self):
        self.W = np.random.randn(2, 3) # 2x3 size random normal distribution matrix

    def predict(self, x):
        a1 = np.dot(x, self.W)
        return softmax(a1)

    def loss(self, x, t):
        y = self.predict(x)
        loss = CEE(y, t)

        return loss
    def f(self, W):
        return self.loss(x, t)


if __name__ == '__main__':
    net = simpleNet()
    print("init W: \n", net.W, "\n")

    x = np.array([0.6, 0.9])
    p = net.predict(x)
    print("predict: ", p, "\n")
    np.argmax(p)

    t = np.array([0, 0, 1])
    L = net.loss(x, t)

    print("Loss: ", L, "\n")

    grad = partial_derivative(net.f, net.W)
    print(grad)


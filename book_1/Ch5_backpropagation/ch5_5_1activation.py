import numpy as np

# Use self.xx when a variable is shared across multiple methods.
class ReLU:
    def __init__(self):
        self.mask = None # mask is array ex) [True, Fals, True, True]

    def forward(self, x):
        self.mask = ( x <= 0 )
        out = x
        out[self.mask] = 0
        return out

    def backward(self, dout):
        dout(self.mask) = 0
        dx = dout
        return dx

class Sigmoid():
    def __init__(self):
        self.out

    def forward(self, x):
        out = 1 / (1 + np.exp(-x))
        self.out = out
        return out

    def backward(self, dout):
        dx = self.out * (1.0 - self.out) * dout
        return dx




if __name__ == '__main__':
    x = np.array([[1.0, -0.5], [-2.0, 3.0]])
    print(x)
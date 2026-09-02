import numpy as np
import matplotlib.pylab as plt
from ch3_2_3step_plot import step_function

def sigmoid(x):
    return 1 / (1 + np.exp(-x))
def identity(x):
    return x


if __name__ == '__main__':
    x1 = np.arange(-5.0, 5.0, 0.1)
    y1 = sigmoid(x1)
    y2 = step_function(x1)
    plt.ylim(-0.1, 1.1)
    plt.plot(x1, y1)
    plt.plot(x1, y2, linestyle="--", color="black")
    plt.show()
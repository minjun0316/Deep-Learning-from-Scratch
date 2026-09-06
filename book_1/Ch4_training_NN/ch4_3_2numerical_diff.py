import numpy as np
import matplotlib.pylab as plt

def function_1(x):
    return 0.01*x**2 + 0.1*x

def numerical_diff(f, x):
    h = 1e-4
    return (f(x+h)-f(x-h))/(2*h)

def tangent_line(x, a, b, gradient):
    return gradient*(x-a)+b

    

if __name__ == '__main__':
    x = np.arange(0.0, 20.0, 0.1)
    y = function_1(x)
    plt.xlabel("x")
    plt.ylabel("f(x)")
    plt.plot(x, y, label="function")

    gradient_5 = numerical_diff(function_1, 5)
    gradient_10 = numerical_diff(function_1, 10)

    y_5 = tangent_line(x, 5, function_1(5), gradient_5)
    y_10 = tangent_line(x, 10, function_1(10), gradient_10)

    plt.plot(x, y_5, label="tangent_5")
    plt.plot(x, y_10, label="tangent_10")
    plt.xlim(0.0, 20.0)
    plt.ylim(-1, function_1(20.0))
    plt.vlines([5, 10], [-1, -1], [function_1(5), function_1(10)], linestyles="--")
    plt.hlines([function_1(5), function_1(10)], [0, 0], [5, 10], linestyles="--")
    plt.scatter(5, function_1(5), color="orange")
    plt.scatter(10, function_1(10), color="green")
    plt.show()


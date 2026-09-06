import numpy as np
from ch4_4_1partial_derivative import partial_derivative

def gradient_descent(f, x_init, lr=0.01, step_num=100):
    x = x_init
    for i in range(step_num):
        grad = partial_derivative(f, x)
        x -= lr*grad
    return x
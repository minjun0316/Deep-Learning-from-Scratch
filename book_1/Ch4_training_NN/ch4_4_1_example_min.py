# calculate minumum of f(x_0, x_1)=x_0^2 + x_1^2 using gradient descent
# x_init = (-3.0, 4.0)
import numpy as np
from ch4_4_1gradient_descent import gradient_descent

def function_2(x):
    return x[0]**2 + x[1]**2

if __name__ == '__main__':
    x_init = np.array([-3.0, 4.0])
    y = gradient_descent(function_2, x_init, lr=0.1, step_num=100)
    print(y)
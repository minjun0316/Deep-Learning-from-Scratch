import numpy as np

'''
# when calculate, exp_x can be very large num because its exponential (ex, e^1000 -> impossible to calculate)
def softmax(x):
    exp_x = np.exp(x)
    sum_exp_x = np.sum(exp_x)
    return exp_x/sum_exp_x
'''

# Instead, we use the mathematical property of softmax that
# adding or subtracting any constant from every logit
# does not change the output of softmax.
# exp(a_k + C) / Σ exp(a_i + C) = exp(a_k) / Σ exp(a_i)
# where C is any constant.


def softmax(x):
    c = np.max(x) # `c` is a scalar, but broadcasting is applied when it is used with a NumPy array.
    exp_x = np.exp(x-c)
    return exp_x / np.sum(exp_x, axis=1, keepdims=True)

if __name__ == '__main__':
    x = np.array([0.3, 2.9, 4.0])
    y = softmax(x)
    print(y)
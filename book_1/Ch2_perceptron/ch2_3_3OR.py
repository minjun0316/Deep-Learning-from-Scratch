import numpy as np

def OR(x1, x2):
    w1, w2, b = 1, 1, -0.5
    x = np.array([x1, x2])
    w = np.array([w1, w2])

    tmp = np.dot(x, w) + b

    if tmp > 0:
        return 1
    else:
        return 0

if __name__ == '__main__':
    print(OR(0, 0))
    print(OR(0, 1))
    print(OR(1, 0))
    print(OR(1, 1))
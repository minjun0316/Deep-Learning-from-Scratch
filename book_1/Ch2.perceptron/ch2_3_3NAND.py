import numpy as np

def NAND(x1, x2):
    w1, w2, b = -1, -1, 1.5
    x = np.array([x1, x2])
    w = np.array([w1, w2])

    tmp = np.sum(w*x) + b
    # tmp = np.dot(x, y) + b

    if tmp > 0:
        return 1
    else:
        return 0

if __name__=='__main__':
    print(NAND(0, 0))
    print(NAND(0, 1))
    print(NAND(1, 0))
    print(NAND(1, 1))
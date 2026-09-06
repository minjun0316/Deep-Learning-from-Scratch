from ch2_3_1AND import AND
from ch2_3_3NAND import NAND
from ch2_3_3OR import OR
import numpy as np

# 다층 퍼셉트론(2층)을 이용해 XOR 구현하기
def XOR(x1, x2):
    s1 = NAND(x1, x2)
    s2 = OR(x1, x2)
    y = AND(s1, s2)
    return y

if __name__=='__main__':
    print(XOR(0, 0))
    print(XOR(0, 1))
    print(XOR(1, 0))
    print(XOR(1, 1))
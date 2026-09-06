# input이 2차원이고, output이 3차원인 NN(Neural Network)를 생각해보면
# output의 계산은 input(x1, x2)와 가중치(w1, w2, w3; w4, w5, w6)의 곱으로 이루어짐
# input : 1x2
# 가중치 : 2x3
# output : 1x3

import numpy as np

X = ([1, 2]) # input x1, x2 행렬
W = ([[1, 3, 5], [2, 4, 6]]) # 가중치 w1, w2, w3, w4, w5, w6 행렬

# bias, 비선형함수 없이 input, 가중치의 곱만 표현한 행렬 곱
Y = np.dot(X, W)
print(Y)


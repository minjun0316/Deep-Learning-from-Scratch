# input size : 2, output size : 3
import numpy as np
from ch3_2_4Sigmoid import sigmoid

# solution_1 : bias를 최종 연산 결과에 더하기
X1 = np.array([1, 2])
W1 = np.array([[1, 2, 3], [4, 5, 6]])
B = np.array([1, 2, 3])
Y1 = np.dot(X1, W1) + B
print("sol1:", Y1)

# solution_2
# input에 항상 1인 원소를 추가하고,
# weight matrix에 bias를 추가하여 하나의 행렬 곱으로 계산
X2 = np.array([1.0, 1.0, 0.5])
W2 = np.array([[0.1, 0.2, 0.3], [0.1, 0.3, 0.5], [0.2, 0.4, 0.6]])
Y2 = np.dot(X2, W2)
print("sol2:", Y2)
Z2 = sigmoid(Y2) # 비선형 함수 포함해서 계산
print("sol2 with sigmoid:", Z2)
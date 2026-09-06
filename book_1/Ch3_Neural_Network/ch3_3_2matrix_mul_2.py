# 3x2 행렬과 2x3 행렬 multiplication
import numpy as np

A = np.array([[1, 2, 3], [4, 5, 6]])
B = np.array([[1, 2], [3, 4], [5, 6]])

print(A.shape, "\n", B.shape)

result1 = np.dot(A, B)
result2 = np.dot(B, A)
print(result1, "\n", result2)
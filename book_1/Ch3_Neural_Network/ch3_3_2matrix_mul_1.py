# 행렬의 곱 계산하기

# 행렬의 곱은 외적, 내적이 아니라 AB 라는 행렬의 곱이 있을 때
# 앞 행렬 A의 행과, 뒤 행렬 B의 열을 내적해 새로운 행렬을 생성하는 것을 말함
# 일반적으로 내적과 외적은 두 벡터 사이에서 정의되며
# 내적은 element-wise로 두 벡터를 곱한 다음에 더해주는 것
# 외적은 두 벡터로 행렬을 만드는 과정을 의미함

import numpy as np

A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])

print(A.shape)
print(B.shape)

print(np.dot(A, B))
# 넘파이 가져오기
#numpy를 np라는 이름(별칭)으로 가져와라
import numpy as np

# numpy 배열 생성하기
x = np.array([1.0, 2.0, 3.0])
print(x)
print(type(x))

# numpy 산술연산
y = np.array([2.0, 4.0, 6.0])

print(x + y)
print(x - y)
print(x / y)
# 넘파이 배열과 스칼라 하나와의 연산도 가능 -> 브로드캐스트
print(x/2.0)

# 넘파이의 N차원 배열
A = np.array([[1, 2], [3, 4]])
print(A)
print("A의 사이즈:", A.shape)
print("A의 데이터타입:", A.dtype)

# 넘파이 행렬의 산술 연산
B = np.array([[3, 0], [0, 6]])
# element-wise summation
print(A + B)
# element-wise multiplication
print(A * B)

print(B)
print(B * 10)
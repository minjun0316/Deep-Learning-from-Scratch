import numpy as np

# 2x3 넘파이 행렬 생성
X = np.array([[51, 55], [14, 19], [0, 4]])
print(X)

# 1행 출력
print(X[0])

# 1행 2열 출력
print(X[0][1])

# for문 접근
for row in X:
    print(row)

print("2차원 반복문")
for row in X:
    for column in row:
        print(column)

# 1차원 배열로 flatten
X = X.flatten()
print(X)

# 넘파이 배열을 인덱스로 사용해서 넘파이 원소 접근
print(X[np.array([0, 2, 4])])

#특정 조건에 해당하는 원소자리의 값만 True인 Boolean 데이터형의 넘파이 배열 출력
print(X>15)
print(X[X>15])
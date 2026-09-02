# 인수 x가 부동소수점만 받아들인다는 단점이 있음 (배열 못받음)
# def step_function(x):
#     if x > 0:
#         return 1
#     else:
#         return 0

# 넘파이 배열을 받을 수 있는 코드
def step_function(x):

    # 0보다 큰지, 작은지로 구분해서 True, False 배열 리턴
    y = x > 0
    # True False를 .astype(int) 함수를 통해 정수형 1또는 0으로 변환
    return y.astype(int)
    # Numpy 배열의 자료형을 벼환할 때 astype() 메서드 사용
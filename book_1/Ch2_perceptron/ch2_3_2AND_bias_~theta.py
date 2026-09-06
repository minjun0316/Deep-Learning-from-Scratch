import numpy as np

def AND(x1, x2):
    # bias는 -theta 여야 함 "w1*x1 + w2*x2 - b = 0"을 기준으로 활성화를 결정하기 때문
    w1, w2, b = 1.0, 1.0, -1.5
    x = np.array([x1, x2])
    w = np.array([w1, w2])


    tmp = np.sum(w*x) + b # 내적 계산인데 방법이 따로 있음 밑에 주석 확인
    #tmp = np.dot(w, x) + b

    if tmp>0:
        return 1
    else:
        return 0

if __name__==__name__:
    print(AND(0, 0))
    print(AND(0, 1))
    print(AND(1, 0))
    print(AND(1, 1))
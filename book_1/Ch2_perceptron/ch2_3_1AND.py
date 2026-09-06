def AND(x1, x2):
    w1, w2, theta = 0.5, 0.5, 0.8 # user가 정의하는 값
    tmp = w1*x1 + w2*x2
    if tmp <= theta:
        return 0
    else:
        return 1

if __name__=='__main__':
    print(AND(0, 0))
    print(AND(0, 1))
    print(AND(1, 0))
    print(AND(1, 1))
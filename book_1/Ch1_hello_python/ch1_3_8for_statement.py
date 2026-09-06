# in과 list가 붙어있음
for i in[1, 2, 3]:
    print(i, end=" ")
print()
# in과 list가 떨어져있음
for i in [1, 2, 3]:
    print(i, end=" ")
print()

a = [1, 2, 3]
# list를 변수 a로 받음
for i in a:
    print(i, end=" ")
print()
# range(a, b) : a부터 b-1까지의 정수 범위를 나타내는 range 객체 생성
# range 객체는 iterable 객체이기 때문에 list처럼 for문에서 사용 가능
for i in range(1, 3):
    print(i, end=" ")
print()

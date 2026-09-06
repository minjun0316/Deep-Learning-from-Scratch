# 특정 기능을 수행하는 일련의 명령어들을 묶어 하나의 함수로 정의할 수 있음

def hello():
    print("Hello World")

hello()

def hello_something(something):
    print("Hello " + something + "!")

hello_something("cat")
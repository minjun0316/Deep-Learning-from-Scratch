class Man:
    # 초기화 메서드 : 클래스의 객체(인스턴스)가 생성될 때 자동으로 호출되는 메서드
    # 객체 자체를 생성하는 메서드는 __new__이고, __init__은 생성된 객체를 초기화하는 메서드
    def __init__(self, name):
        self.name = name
        print("initialized")

    # 메서드의 정의 : 해당 클래스로 생성된 객체가 사용할 수 있는 기능들
    # 함수는 클래스와 독립적으로 정의된 함수.
    # 메서드는 클래스 내부에 정의되어, 해당 클래스 객체와 연관되어 동작하는 함수.
    def hello(self):
        print("Hello " + self.name + "!")

    # self : 현재 이 메서드를 호출한 객체 
    # 예를 들어 m.name 대신 class 내부에서는 self.name 사용
    def goodbye(self):
        print("Good-bye" + self.name + "!")

m = Man("minjun")
m.hello()
m.goodbye()
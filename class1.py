# class1.py

# 클래스 형식을 정의
class Person:
    # 초기화 메서드
    def __init__(self):
        # 인스턴스 멤버 변수 초기화
        self.name = 'default name'
    def print(self):
        print("My name is {0}".format(self.name))

# 인스턴스 생성
p1 = Person()
p2 = Person()

# 메서드 호출
p1.name = "전우치"
p1.print()
p2.print()

# 아래처럼 강제 할당 no 클래스에 추가해서 쓰자.
Person.title = "new title"
print(p1.title, p2.title)
print(Person.title)
# 인스턴스에 추가도 no
p1.age = 30
print(p1.age)
print(p2.age)
print(Person.age)
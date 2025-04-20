# 아래에 코드를 작성하시오.
'''
3431. OOP 기본 활용 2 - 클래스 상속 연습 Lv4
요구사항
Animal 클래스를 정의한다.
Animal 클래스는 이름을 인자로 받는 생성자 메서드를 가진다.
Animal 클래스는 speak 메서드를 가진다. 이 메서드는 자식 클래스에서 오버라이딩된다.
Dog와 Cat 클래스를 정의하고, Animal 클래스를 상속받는다.
Dog 클래스는 speak 메서드를 오버라이딩하여 "Woof!"를 반환한다.
Cat 클래스는 speak 메서드를 오버라이딩하여 "Meow!"를 반환한다.

Flyer와 Swimmer 클래스를 정의한다.
Flyer 클래스는 fly 메서드를 가진다. 이 메서드는 "Flying"을 반환한다.
Swimmer 클래스는 swim 메서드를 가진다. 이 메서드는 "Swimming"을 반환한다.
Duck 클래스를 정의하고, Flyer와 Swimmer 클래스를 다중 상속받는다.
Duck 클래스는 Animal 클래스를 상속받고, 이름을 인자로 받는 생성자 메서드를 가진다.
Duck 클래스는 speak 메서드를 오버라이딩하여 "Quack!"을 반환한다.
make_animal_speak 함수를 정의한다.
이 함수는 Animal 타입의 객체를 인자로 받아, 해당 객체의 speak 메서드를 호출하고 결과를 출력한다.
코드를 실행하고, 출력 결과를 확인한다.
'''

class Animal():
    def __init__(self, name):
        self.name = name
    
    def speak(self):
        pass

class Dog(Animal):
    def __init__(self, name):
        super().__init__(name)
    
    def speak(self):
        print("Woof!")

class Cat(Animal):
    def __init__(self, name):
        super().__init__(name)
    
    def speak(self):
        print("Meow!")

class Flyer():
    def __init__(self):
        pass
    
    def fly(self):
        print("Flying")

class Swimmer():
    def __init__(self):
        pass

    def swim(self):
        print("Swimming")

class Duck(Flyer, Swimmer, Animal):
    def __init__(self, name):
        self.name = name
    
    def speak(self):
        print("Quack!")

def make_animal_speak(object):
    object.speak()

dog = Dog('개')
cat = Cat('고양이')
duck = Duck('오리')

make_animal_speak(dog)
make_animal_speak(cat)
make_animal_speak(duck)
duck.fly()
duck.swim()
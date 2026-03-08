class Animal:
    def __init__(self, name):
        self.name = name
    def speak(self):
        return"..." #建立父類別

class Dog(Animal):
    def speak(self):
        return "Woof!" #覆寫speak()

class Cat(Animal):
    def speak(self):
        return "Meow!" #覆寫speak()
animals = [
    Dog("Lucky"),
    Cat("Mimi"),
    Dog("Jack")
]

for a in animals: #從animal輪流取值
    print(f"{a.name} says: {a.speak()}")
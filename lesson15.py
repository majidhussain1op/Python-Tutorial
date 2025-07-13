class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print(f"{self.name} is making a sound.")

class Dog(Animal):
    def bark(self):
        print(f"{self.name} says : woof!")

d = Dog("Tommy")

d.speak()

d.bark()

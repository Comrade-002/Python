#Parent class
class Animal:
    def move(self):
        print("Animal is walking")

#Child class
class Dog(Animal):
    def bark(self):
        print("Dog is barking")

a = Animal()
d = Dog()
a.move()
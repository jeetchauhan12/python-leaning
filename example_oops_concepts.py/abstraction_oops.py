# Program 1: Abstract class with abstract methods

from abc import ABC, abstractmethod

class Animal:

    @abstractmethod
    def sound(self):
        pass

    @abstractmethod
    def eat(self):
        pass

    @abstractmethod
    def color(self):
        pass

class Cat(Animal):

    def sound(self):
        print("Cat Mewo Mewo")

    def eat(self):
        print(f"Cat is eating Non/Veg , Veg {self.eat}")

    def color(self):
        print(f" The color of Cat is White{self.color}")


class Dog(Animal):

    def sound(self):
        print("Dog Is Barking")

    def eat(self):
        print("Dog is eating Non/veg , Veg ")

    def color(self):
        print("The Color of Dog is the Black" )

d = Dog()
d.sound()
d.eat()
d.color()

c = Cat()
c.sound()
c.eat()
c.color()


# Program 2: Abstract class Shape implemented by child classes

from abc import ABC, abstractmethod
import math


class Shape(ABC):

    @abstractmethod
    def area(self):
        pass


class Circle(Shape):
    def __init__(self):
        self.radius = int(input("Enter the radius of the Circle: "))

    def area(self):
        return math.pi * self.radius * self.radius


class Rectangle(Shape):
    def __init__(self):
        self.length = int(input("Enter the length of the Rectangle: "))
        self.width = int(input("Enter the width of the Rectangle: "))

    def area(self):
        return self.length * self.width


c = Circle()
print("Circle Area:", c.area())

r = Rectangle()
print("Rectangle Area:", r.area())


# Program 3: Error raised if abstract methods are not implemented

from abc import ABC, abstractmethod

class Vehicle(ABC):

    @abstractmethod
    def start(self):
        pass

class Car(Vehicle):
    pass

c = Car()


# Program 4: Real-world abstraction example (ATM)
from abc import ABC, abstractmethod

class ATM(ABC):

    @abstractmethod
    def withdraw(self, amount):
        pass

    @abstractmethod
    def check_balance(self):
        pass

class BankATM(ATM):
    def __init__(self):
        self.balance = 5000

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print("Withdrawn:", amount)
        else:
            print("Insufficient balance")

    def check_balance(self):
        print("Balance:", self.balance)

atm = BankATM()
atm.check_balance()
atm.withdraw(2000)
atm.check_balance()




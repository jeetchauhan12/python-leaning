# Emaple 1 :- Write a program demonstrating single inheritance.

class Animal:
    def eat (self):
        print("Animal Is Eating")
    
    def sleep(self):
        print("Animal is Sleeping")


class Dog(Animal):

    def bark(self):
        print("Dog is Barking")

    def run(self):
        print("Dog is Running Behnind me")
    
    def cry(self):
        print(f"Dog is Crying like 'Bow Bow'{self.cry}")
dog = Dog()
dog.eat()
dog.sleep()
dog.bark()
dog.run()
dog.cry()

# Example 2 :- Write a program demonstrating hierarchical inheritance.

class Animal:
    def eat (self):
        print("Animal Is Eating")
    
    def sleep(self):
        print("Animal is Sleeping")


class Dog(Animal):

    def bark(self):
        print("Dog is Barking")

    def run(self):
        print("Dog is Running Behnind me")
    
    def cry(self):
        print(f"Dog is Crying like 'Bow Bow'{self.cry}")


class Cat(Animal):

    def speck(self):
        print(f"cat is specking like 'Meow Meow'{self.speck}")
    
    def jump(self):
        print("cat is Jump High as Compare To the Dog")

    def looks(self):
        print("cat is looks like a Lioness")
    
    def play(self):
        print("cat is playing with Dog ")

dog = Dog()
cat = Cat()
dog.eat()
dog.sleep()
dog.bark()
dog.run()
dog.cry()
cat.jump()
cat.speak()
cat.looks()
cat.play()

# Example 3 :- Write a program demonstrating multilevel inheritance.

class Vehicle:

    def start(self):
        print("Vehicle started")

class Car(Vehicle):

    def drive(self):
        print("Car is driving")
    
    def color(self):
        print("Car color is Marron")
  
    def Name(self):
        print(f"Auto_Biography Car made by Rang_Rover {self.Name}")

class ElectricCar(Car):

    def charge(self):
        print("Electric car is charging")
    
    def drive(self):
        print("Electrical Car was drive Automatic ")

    def compnay(slf):
        print("Name of Car is the Tesla made by the Elon Musk")

    def color(self):
        print(f"Color of the Car{self.color} ")
    
e = ElectricCar()
e.start()
e.drive()
e.charge()
e.compnay()
e.color()

c = Car()
c.start()
c.Name()
c.color()
c.drive()
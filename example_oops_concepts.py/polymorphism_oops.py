# 1. Real-Life Example of Polymorphism

class Vehicle:
    def move(self):
        pass

class Car(Vehicle):
    def move(self):
        print("Car drives on the road")

class Boat(Vehicle):
    def move(self):
        print("Boat sails on water")

class Plane(Vehicle):
    def move(self):
        print("Plane flies in the air")

vehicles = [Car(), Boat(), Plane()]

for v in vehicles:
    v.move()

# 1. Same Method Name, Different Behavior (Polymorphism)

class Calculator:
    def add(self, a, b=0, c=0):
        return a + b + c

calc = Calculator()
print(calc.add(5))
print(calc.add(5, 10))
print(calc.add(5, 10, 15))



# 2. Same Method Name, Different Behavior (Polymorphism)

class Calculator:
    def add(self, a, b=0, c=0):
        return a + b + c

calc = Calculator()
print(calc.add(5))
print(calc.add(5, 10))
print(calc.add(5, 10, 15))


# 3. Polymorphism Using Parent Reference

class Shape:
    def area(self):
        pass

class Rectangle(Shape):
    def area(self):
        return 10 * 5

class Circle(Shape):
    def area(self):
        return 3.14 * 7 * 7

shapes = [Rectangle(), Circle()]

for shape in shapes:
    print(shape.area())

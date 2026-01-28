# What is OOP?
# Object-Oriented Programming $ (OOP) is a programming paradigm that organizes code using objects and classes instead of functions and logic alone.

#Class
#A class is a blueprint/template for creating objects.

#Object
#An object is an instance of a class.

class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

s1 = Student("Jeet", 22)
print(s1.name)
print(s1.age)


class Color:
    def __init__(self, color_name):
        self.name = color_name  
        self.hex = "#FF0000"
c1 = Color("Red")
print(c1.name)
print(c1.hex)


class Student:
    def __init__(self, name: str, age: int, grade: str):
        self.name = name
        self.age = age
        self.grade = grade

    def display_info(self) -> None:
        """Display student information."""
        print(f"Name: {self.name}, Age: {self.age}, Grade: {self.grade}")



class employee:
    def __init__(self):

        self.id = int(input("Enter Employee ID: "))
        self.name = input("Enter Employee Name: ")
        self.salary = int(input("Enter Employee Salary: "))

    def display(self):

        print("Employee ID:", self.id)
        print("Employee Name:", self.name)
        print("Employee Salary:", self.salary)

employee = employee()
employee.display()


class student:
    def __init__(self):
        self.name = input(f"Enter the Student Name: ")
        self.age = int(input("Enter the Student Age: "))
        self.roll_number = int(input("Enter the roll_number:"))
        self. standerd = input("Enter the standerd:")

    def display(self):
        print("Student Name:", self.name)
        print("Student Age:", self.age)
        print("Student Roll Number:", self.roll_number)
        print("Student Standerd:", self.standerd)
student = student()
student.display()
















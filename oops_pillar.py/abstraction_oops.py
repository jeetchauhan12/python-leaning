#2️⃣ ABSTRACTION
#🧠 WHAT IS IT? Abstraction means hiding internal details and showing only what is needed.

#👉 Like a TV remote:
# You press buttons
# You don’t know internal circuits

#❓ WHY USE IT?
#Reduce complexity
# Focus on usage, not logic
# Easy to use system

#📍 WHERE USED?
# APIs
# Libraries
# Frameworks
# Payment gateways

#⏰ WHEN TO USE?
# When implementation is complex
# When user should not see logic

#👤 WHO USES IT?
# Library developers
# Framework designers

#⚙️ HOW TO USE?
# Using:
# abc module
# Abstract methods


# Example of the Abstraction in Python

# Example 1

from abc import ABC, abstractmethod #ABC : Abstract Base Class

class Employee(ABC):

    @abstractmethod
    def get_salary(self):
        pass

    @abstractmethod
    def get_bonus(self):
        pass

    @abstractmethod
    def view_display(self):
        pass


class Employee_Details(Employee):

    def __init__(self):
        self.id = int(input("Enter the Employee ID: "))
        self.name = input("Enter the Employee Name: ")
        self.__salary = float(input("Enter the Employee Salary: "))
        self.__bonus = int(input("Enter the Employee Bonus: "))

    def get_salary(self):
        return self.__salary

    def get_bonus(self):
        return self.__bonus

    def view_display(self):
        print("Employee ID:", self.id)
        print("Employee Name:", self.name)
        #print("Employee Salary:", self.__salary)
        #print("Employee Bonus:", self.__bonus)


emp = Employee_Details()
emp.view_display()
#print("Employee Salary:", emp.get_salary())
#print("Employee Bonus:", emp.get_bonus())

# Example 2.

from abc import ABC, abstractmethod  # ABC = Abstract Base Class


class Student(ABC):

    @abstractmethod
    def get_roll_number(self):
        pass

    @abstractmethod
    def get_percentage(self):
        pass

    @abstractmethod
    def get_surname(self):
        pass

    @abstractmethod
    def view_details(self):
        pass


class Student_Details(Student):

    def __init__(self):
        self.name = input("Enter the Student Name: ")
        self.age = int(input("Enter Your Age: "))
        self.grade = input("Enter the Grade: ")
        self.__roll_number = int(input("Enter the Roll Number: "))
        self.__percentage = float(input("Enter the Percentage: "))
        self.__surname = input("Enter the Surname: ")

    def get_roll_number(self):
        return self.__roll_number

    def get_percentage(self):
        return self.__percentage

    def get_surname(self):
        return self.__surname

    def view_details(self):
        print("Student Name       :", self.name)
        print("Student Age        :", self.age)
        print("Student Grade      :", self.grade)
        #print("Student Roll Number:", self.__roll_number)
        # print("Student Percentage :", self.__percentage)
        #print("Student Surname    :", self.__surname)


std = Student_Details()
std.view_details()
#print("Student Roll Number:", std.get_roll_number())
#print("Student Percentage :", std.get_percentage())
#print("Student Surname    :", std.get_surname())









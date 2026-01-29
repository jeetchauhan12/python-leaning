# example !1

class Student:

    def get_roll_number(self):
        pass

    def get_percentage(self):
        pass

    def get_surname(self):
        pass

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
        print("Student Name :", self.name)
        print("Student Age  :", self.age)
        print("Student Grade:", self.grade)


std = Student_Details()
std.view_details()







class Employee:
    def get_salary(self):
        pass

    def get_bonus(self):
        pass

    def view_display(self):
        pass


class FullTimeEmployee(Employee):
    def __init__(self):
        self.emp_id = int(input("Enter Employee ID: "))
        self.name = input("Enter Employee Name: ")
        self.salary = float(input("Enter Monthly Salary: "))
        self.bonus = float(input("Enter Bonus Amount: "))

    def get_salary(self):
        return self.salary

    def get_bonus(self):
        return self.bonus

    def view_display(self):
        print("Employee ID:", self.emp_id)
        print("Employee Name:", self.name)
        print("Total Pay:", self.get_salary() + self.get_bonus())

emp = FullTimeEmployee()
emp.view_display()

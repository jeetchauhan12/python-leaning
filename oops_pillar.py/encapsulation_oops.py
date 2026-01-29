# 1️⃣ ENCAPSULATION
# 🧠 WHAT IS IT?
#Encapsulation means wrapping data and methods together and protecting data from outside misuse.

# 👉 Like a school bag:
# Books are inside
# Zip protects them
# You access only what is allowed

# ❓ WHY USE IT?                 
#Protect data
#Avoid accidental changes
#Improve security
#Clean and safe code

# 📍 WHERE USED?
#Banking apps
#Login systems
#User profiles
#Employee records

# ⏰ WHEN TO USE?
#When data must be protected
#When values should not be directly modified

# ⚙️ HOW TO USE?
#Using:
#__private_variable
#Getter & Setter methods

# Example of Encapsulation in Python

# Example 1

class Student:
    def __init__(self):
        self.name = input("Enter the Student Name: ")
        self.age = int(input("Enter the Student Age: "))
        self.__roll_number = int(input("Enter the Roll Number: "))
        self.standard = input("Enter the Standard: ")
        self.__percentage = float(input("Enter the Percentage: "))

    def get_roll_number(self):
        return self.__roll_number

    def get_percentage(self):
        return self.__percentage

    def view_details(self):
        print("Student Name:", self.name)
        print("Student Age:", self.age)
        print("Student Roll Number:", self.__roll_number)
        print("Student Standard:", self.standard)
        print("Student Percentage:", self.__percentage)


student = Student()
student.view_details()
print("roll_number:", student.get_roll_number())
print("percentage:", student.get_percentage())
 

# Example 2
class Bank:
    def __init__(self):
        self.__balance = 10000

    def deposit(self, amount):
        self.__balance += amount

    def get_balance(self):
        return self.__balance
print(getattr(Bank(), 'get_balance')())  


# Example 3

class employee:
    def __init__(self):
        self.id = int(input("Enter the Employee ID :"))
        self.name = input("Enter the Employee Name :")
        self.__salary = float(input("Enter the Employee salary :"))
        self.__bonus = int(input("enter the Bonus :"))

    def get_salary(self):
        return self.__salary

    def get_bonus(self):
         return self.__bonus
        
    def view_display(self):
            print("Employee ID :", self.id)
            print("Employee Name :", self.name)
            print("Employee Salary :", self.__salary)
            print("Employee Bonus :",self.__bonus)

emp = employee()
employee.view_display(emp)
print("employee salary :", emp.get_salary())
print("employee bonus :", emp.get_bonus())



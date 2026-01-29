# Parent class
class Student:
    def __init__(self):
        self.name = input("Enter the Student Name: ")
        self.age = int(input("Enter Your Age: "))
        self.grade = input("Enter the Grade: ")
        self.roll_number = int(input("Enter the Roll Number: "))
        self.percentage = float(input("Enter the Percentage: "))
        self.surname = input("Enter the Surname: ")

    def get_roll_number(self):
        return self.roll_number

    def get_percentage(self):
        return self.percentage

    def get_surname(self):
        return self.surname

    def view_details(self):
        print("----- Student Details -----")
        print("Name       :", self.name)
        print("Age        :", self.age)
        print("Grade      :", self.grade)
        print("Roll Number:", self.roll_number)
       # print("Percentage :", self.percentage)
       # print("Surname    :", self.surname)


# Child class inherits Student
class Employee(Student):
    def __init__(self):
        super().__init__()  # Initialize Student details
        self.emp_id = int(input("Enter the Employee ID: "))
        self.salary = float(input("Enter the Employee Salary: "))
        self.bonus = int(input("Enter the Employee Bonus: "))

    def get_salary(self):
        return self.salary

    def get_bonus(self):
        return self.bonus

    # Override view_details to include Employee info
    def view_details(self):
        super().view_details()  # Show student info
        print("----- Employee Details -----")
        print("Employee ID  :", self.emp_id)
        print("Salary       :", self.salary)
        # print("Bonus        :", self.bonus)


# Create object and display details
emp = Employee()
emp.view_details()

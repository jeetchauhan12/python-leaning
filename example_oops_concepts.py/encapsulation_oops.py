# 1) Declare private variables and access them using getter methods (

class Student:
    def __init__(self):
        self.__id = int(input("Enter the Student Id :"))
        self.name = input("Enter the Student Name :")
        self.__percentage = float(input("Enter the Student Percentage :"))
        self.age = int(input("Enter the Student Age :"))

    def get_id(self):
        return self.__id
    
    def get_percentage(self):
        return self.__percentage
    
    def view_details(self):
        print("Student Id :" , self.__id)
        print("Student Name :", self.name)
        #print("Student Percentage :" , self.__percentage)
        #print("Student Age :" , self.age)

std = Student()
std.view_details()
#print("Student Id :" , std.get_id())
#print("Student Percentage :", std.get_percentage())

# Example 2) Create a class Account with private balance and methods deposit() and withdraw().


class Account:
    def __init__(self):
        self.__Account_Number = int(input("Enter the Account Number :"))
        self.__balance = float(input("Enter The Amount:"))
        self.Account_Type = input("Choose one of them like Saving or Current Account :")
        self.__Green_Pin = int(input("Enter the Green Pin:"))
        for i in range(3):
            pin = int(input("Enter the Correct Pin :"))
            if pin == self.__Green_Pin:
                print(f"Your Balance is : {self.__balance}")
                break
            else:
                print("Inter the Correct Green Pin")

        self.age = int(input("Enter the Age :"))

        self.__Phone_Number = int(input("Enter the Phone Number :"))

        self.__Minimum_Balance = 10000
        while self.__balance < self.__Minimum_Balance:
            print(f"Your Balance is below the Minimum Balance of {self.__Minimum_Balance}. Please deposit more funds.")
            deposit_amount = float(input("Enter the amount to deposit: "))
            self.deposit(deposit_amount) 
    
    def deposit(self, amount):
        self.__balance += amount

    def get_Account_Number(self):
        return self.__Account_Number

    def get_Green_Pin(self):
        return self.__Green_Pin
    
    def get_Phone_Number(self):
        return self.__Phone_Number
    
    def get_Minimum_Balance(self):
        return self.__Minimum_Balance

    def view_details(self):
        print("balance :", self.__balance)
        print("Account Type :" , self.Account_Type)
        print("Age :" , self.age)

acc = Account()
acc.view_details()


# Example 3) Prevent direct access to sensitive data

class Employee:
    def __init__(self):
        self.id = int(input("Enter the Employee ID :"))
        self.id_password = input("Enter the Employee Password ;")
    
    def get_id_password(self):
        return self.id_password
       
    def view_displaydetails(self):
        print("Enter the Employee ID : " , self.id)
        print("Enter the Employee Password:", self.get_id_password())

a = Employee()
a.view_displaydetails()
print("Employee Password :", a.get_id_password())



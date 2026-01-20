# 🔹 What is input()?

#input() is used to take input from the user at runtime (keyboard input).

# Important Rule
# input() always returns data as a string (str), even if you type a number.

# Basic Syntax

 #variable_name = input("Message to user: ")

# Example of Input()Functions.

#Simple how to do this thing.

name = input("enter your name:")
print(name)

# Input with Numbers

age = input("Enter your age: ")
print(age)
print(type(age))

# Convert into Integer
age = int(input("Enter your age: "))
print(age)
print(type(age))


# Took Multiple Inputs
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
print(a + b)


# Taking Float Input
price = float(input("Enter price: "))
print(price)





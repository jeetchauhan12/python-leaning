# Built-in Exceptions in Python
# An exception is a runtime error that disrupts normal program execution.
# Python provides several built-in exceptions to handle various error conditions.
# Here are some common built-in exceptions:

# ZeroDivisionError: Raised when attempting to divide by zero.
# 1. ZeroDivisionError

try:
    a = int(input("Enter the Number:-"))
    b = int(input("Enter the Number:-"))
    x = a / b
    print(x)
except ZeroDivisionError:
    print("Cannot divide by zero")

else:
    print("Division is Successfully Done")

#  ValueError: Raised when a function receives an argument of the correct type but inappropriate value.
# 2. ValueError

try:
    A = int(input("Enter the Number:-"))
    print(A)
except ValueError:
    print("Invalid input! please enter an integer.")
else:
    print("Value is SuccessFully Taken")

# IndexError: Raised when trying to access an element from a list using an invalid index.
# 3. IndexError

my_list = [10, 20, 30, 40, 50]
try:
    index = int(input("Enter the index to access the list element: "))
    print(my_list[index])
except IndexError:
    print("Index out of range")
else:
    print("Index is Valid")
    
# TypeError: Raised when an operation or function is applied to an object of inappropriate type.
# 4. TypeError
try:
    num = 5
    text = "Hello"
    result = num + text  # This will raise a TypeError
    print(result)
except TypeError:
    print("Type Error occurred")

# KeyError: Raised when trying to access a dictionary with a key that does not exist.
# 5. KeyError
try:
    data = {"name": "Jeet" , "age":22 }
    print(data["date of birth"])
except KeyError:
    print("Key not found in dictionary")

# FileNotFoundError: Raised when trying to access a file that does not exist.
# 6. FileNotFoundError
try:
     f = open("missing.txt", "r")
except FileNotFoundError:
    print("File does not exist")

















































































































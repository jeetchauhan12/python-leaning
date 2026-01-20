# if condition: statement
# Example 1: Simple Condition

age = 20

if age >= 18:
    print("Eligible to vote")

# Example 2: Using Comparison Operators

a = 10
b = 5

if a > b:
    print("a is greater than b")

# Example 3: Checking if a string is not empty

name = "John"

if name:
    print(f"Hello, {name}!")

# Example 4: Checking if a number is positive

number = 15

if number > 0:
    print(f"{number} is a positive number")

# Example 5: Checking if a number is even

num = 8

if num % 2 == 0:
    print(f"{num} is an even number")

# Example 6: Checking membership in a list

fruits = ["apple", "banana", "orange"]
fruit = "apple"

if fruit in fruits:
    print(f"{fruit} is in the list")

# Example 7: Checking if a value is None

value = None

if value is None:
    print("Value is None")

# Example 8: Checking if a variable exists

username = "John_Doe"

if 'username' in locals():
    print(f"Username exists: {username}")
else:
    print("Username variable does not exist")

# Example 9: Simple authentication check

username = "admin"
password = "12345"

if username == "admin" and password == "12345":
    print("Login successful!")

# Example 10: Check temperature conditions

temperature = 25

if temperature > 30:
    print("It's very hot!")

if temperature < 10:
    print("It's very cold!")

if temperature >= 10 and temperature <= 30:
    print("Temperature is moderate")

# Example 11: Check if user is a student

age = 19
is_student = True

if age >= 18 and is_student:
    print("You are an adult student")

# Example 12: Check score validation

score = 85

if score >= 90:
    print("Grade: A")

if score >= 80 and score < 90:
    print("Grade: B")

if score >= 70 and score < 80:
    print("Grade: C")

# Example 13: Check if list is not empty

my_list = [1, 2, 3, 4, 5]

if len(my_list) > 0:
    print(f"List contains {len(my_list)} items")

# Example 14: Check if dictionary has a key

person = {"name": "Alice", "age": 30}

if "age" in person:
    print(f"Age is {person['age']}")

# Example 15: Check if string contains a substring

text = "Python is awesome"

if "Python" in text:
    print("Text contains 'Python'")


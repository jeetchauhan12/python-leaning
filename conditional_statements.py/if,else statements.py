# If and Else Statements in Python
# Syntax: if condition: statement else: statement

# Example 1: Simple age check

age = 20

if age >= 18:
    print("You are an adult")
else:
    print("You are a minor")

# Example 2: Check if number is positive or negative

number = -5

if number > 0:
    print("Number is positive")
else:
    print("Number is negative or zero")

# Example 3: Check if a string is empty

name = "Alice"

if name:
    print(f"Hello, {name}!")
else:
    print("Name is empty")

# Example 4: Check if password is correct

entered_password = "pass123"
correct_password = "pass123"

if entered_password == correct_password:
    print("Login successful!")
else:
    print("Invalid password")

# Example 5: Check if number is even or odd

num = 7

if num % 2 == 0:
    print(f"{num} is even")
else:
    print(f"{num} is odd")

# Example 6: Check if student passed or failed

marks = 45
passing_score = 50

if marks >= passing_score:
    print("You passed!")
else:
    print("You failed! Better luck next time")

# Example 7: Check voting eligibility

voter_age = 16

if voter_age >= 18:
    print("You can vote")
else:
    print("You are not eligible to vote yet")

# Example 8: Check if item is in a list

fruits = ["apple", "banana", "orange"]
selected_fruit = "mango"

if selected_fruit in fruits:
    print(f"{selected_fruit} is available")
else:
    print(f"{selected_fruit} is not available")

# Example 9: Check if dictionary key exists

student = {"name": "John", "age": 20}

if "age" in student:
    print(f"Age: {student['age']}")
else:
    print("Age not found")

# Example 10: Check user role permissions

user_role = "user"

if user_role == "admin":
    print("You have full access")
else:
    print("You have limited access")

# Example 11: Check temperature

temperature = 5

if temperature > 0:
    print("Water will not freeze")
else:
    print("Water will freeze")

# Example 12: Check if score is passing

score = 35

if score >= 40:
    print("Score is passing")
else:
    print("Score is failing")

# Example 13: Check if person is eligible for senior citizen benefits

person_age = 65

if person_age >= 60:
    print("Eligible for senior citizen benefits")
else:
    print("Not eligible for senior citizen benefits")

# Example 14: Check list status

shopping_list = []

if shopping_list:
    print("Shopping list has items")
else:
    print("Shopping list is empty")



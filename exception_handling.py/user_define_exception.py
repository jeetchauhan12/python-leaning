#🔹 What is a User-Defined Exception?
# A user-defined exception is a custom error created by the programmer to represent application-specific problems.
# It allows developers to define their own exception types by creating new classes that inherit from the built-in Exception class.
# This helps in providing more meaningful error messages and handling specific error conditions in a more controlled manner.

#🔹 Basic Structure
#class CustomError(Exception):
#    pass
# class → creates a new exception type
# Exception → built-in base class
# pass → no extra logic needed for beginners


# Example 1: InvalidAgeError

class InvalidAgeError(Exception):
    pass

age = int(input("Enter age: "))

try:
    if age < 18:
        raise InvalidAgeError("Age must be 18 or above")
    print("Access granted")
except InvalidAgeError as e:
    print(e)

# Example 2 :- NegativeNumberError

class NegativeNumberError(Exception):
    pass

num = int(input("Enter number: "))

try:
    if num < 0:
        raise NegativeNumberError("Negative number not allowed")
    print("Valid number:", num)
except NegativeNumberError as e:
    print(e)

# Example 3 :- InvalidEmailError

class InvalidEmailError(Exception):
    pass

email = input("Enter email: ")

try:
    if "@" not in email:
        raise InvalidEmailError("Invalid email format")
    print("Email accepted")
except InvalidEmailError as e:
    print(e)


































































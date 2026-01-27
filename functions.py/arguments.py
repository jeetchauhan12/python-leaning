# GitHub: https://github.com/jeetchauhan12/python-leaning/tree/main
# What are Arguments?
# Arguments are values passed to a function when calling it.
# They provide input data for the function to process.

a = 60
b = 30



# 1. Positional Arguments
def add(a, b):
    return a + b
result1 = add(10, 20)
print("Addition:", result1)


# 2. Keyword Arguments
def student_info(name, age):
    return f"Name: {name}, Age: {age}"
result2 = student_info(age=21, name="Jeet")
print(result2)


# 3. Default Argument
def power(base, exp=2):
    return base ** exp
result3 = power(5)
result4 = power(5, 3)
print("Power with default exponent:", result3)
print("Power with custom exponent:", result4)


# 4. Variable-length Arguments (*args)
def total_sum(*numbers):
    return sum(numbers)
result5 = total_sum(1, 2, 3, 4, 5)
print("Total Sum:", result5)


# 5. Keyword Variable-length Arguments (**kwargs)
def user_profile(**details):
    return details
result6 = user_profile(name="Jeet", age=21, city="Ahmedabad")
print("User Profile:", result6)


# 6. Mixed Arguments (Positional + Default)
def greet(name, message="Welcome"):
    return f"{message}, {name}"

result7 = greet("Jeet")
result8 = greet("Jeet", "Hello")
print(result7)
print(result8)

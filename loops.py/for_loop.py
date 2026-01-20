# FOR LOOP IN PYTHON
# Description: A for loop repeats a block of code for a specific number of times or for each item in a sequence

# SYNTAX:
# for variable in sequence:
#     statement to execute

print("="*50)
print("FOR LOOP EXAMPLES")
print("="*50)
print()

# Example 1: Print numbers from 1 to 5 using range()
print("Example 1: Print numbers 1 to 5")
for i in range(1, 6):
    print(i)

print()

# Example 2: Loop through a list
print("Example 2: Loop through a list of fruits")
fruits = ["apple", "banana", "orange", "mango"]
for fruit in fruits:
    print(f"I like {fruit}")

print()

# Example 3: Loop through a string
print("Example 3: Loop through letters in a string")
word = "Python"
for letter in word:
    print(letter)

print()

# Example 4: Print multiplication table
print("Example 4: Multiplication table of 5")
number = 5
for i in range(1, 11):
    result = number * i
    print(f"{number} x {i} = {result}")

print()

# Example 5: Calculate sum of numbers
print("Example 5: Sum of numbers 1 to 10")
total = 0
for num in range(1, 11):
    total = total + num
print(f"Sum: {total}")

print()

# Example 6: Count numbers
print("Example 6: Count from 0 to 4")
for count in range(5):
    print(f"Count: {count}")

print()

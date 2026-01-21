# 1. break Statement Definition: The break statement immediately terminates the loop, even if the loop condition is still true.
# The break statement is used to exit a loop prematurely.
# Execution Flow of break

# Loop starts
# Condition is checked
# When break executes:
# Loop stops instantly
# No further iterations
# Loop else block (if any) is skipped

# Example 1

for i in range(1, 10):
    if i == 5:
        break
    print(i)

# Example 2
count = 0
while count < 10:   
    print(count)
    if count == 6:
        break
    count += 1

# Example 3
names = ["Alice", "Bob", "Charlie", "David"]
for name in names:
    if name == "Charlie":
        break
    print(name)     

# Example 4
for letter in 'PythonLoop':
    if letter == 'L':
        break
    print(letter)   

# Example 5
n = 10
while n > 0:
    print(n)
    if n == 4:
        break
    n -= 1

# Example 6
fruits = ["apple", "banana", "cherry", "date"]
for fruit in fruits:
    if fruit == "cherry":
        break
    print(fruit)

# Example 7
for i in range(1, 15):  
    if i == 10:
        break
    print(i)

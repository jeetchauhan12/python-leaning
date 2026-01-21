# continue Statement Definition: The continue statement is used to skip the current iteration of a loop and proceed to the next iteration.
# Execution Flow of continue
# Loop starts
# Condition is checked
# When continue executes:
# Current iteration is skipped
# Next iteration begins
# Loop else block (if any) is not affected

# Example 1 

for i in range(1, 6):
    if i == 3:
        continue
    print(i)

# Example 2
count = 0
while count < 5:
    count += 1
    if count == 3:
        continue
    print(count)

# Example 3
names = ["Alice", "Bob", "Charlie", "David"]
for name in names:
    if name == "Charlie":
        continue
    print(name)

# Example 4
for letter in 'ContinueLoop':
    if letter == 'L':
        continue
    print(letter)

# Example 5
n = 5
while n > 0:
    n -= 1
    if n == 2:
        continue
    print(n)

# Example 6
fruits = ["apple", "banana", "cherry", "date"]
for fruit in fruits:
    if fruit == "banana":
        continue
    print(fruit)

# Example 7
for i in range(1, 10):  
    if i == 7:
        continue
    print(i)

# Example 8
for i in range(1, 11):
    if i % 2 == 0:
        continue
    print(i)

# Example 9
for i in range(10):
    if i > 5:
        continue
    print(i)
    
# Example 10
for char in "abcdefghij":
    if char in 'aeiou':
        continue
    print(char)

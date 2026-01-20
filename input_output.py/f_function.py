# f-Strings (Formatted String Literals)
# What are f-strings?
# f-strings allow direct variable insertion inside strings.
# Introduced in Python 3.6.
# Syntax
# f"Text {variable}"

# Example 1: Basic f-string
name = "Jeet"
age = 21
print(f"My name is {name} and my age is {age}")

# Example 2: Expressions Inside f-strings
a = 10
b = 5
print(f"Sum = {a + b}")


#Example 3: Float Formatting

pi = 3.1415926
print(f"Value of pi is {pi:.2f}")


#Example 4: Alignment and Width

name = "Python"

print(f"{name:>10}") 
# EXPLINE THIS HOW THIS WORK:-
# "Python" → 6 characters
# Width → 10
# Extra spaces → 4
# > means right align

print(f"{name:<10}") 
# EXPLINE THIS HOW THIS WORK:-
 # "Python" → 6 characters
# Width → 10
# Extra spaces → 4
# < means left align

print(f"{name:^10}")

# EXPLINE THIS HOW THIS WORK:-
# "Python" → 6 characters
# Width → 10
# Extra spaces → 4
# ^ means center align
# Spaces split equally:
# Left → 2 spaces
# Right → 2 spaces

# @@@ Why f-strings are Best?
# Fast
# Clean
# Readable
# Recommended by professionals
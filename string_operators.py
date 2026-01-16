# String Operators in Python

# Concatenation (+)
str1 = "Hello"
str2 = "World"
result = str1 + " " + str2
print("Concatenation:", result)

# Repetition (*)
str3 = "Python"
result = str3 * 3
print("Repetition:", result)

# Membership (in)
str4 = "Programming"
if "gram" in str4:
    print("'gram' is in 'Programming'")

# Membership not in
if "xyz" not in str4:
    print("'xyz' is not in 'Programming'")

# Slicing
str5 = "PythonLearning"
print("Slicing [0:6]:", str5[0:6])
print("Slicing [6:]:", str5[6:])

# String Methods
str6 = "hello world"
print("Upper:", str6.upper())
print("Title:", str6.title())
print("Length:", len(str6))

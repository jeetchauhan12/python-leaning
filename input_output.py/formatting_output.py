# Method 1: Using , in print

name = "Jeet"
age = 21
print("Name:", name, "Age:", age)

# Method 2: Using % Formatting (Old Style)

name = "Jeet"
age = 21
print("Name: %s Age: %d" % (name, age))

# Method 3: Using str.format() Method

name = "Jeet"
age = 21
print("Name: {} Age: {}".format(name, age))

# Method 4: Using f-Strings (Python 3.6+)
name = "Jeet"
age = 21
print(f"Name: {name} Age: {age}")
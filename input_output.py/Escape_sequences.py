#| Escape | Function                   |
#| ------ | -------------------------- |
#| `\n`   | Moves to next line         |
#| `\t`   | Horizontal tab             |
#| `\\`   | Prints backslash           |
#| `\'`   | Single quote               |
#| `\"`   | Double quote               |
#| `\b`   | Removes previous character |
# Escape Sequences in Python.

#  1). \n → New Line 
# Meaning

# Moves the cursor to the next line.

# Example 1: Basic New Line
print("Hello\nWorld")


# Example 2: Multiple New Lines
print("Python\nis\npowerful")


 # Example 3: New Line in Sentence
print("Name: Jeet\nAge: 21\nCity: Delhi")


# 2). \t → Tab Space
# Meaning

# Inserts horizontal tab space (usually 4 or 8 spaces depending on system).

# Example 1: Column Alignment

print("Name\tAge\tMarks")
print("Jeet\t21\t85")
print("Amit\t22\t90")


# Example 2: Menu Style Output

print("1.\tStart")
print("2.\tStop")
print("3.\tExit")


# 3). \\ → Backslash

# Meaning :- Used to print a single backslash.
# Why?
# Backslash is a special character, so to print it, you must escape it.


# Example 1: File Path

print("C:\\Users\\Admin\\Documents")


#Example 2: Showing Escape Sequences

print("New line symbol is \\n")

# Common Mistake
print("C:\new\test")

# Correct 
print("C:\\new\\test")

4# 4). \' → Single Quote
# Meaning :- Used to print a single quote inside a string enclosed by single quotes.

# Example 1: Single Quote in Single Quote String
print('It\'s a beautiful day')

# Example 2: Multiple Single Quotes
print('She said, \'Hello!\'')

# Example 3: Single Quote in Double Quote String
print("It's a sunny day")

# 5). \" → Double Quote
# Meaning :- Used to print a double quote inside a string enclosed by double quotes.

# Example 1: Double Quote in Double Quote String
print("He said, \"Hello!\"")

# Example 2: Multiple Double Quotes
print("She said, \"I'm fine.\"")

# Example 3: Double Quote in Single Quote String
print('He said, "Welcome!"')   


# 6). \b → Backspace
# Meaning :- Removes the character before it.

# Example 1: Basic Backspace
print("Hello\bWorld")      # Output: HellWorld

# Example 2: Multiple Backspaces
print("Python\b\b\bJava")  # Output: PytJava

# Example 3: Backspace in Sentence
print("Data\b Science")    # Output: Dat Science






#File Handling in Python
# What is File Handling?
# File handling is the process of creating, reading, writing, and modifying files stored on secondary storage (disk).
# Python provides built-in functions to work with files efficiently.


# Summary
# r → Read file
# w → Write (overwrite)
# a → Append
# with → Best practice


# Example 1: Reading Entire File

file = open("write_read_append.py", "r")
data = file.read()
print(data)
file.close()


# Example 2: Reading File Line by Line (Loop)

file = open("write_read_append.py", "r")

for line in file:
    print(line)

file.close()

# Example 3: Using readline()

file = open("write_read_append.py", "r")
line1 = file.readline()
line2 = file.readline()

print(line1)
print(line2)

file.close()

###################################################################################################################################################


# Example 1 :- Writing to a File (w mode)

file = open("write.py", "w")
file.write("Python File Handling\n")
file.write("Write Mode Example")
file.close()

# Example 2 :- Writing Multiple Lines Using writelines()
file = open("Write.py","w")
data = ["Apple\n", "Banana\n", "Mango\n"]
file.writelines(data)
file.close()


################################################################################################################################################

# Example 1 :- Appending Data to a File

file = open("Write.py", "a")
file.write("\nThis line is appended")
file.close()

# Example 2 :- Read + Append

file = open ("Write.py","a+")
file.seek(5)
print(file.read())
file.write("\nNew data added")
file.close()

# Example 1 Using with Statement (Read)

with open("write.py", "r") as file:
    print(file.read())


# Example 2 Using with Statement (Write)

with open("write.py", "w") as file:
    file.write("Using with statement")
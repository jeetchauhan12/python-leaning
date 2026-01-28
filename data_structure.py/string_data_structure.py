# 5. STRING (Ordered, Immutable, Sequence of Characters) What is a String? A string is a sequence of characters enclosed in quotes. Ordered Immutable Supports slicing and indexing

# 1. Create string

s = "Python"
print(s)

# 2. Access character
print(s[0])

# 3. Negative index
print(s[-1])

# 4. Length
print(len(s))

# 5. Slicing
print(s[1:4])

# 6. Uppercase
print(s.upper())

# 7. Lowercase
print(s.lower())

# 8. Replace
print(s.replace("P", "J"))

# 9. Membership
print("Py" in s)

# 10. Split
text = "Python is easy"
print(text.split())

# 11. Join
words = ["Python", "is", "fun"]
print(" ".join(words))

# 12. Loop through string
for ch in s:
    print(ch)

# 4. Dictionary (Mutable, Ordered Collection) Definition: A dictionary stores data as key-value pairs.

# Example 1: Creating a dictionary

student = {"name": "Jeet", "age": 21}
print(student)

# Example 2: Accessing values by key

data = {"a": 10, "b": 20}
print(data["a"])

# Example 3: Adding a new key-value pair

data["c"] = 30
print(data)

# Example 4: Modifying an existing value
data["b"] = 25
print(data)

# Example 5: Removing elements from dictionary

data = {"x": 1, "y": 2}
data.pop("x")
print(data)

# Example 6: Looping through dictionary

marks = {"Math": 80, "Sci": 90}

for subject, score in marks.items():
    print(subject, score)

# Example 7: Dictionary with mixed data types

info = {"id": 101, "name": "Alice", "is_student": True, "grades": [85, 90, 95]}
print(info)

# Example 8: Nested dictionary

employee = {
    "emp1": {"name": "Bob", "age": 30},
    "emp2": {"name": "Alice", "age": 25}
}
print(employee)

# Example 9: Creating dictionary using dict() function

new_dict = dict(name="Jeet", age=21)
print(new_dict)

# 3. Set (Unordered, Mutable, No Duplicates) Definition: A set stores unique elements only and does not maintain order.

# Example 1: Creating a set

s = {1, 2, 3, 3, 2}
print(s)

# Example 2: Adding and removing elements

s = {10, 20, 30}
s.add(40)
s.remove(20)
print(s)

# Example 3: Checking membership

s = {1, 2, 3}
print(2 in s)
print(5 in s)


# Example 4: Union of sets

a = {1, 2, 3}
b = {3, 4, 5}
print(a.union(b))

# Example 5: Intersection of sets

a = {1, 2, 3}
b = {2, 3, 4}
print(a.intersection(b))

# Example 6: Difference of sets

a = {1, 2, 3}
b = {2, 3}
print(a.difference(b))

# Example 7: Symmetric difference of sets

a = {1, 2, 3}
b = {3, 4, 5}
print(a.symmetric_difference(b))

# Example 8: Set comprehension
squares = {x**2 for x in range(10)}
print(squares)

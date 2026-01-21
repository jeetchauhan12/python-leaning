# 1. List (Mutable, Ordered Collection) Definition: A list is a collection of elements that is: Ordered, Mutable (can be changed), Allows duplicate values, Can store mixed data types.
# Simple example of the list
my_list = [10, 20, 30, "Python", 5.5]

# Example 1
numbers = [1, 2, 3, 4]
numbers[1] = 20
print(numbers)

# Example 2
fruits = ["apple", "banana", "cherry"]
fruits.append("date")
print(fruits)

# Example 3
colors = ["red", "green", "blue"]
colors.insert(1, "yellow")
print(colors)

# Example 4
animals = ["cat", "dog", "rabbit"]
animals.remove("dog")
print(animals)

# Example 5                  
numbers = [1, 2, 3, 4]
numbers.pop(1)
print(numbers)

# Example 6
letters = ['a', 'b', 'c', 'd']
letters.clear()
print(letters)

# Example 7
mixed_list = [1, "two", 3.0, "four"]
print(mixed_list)

# Example 8
nested_list = [1, 2, [3, 4], 5]
print(nested_list)

# Example 9
empty_list = []

 # 2. Tuple (Immutable, Ordered Collection) Definition: A tuple is similar to a list but: Immutable (cannot be modified), Faster than lists, Safer for fixed data.
# SYNTAX
my_tuple = (10, 20, 30)

# Example 1
coordinates = (5, 10)  
print(coordinates)

# Example 2
person = ("Alice", 30, "Engineer")
print(person)

# Example 3
empty_tuple = ()
print(empty_tuple)

# Example 4
single_element_tuple = (42,)
print(single_element_tuple)

# Example 5
mixed_tuple = (1, "two", 3.0, "four")
print(mixed_tuple)

# Example 6
nested_tuple = (1, 2, (3, 4), 5)
print(nested_tuple)

# Example 7
tuple_from_list = tuple([1, 2, 3, 4])   
print(tuple_from_list)

# Example 8
access_element = my_tuple[1]
print(access_element)

# Example 9
print(my_tuple[0])
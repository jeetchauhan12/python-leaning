# What are Built-in Functions?
# Built-in functions are predefined functions provided by Python.
# You can use them directly without importing any module.

def demonstrate_builtin_functions():
    """Demonstrates several common Python built-in functions."""
    print("--- Demonstrating Common Built-in Functions ---")

    # len(): Returns the length of an object.
    len_result = len("Python")
    print(f"len('Python'): {len_result}")

    # type(): Returns the type of an object.
    type_result = type(10)
    print(f"type(10): {type_result}")

    # int(): Converts a value to an integer.
    int_result = int("100")
    print(f"int('100'): {int_result}")

    # float(): Converts a value to a float.
    float_result = float("3.5")
    print(f"float('3.5'): {float_result}")

    # str(): Converts a value to a string.
    str_result = str(500)
    print(f"str(500): '{str_result}'")

    # max(): Returns the largest item in an iterable or the largest of two or more arguments.
    max_result = max(10, 20, 30)
    print(f"max(10, 20, 30): {max_result}")

    # min(): Returns the smallest item in an iterable or the smallest of two or more arguments.
    min_result = min(5, 2, 9)
    print(f"min(5, 2, 9): {min_result}")

    # sum(): Sums the items of an iterable.
    sum_result = sum([1, 2, 3, 4])
    print(f"sum([1, 2, 3, 4]): {sum_result}")

    # sorted(): Returns a new sorted list from the items in an iterable.
    sorted_result = sorted([4, 1, 3, 2])
    print(f"sorted([4, 1, 3, 2]): {sorted_result}")

if __name__ == "__main__":
    demonstrate_builtin_functions()

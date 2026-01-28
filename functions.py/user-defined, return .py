# What is a User-Defined Function?
# A function created by the programmer using the def keyword.
# It can take inputs, perform operations, and return outputs.

def add(a: int, b: int) -> int:
    """Return sum of two integers."""
    return a + b

def subtract(a: int, b: int) -> int:
    """Return difference of two integers."""
    return a - b

def multiply(a: int, b: int) -> int:
    """Return product of two integers."""
    return a * b

def divide(a: float, b: float) -> float:
    """Return division result with validation. Raises ValueError on division by zero."""
    if b == 0:
        raise ValueError("Division by zero is not allowed")
    return a / b

def square(n: int) -> int:
    """Return square of a number."""
    return n * n

def cube(n: int) -> int:
    """Return cube of a number."""
    return n ** 3

def is_even(n: int) -> bool:
    """Check if a number is even."""
    return n % 2 == 0

def area_circle(radius: float) -> float:
    """Calculate area of a circle."""
    # Note: For more precision, use math.pi
    return 3.14 * radius * radius

def greet(name: str) -> str:
    """Return a greeting message."""
    return f"Hello, {name}!"

def main():
    """Demonstrates the use of various user-defined functions."""
    print("--- Demonstrating User-Defined Functions ---")

    a = 20
    b = 10
    n = 10

    print(f"{a} + {b} = {add(a, b)}")
    print(f"{a} - {b} = {subtract(a, b)}")
    print(f"{a} * {b} = {multiply(a, b)}")

    try:
        print(f"{a} / {b} = {divide(a, b)}")
        print(f"{a} / 0 = ...")
        print(divide(a, 0))
    except ValueError as e:
        print(f"Error during division: {e}")

    print(f"Square of {n} is {square(n)}")
    print(f"Cube of {n} is {cube(n)}")
    print(f"Is {n} even? {is_even(n)}")

    radius = 5
    print(f"Area of a circle with radius {radius} is {area_circle(radius)}")

    print(greet("Jeet"))

if __name__ == "__main__":
    main()

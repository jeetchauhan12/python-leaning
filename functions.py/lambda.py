# What is a Lambda Function?
#One-line function.
#No name.
#Used for short logic.
#Written using lambda.

# Example of Lambda Functions

a = 10
b = 50
c = 15
x = 12
s = " Hello How R You "

square = lambda x: x * x
print('Square:', square(x))

add = lambda a, b: a + b
print('Add:', add(a,b))

subtract = lambda a, b: a - b
print('Subtract:', subtract(a,b))


even = lambda n: n % 2 == 0
print('Is Even:', even(a))


max_val = lambda a, b: a if a > b else b
print('Max Value:', max_val(a,b))


cube = lambda x: x ** 3
print('Cube:', cube(x))


length = lambda s: len(s)
print('Length:', length(s))


uppercase = lambda s: s.upper()
print('uppercase:', uppercase(s))


multiply = lambda a, b, c: a * b * c
print('Multiply:', multiply(a,b,c))


check_age = lambda age: "Adult" if age >= 18 else "Minor"
print('Check Age:', check_age(19))


area_circle = lambda r: 3.14 * r * r
print ('Area of Circle:', area_circle(5))



























#  Identity operators are used to check whether two variables refer to the same object in memory, not whether their values are equal.
#  | Operator | Meaning                                                         |
#| --------    | --------------------------------------------------------------- |
#| `is`        | Returns `True` if both variables refer to the **same object**   |
#| `is not`    | Returns `True` if both variables refer to **different objects** |
#  IF IS OPERATOR :- The is operator checks memory identity (same object reference).
a = (10, 20)
b = a

print(a is b)

x = [1, 2, 3]
y = [1, 2, 3]

print(x is y)

#  IS-NOT Operator

p = {"name": "Alex"}
q = {"name": "Alex"}

print(p is not q)

m = [100, 200]
n = m

print(m is not n)


# Important Difference: == vs is

a = [5, 6]
b = [5, 6]

print(a == b)
print(a is b)
















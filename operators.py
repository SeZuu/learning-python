# Operators in python

a = 5
b = 3

# Arithmetic Operations
addition = a + b      # 8
diff = a - b          # 2
product = a * b       # 16
division = a / b      # 1.6
floor_division = a//b # 1 -> se aproxima al entero mas cercano
mod = a % b           # 2
exponential = a ** b  # 125 (a^b)

# + sirve para concatenar cadenas de texto
print("this is a diff: " + str(diff))

# * n sirve tambien para imprimir un string la cantidad definida
print("Five " * 5)

# Comparison Operators
# -> these operations will always return a boolean value
print(3 > 2)    # True
print(3 < 2)    # False
print(3 >= 2)   # True, because one of them is true
print(3 <= 2)   # False, because none of them are true
print(3 == 2)   # False
print(3 != 2)   # True

#example
print(len("something") == len("txt"))   # False, (9 == 3)?
print(len("hello") == len("hola!"))     # True,  (5 == 5)?

"""
is: returns true if both variables are the same object(x is y)
is not: returns true if both variables are not the same object(x is not y)
in: returns True if the queried list contains a certain item(x in y)
not in: returns True if the queried list doesn't have a certain item(x in y)
"""
print(1 is 1)           # True -> data is the same
print(1 is not 1)       # False
print("A" in "ABC")     # True
print("D" not in "ABC") # True

# Logical Operators
print(3 > 1 and 5 > 3)  # True -> and: ambas tienen que cumplir (&&)
print(3 > 1 or 4 > 1)   # True -> or: basta con que una cumpla  (||)

print(5 > 4)            # True
print(not(5 > 4))       # False -> not(true) = false (!(bool))
print(not(not(False)))  # False
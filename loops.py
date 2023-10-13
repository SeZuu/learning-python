# Loops

condition = True
value = 0

# while loop
while condition:
    print("message")
    value += 1
    if value == 5:
        condition = False

value = 0

while value < 5:
    print("message")
    value += 1

# break and continue in (while func)

condition = True
value = 0

while condition:
    print("something")
    value += 1
    if value == 5:  # si value es 5 rompe el while
        break

value = 0

while value < 11:
    value += 1
    if value == 10: # si value es 10 no imprime 10, vuelve al inicio
        continue    # del bucle
    print(value)

# for loop

"""
en python, " for iterator in lst: " sirve para recorrer una lista,
tupla, set, dictionary o string. Cada elemento que contengan estos
cuenta como una iteracion
"""

string = "Python"

for i in string:
    print(i)

lst = ["hello", "python", "again"]

for iterator in lst:
    print(iterator)

tpl = ("value", "value2", "value3")

for iterator in tpl:
    print(iterator)

st = {"0", "1", "2", "3", "4", "5"}

for iterator in st:
    print(iterator)

dct = {"key1":"value1", "key2":"value2", "key3":"value3"}

for iterator in dct:
    print(iterator)

for iterator in dct.values():
    print(iterator)

for i in range(3):
    print("hello")

# break and continue in (for func)

numbers = [0, 1, 2, 3, 4, 5]
for number in numbers:
    print(number)
    if number == 3:
        break
## note: imprime hasta 3 porque cumple con la condicion para romper
##       el bucle

for number in numbers:
    if (number == 3):
        continue
    print(number)
## note: imprime hasta 3 porque cumple con la condicion para romper
##       el bucle

# range function

lst = list(range(11))
print(lst) # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10] -> starts at 0

lst = list(range(1, 11)) # 2 arg = start - end - step-> set to default 1
print(lst)

lst = list(range(0, 11, 2)) # 3 arg = start - end - step
print(lst) # [0, 2, 4, 6, 8, 10]

# range in for
# syntax -> for iterator in range(start, end, step):

for number in range(11):
    print(number, end = " ") # 0 1 2 3 4 5 6 7 8 9 10

print() # new line

for number in range(0, 12, 2):
    print(number, end = " ") # 0 2 4 6 8 10

print() # new line

# nested for loop
for i in range(0, 10, 1):
    for j in range(0, 10, 1):
        print("*", end = " ")
    print("*")

person = {
    "name": "gabriel",
    "surname": "zuni",
    "age": "20",
    "learning": ["python", "git"],
    "city": "lima"
}

for i in person:
    if i == "learning":
        for j in person["learning"]:
            print(j)
        continue
    print(person[i])

# for else
for number in range(11): # prints 0 to 10, not including 11
    print(number)
else: # message para cuando sale del loop
    print("the loop stops at", number)

# pass 
"""
in python when a statement is required, but we don't like to execute
any code there, we can write the word pass to avoid errors
"""

for number in range(11):
    pass

# triangle

for i in range(10):
    for j in range(i):
        print("*", end = " ")
    print("*")
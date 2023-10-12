# Conditionals

value = True

# if
if value:
    print("value is true")

# if else

value = False

if value:
    print("value is true")
else:
    print("value is false")

# if, elif, else

value = 10

if value < 10:
    print("my value < 10")
elif value == 10:
    print("my value is 10")
else:
    print("my value is > 10")

# short hand -> code "if" condition "else" code

value = 5
print("value is 5") if value == 5 else print("value is not 5")

# nested conditions

if value < 10:
    if value == 5:
        print("the value meets both conditions :D")
    else:
        print("the value does not meet the second condition")
else:
    print("value does not meet the condition")

# conditional with logical operators

value = 5

if value > 1 and value < 10: # debe cumplir ambas condiciones
    print("hello")
else:
    print("python")

if value > 1 or value < 4:   # solo necesita complir una
    print(":D")
else:
    print(":C")
# Strings in Python

# declaration
character = "a"        # en python no hay char, es solo un string
my_string = 'sentence' # es indiferente el uso de "" o ''

# multiline string
multiline_string = """this is a multiline
string, declared as a multi-line
comment."""

# concatenation in string
name = "gabriel"
surname = "zuni"
age = 20
personal_data = name + surname + str(age) # output: gabrielzuni20

# scape sequences
'''
\n -> new line
\t -> tab (8 spaces)
\\ -> back slash
\' -> single quote
\" -> double quote
'''
print("Todo esta bien por aqui.\nQue tal por alli?") # salto de linea
print("centena\tdecena\tunidad") # tab
print("100\t10\t1")
print("200\t20\t2")
print("300\t30\t3")
print("simbolo back slash (\\)")

# formatting
'''
%s -> string
%d -> int
%f -> float
%.n..f -> numero de digitos especifico para el float
'''
day = 7
month = "October"
formated_str = "Today is %d of %s" %(day, month)
print(formated_str)

# new formatting style -> .format()
# print('{} / {} = {:.2f}'.format(a, b, a / b)) # limits it to two digits after decimal
new_formated_str = "Today is {} of {}".format(day, month)
print(new_formated_str)

a = 3
b = 5
print("{} + {} = {}".format(a, b, a + b))

# string interpolation -> f-string
print(f"{a} + {b} = {a + b}")
print(f"today is {day} of {month}")

# unpacking char's
message = "Python"
a, b, c, d, e, f = message # debe tener una variable para cada letra
print(a + c + e)
print(message[0] + message[2] + message[4])

# slicing strings
print(message[0:2]) # empieza en el index 0 hasta el 2 pero no incluye el 2

# reverse
message_reverse = message[::-1]
print(message_reverse)

# string methods
print(message.capitalize())     # vuelve mayuscula la primera letra
print(message.count("y"))       # cuenta cuantos hay
print(message.endswith("on"))   # verifica si termina con ..
print(message.startswith("Py")) # verifica si empieza con ..

#message = "lenguage\tPython"

print(message.expandtabs(20))  # cambia el valor del tab
print(message.find("y"))       # devuelve el index del primer valor, si no devuelve -1
print(message.rfind("n"))      # devuelve el index del ultimo valor, si no devuelve -1
print(message.upper())         # vuelve todo mayuscula
print(message.lower())         # vuelve todo minuscula
print(message.isupper())       # verifica si todo esta en mayuscula
print(message.upper().isupper())
print(message.islower())       # verifica si todo esta en minuscula
print(message.lower().islower())
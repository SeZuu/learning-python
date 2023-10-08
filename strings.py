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

# new formatting style .format()
# print('{} / {} = {:.2f}'.format(a, b, a / b)) # limits it to two digits after decimal
new_formated_str = "Today is {} of {}".format(day, month)
print(new_formated_str)

a = 3
b = 5
print("{} + {} = {}".format(a, b, a + b))

# string interpolation -> f-string
print(f"{a} + {b} = {a + b}")
print(f"today is {day} of {month}")
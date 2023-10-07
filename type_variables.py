"""
no es necesario indicar el tipo de dato al declarar una variable
pero es indispensable asginarle un valor
"""

# numeric data type
int_var = 5
long_var = 5555555 #.....
float_var = 1.5
complex_var = 1 + 3j

# boolean data type
check = True
approved = False

# string data type (u can use " or ')
string_var = "something"

# list data type -> funciona como un array en c++, pero puede tener diferentes tipos de datos a la vez 
int_list = [ 1, 2, 3, 4, 5 ]
string_list = [ "hello", "python", "again" ]
combination_list = [ 1, "two", 3 ]
print(string_list[1]) # para imprimir un elemento por su indice

# declaring multiple variable in a line, tambien se puede declarar mas de una variable en una linea
first_name, studying, age = "gabriel", True, 20 

# input() -> sirve para asignarle el valor manualmente via "consola"
message = input("write a message: ")
print(message)

# type() permite ver el tipo de dato
print(type(int_var))     # type -> int
print(type(long_var))    # type -> long
print(type(float_var))   # type -> float
print(type(complex_var)) # type -> complex

# print() puede tener varios argumentos concatenados con ' , ' (coma)
print(int_var, long_var, float_var, complex_var)

# len() retorna la longitud de un objeto, solo toma un argumento
print(len(string_var))

# casting -> es posible cambiar el tipo de dato a otro, utilizando las funciones por su nombre.. int() float()....
num_int = 10
print("int:", num_int)       # 10
num_float = float(num_int)
print("float:", num_float)   # 10.0
num_string = str(num_float)
print("string:", num_string) # "10"

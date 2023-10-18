### EXCEPTIONS ###

value, value2 = 1, 4
#value2 = "number"

# try, exception
try:
    print(value + value2) # if both of them are int the console shows 5
except:
    print("an error has ocurred") # else the console displayed the error message

# try, exception, else 
try:
    print(value + value2)
except:
    print("error")
else:
    print("this message is displayed when there is no error")

# try, except, else, finally
try:
    print("Hello")
except:
    print("No hello")
else:
    print("the hello message works")
finally:
    print("always display this message")

# capturar un error -> imprime el error sin romper el programa
try:
    print(1 + "text")
except Exception as error:
    print(error)

try:
    print(1 + "text")
except TypeError: # corre esta linea si el error es un TypeError
    print("Error en el tipo de dato") 
except ValueError: # corre esta linea si el error es un ValueError
    print("Error en los valores definidos")
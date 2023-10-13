### Functions ###

# syntax -> declaring a function
def function():
    pass

# calling a function
function()

# examples
def print_triangle():
    for i in range(10):
        for j in range(i):
            print("*", end = " ")
        print("*")

print_triangle() # triangle

def add_two_numbers():
    n1, n2 = 3, 2
    print(n1 + n2)

add_two_numbers() # 5

# function returning a value
def add_two_numbers_with_return():
    n1, n2 = 3, 2
    return n1 + n2

print(add_two_numbers_with_return()) # 5

# funtion with parameters
def greetings(name):
    return name + ", Welcome to Python"

print(greetings("Gabriel"))

def add_two_numbers_with_parameters(n1, n2):
    return n1 + n2

print(add_two_numbers_with_parameters(3, 2))

# passing arguments with key and value
def add_three_numbers(n1, n2, n3):
    return n1 + n2 + n3

add_three_numbers(n2 = 5, n1 = 4, n3 = 1) # order does not matter

# functions can return any data type, for example: lists
def find_even_numbers(n):
    evens = list()
    for i in range(1, n + 1):
        if i % 2 == 0:
            evens.append(i)
    return evens

print(find_even_numbers(10))

# function with default parameters
def greetings_function(name = "gabriel"):
    return name + ", welcome to python"

print(greetings_function())            # gabriel, welcome...
print(greetings_function("Sebastian")) # sebastian, welcome...

# arbitrary number of arguments
def sum_all_nums(*nums): # es como el *rest
    total = 0
    for i in nums:
        total += i
    return total

print(sum_all_nums(1, 4, 5)) # 10

def hello_leader_and_members(leader, *members):
    message = f"Hello, {leader} and"
    for i in members:
        message += f" {i},"
    message += " I hope you are ok"
    return message

print(hello_leader_and_members("Jose", "Pablo", "Lautaro", "Julio"))
# Hello, Jose and Pablo, Lautaro, Julio, I hope you are ok

# function as a parameter of another function
def square_number(n):
    return n * n

def do_something(func, arg):
    return func(arg)

print(do_something(square_number, 3)) # 9
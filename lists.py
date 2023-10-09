# Lists in Python

# syntax (declaration)
lst = list()
lst = []

empty_list = []   # lista vacia
print(empty_list) # 0

# lists examples
muscle_cars = ["camaro", "mustang", "challenger", "charger"]
numbers = [1, 2, 3, 4, 5]

print(len(muscle_cars)) # 4
print(len(numbers))     # 5

# lists are muly-type
lst = ["text", 5, 1.2, True]

# accesing by index
brands = ["Samsung", "Apple", "Xiaomi", "Huawei"]

print(brands[0]) # Samsung
print(brands[3]) # Huawei

# we can also access from the end, -1 refers to the las item, -2 the second last item ...
print(brands[-1]) # Huawei
print(brands[-4]) # Samsung

# unpacking a list
a, b, *c = brands
print(a) # Samsung
print(b) # Apple
print(c) # Xiaomi, Huawei -> contains the rest

# modifying lists
brands[0] = "LG"  # replace by index, and samsung is eliminated
print(brands)
brands[2] = "ZTE" # Xiaomi is eliminated
print(brands)

# checking items in a list
print("LG" in brands)     # True
print("Vision" in brands) # False

# adding items
brands.append("Poco")
print(brands) # ['LG', 'Apple', 'ZTE', 'Huawei', 'Poco']
brands.append("Honor")
print(brands) # ['LG', 'Apple', 'ZTE', 'Huawei', 'Poco', 'Honor']

# inserting items
lst = ["item 1", "item 2"]
lst.insert(0, "item 0") # syntax -> list.insert(index, item)
print(lst)
lst.insert(1, "item 1")
print(lst)              # ['item 0', 'item 1', 'item 1', 'item 2']

# removing items
lst.remove("item 1")
print(lst) # ['item 0', 'item 1.0', 'item 2'] -> elimina la primera concurrencia left to right

# list.pop() -> elimina objetos pero tambien retorna el objeto eliminado
lst.pop()  # elimina el ultimo elemento
lst.pop(0) # elimina por indice

print(lst) # ['item 1']

# del list[index] -> delete 1 item by index
# del list        -> delete the list

lst = [1, 2, 3]
del lst[0]
print(lst) # [2, 3]
del lst
#print(lst) -> shows error : lst is not defined

# clearing items
lst = ["apple", "orange", "grapes"]
lst.clear()
print(lst) # []

# copying a list
lst = [1, 2, 3, 4]
copy_list = lst.copy()
print(copy_list) # [1, 2, 3, 4]

# concatenating
list1 = [-3, -2, -1]
list2 = [0]
list3 = [1, 2, 3]
complete_list = list1 + list2 + list3 # doesn't works only with number or strings
print(complete_list)

# extend()
lst1 = [1, 2, 3]
lst2 = [4, 5]
lst1.extend(lst2)
print(lst1) # [1, 2, 3, 4, 5]

# counting items
lst = [1, 2, 3, 3, 4]
print(lst.count(3)) # 2 -> cuantos 3 encontro

# finding index of an item
lst = ["hello", "python", "lists"]
print(lst.index("hello")) # 0
print(lst.index("lists")) # 2

# reversing a list
lst = ["hello", "python", "lists", "again"]
lst.reverse()
print(lst) # ['again', 'lists', 'python', 'hello']

# Sorting list items
# sort() -> ordena la lista y sobrescribe la misma
lst.sort()               # ascending in alphabetical order

print(lst) # ['again', 'hello', 'lists', 'python']

lst.sort(reverse = True) # descengind in alphabetical order

print(lst) # ['python', 'lists', 'hello', 'again']

# sorted() -> ordena la lista pero no se guarda
lst = ["c", "a", "b"]
print(sorted(lst)) # ['a', 'b', 'c']
print(lst)         # ['c', 'a', 'b']
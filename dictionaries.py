# Dictionaries -> collection of unordered, mutable, paired data type

# syntax
dct = {}
dct = {"key1": "value1", "key2": "value2", "key3": "value3"}

# example
person = {
    "name": "Gabriel",
    "surname": "Zuni",
    "age": 20,
    "learning": ["python", "git"],
    "address": {
        "street": "street fighter",
        "zipcode": "010101"  # no ( , ) at the final
    }
}

""" 
note: el diccionario de arriba demuestra que puede contener cualquier
      tipo de dato: string, int, bool, list, tuple set or dictionary
"""

print(len(person)) # 5
print(len(person["address"])) # 2
print(len(dct))    # 3

# accesing items
print(dct["key1"]) # value1
print(dct["key3"]) # value3

print(person["name"])               # Gabriel
print(person["age"])                # 20
print(person["learning"])           # ['python', 'git']
print(person["learning"][0])        # pyton
print(person["address"]["zipcode"]) # 010101
#print(person["country"])           # Error

"""
si accedemos a un item por "keyname" y no existe, lanza error
para evitar esto, primero tenemos que checar si esta "keyname" existe
o podemos utilizar el metodo get()... retornara none si no existe
"""

print(person.get("name"))    # Gabriel
print(person.get("age"))     # 20
print(person.get("country")) # None

# adding items
dct = {"key1": "value1", "key2": "value2", "key3": "value3"}
dct["key4"] = "value4"
print(dct) # {'key1': 'value1', 'key2': 'value2', 'key3': 'value3', 'key4': 'value4'}

new_person = {
    "name": "gabriel",
    "surname": "zuni",
    "learning": ["python", "git"]
}
new_person["age"] = 20
new_person["learning"].append("c++") # because is a list
print(new_person) # {'name': 'gabriel', 'surname': 'zuni', 'age': 20}

# modifying items
dct["key1"] = "modified_value_1"
print(dct)
new_person["age"] = 200
print(new_person)

# checking keys
print("key2" in dct) # True
print("key5" in dct) # False

# removing key and value pairs
dct = {"key1": "value1", "key2": "value2", "key3": "value3", "key4": "value4"}
dct.pop("key1") # removes key1
print(dct)      # {'key2': 'value2', 'key3': 'value3', 'key4': 'value4'}

dct.popitem()   # removes the last item
print(dct)      # {'key2': 'value2', 'key3': 'value3'}

del dct["key2"] # removes key2
print(dct)      # {'key3': 'value3'}

# changing to a list of items
dct = {"key1": "value1", "key2": "value2", "key3": "value3"}
print(dct.items()) # dict_items([('key1', 'value1'), ('key2', 'value2'), ('key3', 'value3')])
"""
items() method changes dictionary to a list of tuples
"""

# clearing
print(dct.clear()) # None
print(dct)         # {}

# deleting
dct = {"key1": "value1", "key2": "value2", "key3": "value3"}
del dct

# copy a dictionary
dct = {"key1": "value1", "key2": "value2", "key3": "value3"}
dct_copy = dct.copy()
print(dct_copy) # {'key1': 'value1', 'key2': 'value2', 'key3': 'value3'}

# getting dictionary values as a list
values = dct.values()
print(values)
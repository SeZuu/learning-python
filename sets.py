# Sets

# syntax
st = set()
st = {}         # si se declara asi
print(type(st)) # incialmente es un dict

st = {"item1", "item2", "item3"} # al agregar items es un set
print(type(st))

# checking an item
print("item1" in st) # True
print("item4" in st) # False

# adding items
st.add("item4") # .add() solo puede agregar un item
print(st) # {'item1', 'item4', 'item2', 'item3'}

st.update(["item5", "item6", "item7"]) # .update() puede agregar varios items
print(st) # {'item3', 'item2', 'item5', 'item4', 'item6', 'item7', 'item1'}

## note: podemos ver que sets son estructuras de datos no ordenadas

st.add("item1")
print(st) # {'item6', 'item2', 'item3', 'item1', 'item7', 'item4', 'item5'}

## note: un set no admite repetidos

# removing items
st = {"item1", "item2", "item3"}
st.remove("item2")
print(st)

st.pop() # elimina un item random

# clearing items in a set
st.clear() 
print(st) # set()

# deleting a set
st = {"item1", "item2", "item3"}
del st
## print(st) name 'st' is not defined

## print(st[0]) 'set' object is not subscriptable, no podemos acceder por index

# set to list
st = {"item1", "item2", "item3"}
lst = list(st)
print(lst[0]) # item2 -> ahora si puedo acceder por posicion

# joining sets
st = {"samsung", "huawei", "lg"}
st2 = {"redmi", "oppo"}
st3 = st.union(st2) # es necesario asignarlo a una variables porque .union() retorna un set
print(st3)

# finding intersection
st1 = {"C++", "C#", "C"}
st2 = {"C#", "Java", "Javascript"}
print(st1.intersection(st2)) # {'C#'} -> encuentra las coincidencias

# subset and superset
smarthome = {"s", "m", "a", "r", "t", "h", "o", "m", "e"}
home = {"h", "o", "m", "e"}
print(smarthome.issubset(home))   # False
print(smarthome.issuperset(home)) # True

print(home.issubset(smarthome))   # True
print(home.issuperset(smarthome)) # False

# difference between two sets
smarthome = {"s", "m", "a", "r", "t", "h", "o", "m", "e"}
home = {"h", "o", "m", "e"}
print(smarthome.difference(home)) # {'a', 's', 't', 'r'}
print(home.difference(smarthome)) # set() -> because is a subset of smarthome

# joining sets -> si dos sets no tienen items en comun podemos llamarlos "disjoint sets"
web = {"javascript", "php"}
desktop = {"c#", "java"}
desktop_two = {"c#", "c++"}
print(web.isdisjoint(desktop))         # True
print(desktop.isdisjoint(desktop_two)) # False -> porque c# se repite
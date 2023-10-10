# Tuples
# A tuple is a collection of different data types which is ordered and unchangeable (immutable).

# declaration
tpl = tuple()
tpl = ()
tpl = ("this", "is", "a", "tuple")

# accessing tuple

value1 = tpl[0]
value2 = tpl[1]
value3 = tpl[-1] # last item

# slicing

all_items = tpl[0:3]
this_is = tpl[0:2]
a_touple = tpl[2:4]
print(this_is)
print(a_touple)

# changing tuple to list -> if we do this, we can change the data
changeable_tuple = list(tpl)
print(type(changeable_tuple))   # <class 'list'>
changeable_tuple[0] = "What"    # ['What', 'is', 'a', 'tuple']
print(changeable_tuple)
tpl = tuple(changeable_tuple)
print(type(tpl))                # <class 'tuple'>

# checking an item in a tuple
tpl = ('item1', 'item2', 'item3','item4')
print('item2' in tpl) # True

# joining tuples
tpl = ("item1", "item2")
tpl2 = ("item3", "item4")
tpl3 = tpl + tpl2
print(tpl3) # ('item1', 'item2', 'item3', 'item4')

# deleting tuples
tpl = (10, 11, 12)
# del tpl[0] 'tuple' object doesn't support item deletion
# but we can delete the entire tuple
del tpl
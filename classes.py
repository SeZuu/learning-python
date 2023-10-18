### CLASSES ###

class Person:   # clase siempre con PascalCase   
    def __init__(self, name): # constructor __init__, con atributo self que es el mismo
        print(f"Soy una persona y me llamo {name}")
    
# creando una instancia u objeto
persona = Person("Gabriel")
persona = Person("Javier")

# asignando parametros en el constructor
class Persona:
    def __init__(self, name, surname, age, fav_color):
        self.name = name
        self.surname = surname
        self.age = age
        self.fav_color = fav_color

p = Persona("Gabriel", "Zuni", 20, "violet")

# accediendo a los atributos de la instancia
print(p.name, end=" ")
print(p.surname)
print(p.age)
print(p.fav_color)

# metodos del objeto
class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def dog_info(self):
        return f"the dog name is {self.name} and he/she have {self.age} years old"
    
dog = Dog("Terry", 4)
print(dog.dog_info())
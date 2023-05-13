"""

"""

class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def saludar(self):
        print(f"Hola, mi nombre es {self.nombre} y tengo {self.edad} años.")


class Perro:
    def __init__(self, nombre, raza):
        self.nombre = nombre
        self.raza = raza

    def ladrar(self):
        print(f"{self.nombre}, el {self.raza}, está ladrando.")


# Creación de objetos
persona1 = Persona("Juan", 30)
perro1 = Perro("Bobby", "Labrador")

# Acceso a los atributos y métodos de los objetos
persona1.saludar()
perro1.ladrar()

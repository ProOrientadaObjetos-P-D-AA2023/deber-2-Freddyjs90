"""

"""
# Crear dos objetos de la clase 02

# objeto 01

# crear

# Presentar objeto; usar el método __st__

# objeto 02

# crear ingresando valores por teclado

# Presentar objeto; usar el método __st__


class Objeto:
    def __init__(self, atributo1, atributo2):
        self.atributo1 = atributo1
        self.atributo2 = atributo2

    def __str__(self):
        return f"Atributo 1: {self.atributo1}, Atributo 2: {self.atributo2}"


# Creación del objeto 1
objeto1 = Objeto("Valor 1", "Valor 2")

# Presentación del objeto 1
print(objeto1)

# Creación del objeto 2 ingresando valores por teclado
atributo1 = input("Ingrese el valor para el Atributo 1: ")
atributo2 = input("Ingrese el valor para el Atributo 2: ")
objeto2 = Objeto(atributo1, atributo2)

# Presentación del objeto 2
print(objeto2)



class Animal:
    def __init__(self, nombre):
        self.nombre = nombre

    def hacer_ruido(self):
        return "Algun ruido"

class Perro(Animal):
    def hacer_ruido(self):
        return "miau"

class Gato(Animal):
    def hacer_ruido(self):
        return "Guau"

mi_perro = Perro("Tobby")
mi_gato = Gato("Michi")

print(mi_perro.hacer_ruido())
print(mi_gato.hacer_ruido())

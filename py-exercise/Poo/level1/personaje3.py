
from traceback import print_tb


class Personaje:
    def __init__(self, nombre, vida, energia, velocidad, inteligencia):
        self.nombre = nombre
        self.vida = vida
        self.energia = energia
        self.velociadad = velocidad
        self.inteligencia = inteligencia

    def mostrar(self):
        print(self.nombre)
        print(self.vida)
        print(self.energia)
        print(self.velociadad)
        print(self.inteligencia)

    def subir_nivel(self, energia):
        self.energia = self.energia + energia

    def esta_vivo(self):
        return self.vida > 0

    def morir(self, resistencia):
        self.vida = self.vida - resistencia

    # metodo que necesita crear un nuevo objeto(enemigo)
    # en base a su velocidad deberia quitar vida
    def dano(self, enemigo):
        return self.velociadad - enemigo.energia

    def atacar(self, enemigo):
        dano = self.dano(enemigo)
        enemigo.vida = enemigo.vida - dano
        print(f"{self.nombre} ha realizado dano al enenigo {enemigo.nombre}")


personaje1 = Personaje("Goku", 100, 80, 89, 70)
enemigo = Personaje("Vegeta", 100, 40, 60, 50)

personaje1.atacar(enemigo)
print(enemigo.mostrar())

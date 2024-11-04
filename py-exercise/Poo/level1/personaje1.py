class Personaje:
    def __init__(self, name, velocidad, fuerza,
                 inteligencia, defensa, vida):
        self.name = name
        self.velocidad = velocidad
        self.fuerza = fuerza
        self.inteligencia = inteligencia
        self.defensa = defensa
        self.vida = vida
    
    def mostrar(self):
        print(self.name)
        print(self.velocidad)
        print(self.fuerza)
        print(self.inteligencia)
        print(self.defensa)
        print(self.vida)

mi_personaje = Personaje("Goku", 78, 55, 43, 88, 100)
mi_personaje1 = Personaje("Vegeta", 70, 100, 60, 80, 100)
mi_personaje.mostrar()
mi_personaje1.mostrar()

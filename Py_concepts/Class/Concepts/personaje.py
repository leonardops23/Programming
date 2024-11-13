# CLASS
# CONTRUCTOR
# INICIALIZADOR
# METODO
# VARIABLE
# OBJETO

class Personaje:
    def __init__(self,
                nombre,
                fuerza,
                inteligencia,
                niveles,
                para_combate):

        self.nombre = nombre
        self.fuerza = fuerza
        self.inteligencia = inteligencia
        self.niveles = niveles
        self.para_combate = para_combate

    def atacar(self):
        print(f"EL personaje {self.nombre} ataca con una fuerza de {self.fuerza}")

class Enemigo(Personaje):
    def __init__(self, nombre, fuerza, inteligencia, 
                niveles, para_combate, ):
        super().__init__(nombre, fuerza,
                        inteligencia, niveles, para_combate)

character_name = input("Character name: ")
fuerza = input("Su fuerza: ")
inteligencia = input("Inteligencia: ")
niveles = input("Nivel del personaje: ")
disponible = input("Esta disponible: ")

personaje1 = Personaje(character_name, fuerza, inteligencia, niveles, disponible)

while True:
    try:
        if personaje1.para_combate == "True":
            personaje1.atacar()
            break
        else:
            quiere_pelear = input("Esta disponible: ")
            personaje1.para_combate = quiere_pelear
            if quiere_pelear == "True":
                print("El personaje esta listo para combate")
                personaje1.atacar()
                break
    except:
        print("El personaje no esta disponible")

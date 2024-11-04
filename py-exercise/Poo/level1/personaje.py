class Personaje:
    nombre = "Default"
    fuerza = 0
    inteligenci = 0
    defensa = 0
    vida = 0

    """
    Metodo constructor para que resivan los valores
    """

    def __init__(self, nombre, fuerza, inteligencia, defensa, vida) -> None:
        self.nombre = nombre
        self.fuerza = fuerza
        self.inteligencia = inteligencia
        self.defensa = defensa
        self.vida = vida


# Creando un objeto
mi_personaje = Personaje()
mi_personaje.defensa = 20
mi_personaje.inteligenci = 20
mi_personaje.nombre = 'Spartas'
print("El nombre del personaje es: ", mi_personaje.nombre)
print("El nombre del personaje es: ", mi_personaje.defensa)
print("El nombre del personaje es: ", mi_personaje.vida)

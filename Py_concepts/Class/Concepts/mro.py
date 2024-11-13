class Persona:
    def __init__(self, nombre, edad) -> None:
        self.nombre = nombre
        self.edad = edad

    def print_info(self):
        return f"Name: {self}\nEdad:  {self.edad}\n"


class Estudiante:
    pass

persona = Persona("Ivan", 23)
print(persona)

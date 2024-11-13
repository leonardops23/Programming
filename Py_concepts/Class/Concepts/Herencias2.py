class Transporte:
    def __init__(self, kilometros: int, tarifa: int) -> None:
        self.kilometros = kilometros
        self.tarifa = tarifa

    def calcular_tarifa(self):
        return self.tarifa

class Taxi(Transporte):
    def calcular_tarifa(self):
        return super().calcular_tarifa() * self.kilometros

class Autobus(Transporte):
    def calcular_tarifa(self) -> int:
        self.tarifa = 5
        return self.tarifa

class Bicicleta(Transporte):
    def calcular_tarifa(self):
        return "Gratis el uso de este Transporte"

taxi1 = Taxi(2, 4)
print(f"Se ha hecho el monto total de: ${taxi1.calcular_tarifa()}")

autobus = Autobus(2, 4)
print(f"Su monto es: ${autobus.calcular_tarifa()}")

bici = Bicicleta(2, 12)
print(bici.calcular_tarifa())
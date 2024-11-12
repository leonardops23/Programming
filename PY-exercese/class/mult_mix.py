class DescuentoMixin:
    def aplicar_descuento(self, precio, descuento):
        return precio * (1 - descuento)

class Vehiculo:
    def __init__(self, modelo):
        self.modelo = modelo

class Auto(DescuentoMixin, Vehiculo):
    def __init__(self, modelo):
        super().__init__(modelo)

    def precio_final(self, precio, descuento):
        return self.aplicar_descuento(precio, descuento)

mi_auto = Auto("Toyota")
print(mi_auto.precio_final(10000, 0.1))  # Aplica un 10% de descuento

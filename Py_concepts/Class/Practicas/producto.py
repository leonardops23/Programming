
"""
Clase producto que represente el producto con un precio y un
stock.
"""
class Producto:
    def __init__(self, precio: int, stock: int):
        self.__precio = precio
        self.__stock = stock

    @property
    def precio(self):
        return self.__precio

    @property
    def stock(self):
        return self.__stock

    @precio.setter
    def descuento(self, descuento: int, day: str):
        if descuento > 0:
            self.__precio = descuento

licuadora = Producto(23, 4)
print(licuadora.precio)
licuadora.descuento = 12

print(licuadora.precio)

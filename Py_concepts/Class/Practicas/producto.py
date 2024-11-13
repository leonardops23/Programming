class Producto:
    def __init__(self, nombre, precio, stock):
        self.nombre = nombre
        self.__precio = precio  # Atributo privado
        self.__stock = stock    # Atributo privado

    # Getter para el precio
    @property
    def precio(self):
        return self.__precio

    # Setter para el precio
    @precio.setter
    def precio(self, nuevo_precio):
        if nuevo_precio > 0:
            self.__precio = nuevo_precio
        else:
            raise ValueError("El precio debe ser mayor que 0")

    # Getter para el stock
    @property
    def stock(self):
        return self.__stock

    # Setter para el stock
    @stock.setter
    def stock(self, nuevo_stock):
        if nuevo_stock >= 0:
            self.__stock = nuevo_stock
        else:
            raise ValueError("El stock no puede ser negativo")

    # Método para vender una cantidad del producto
    def vender(self, cantidad):
        if cantidad <= self.__stock:
            self.__stock -= cantidad
            print(f"Se vendieron {cantidad} unidades de {self.nombre}. Stock restante: {self.__stock}")
        else:
            print(f"No hay suficiente stock para vender {cantidad} unidades de {self.nombre}. Stock actual: {self.__stock}")

# Uso de la clase Producto
producto = Producto("Camiseta", 25.0, 50)

# Acceder al precio y stock
print("Precio:", producto.precio)
print("Stock:", producto.stock)

# Modificar el precio y stock de forma controlada
producto.precio = 30.0  # Nuevo precio
producto.stock = 40     # Nuevo stock

print("Precio actualizado:", producto.precio)
print("Stock actualizado:", producto.stock)

# Intentar asignar un precio negativo (genera un error)
try:
    producto.precio = -10
except ValueError as e:
    print(e)

# Intentar asignar un stock negativo (genera un error)
try:
    producto.stock = -5
except ValueError as e:
    print(e)

# Vender unidades del producto
producto.vender(10)  # Vender 10 unidades
producto.vender(35)  # Intentar vender más unidades de las disponibles

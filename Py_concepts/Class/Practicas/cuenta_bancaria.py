"""
Bank Account
"""

class BankAccount:
    def __init__(self, titular: str, saldo_inicial=0):
        self.titular = titular
        self.__saldo_inicial = saldo_inicial

    @property
    def saldo(self):
        """Para obtener el saldo"""
        return self.__saldo_inicial

    @saldo.setter
    def saldo(self, monto):
        "Agregando un monto y actualizando el saldo"
        if monto < 0:
            raise ValueError("No se puede asignar valores negativos")
        self.__saldo_inicial = monto

    def depositar(self, cantidad):
        if cantidad > 0:
            self.__saldo_inicial += cantidad
            print(f"Se depositaron ${cantidad} a su cuenta")
            print(f"Su toal es de: ${self.saldo}")

    def retirar(self, cantidad_retirada):
        if cantidad_retirada < self.saldo:
            self.__saldo_inicial -= cantidad_retirada
            print(f"Se retiro ${cantidad_retirada} en su cuenta")
            print(f"El monto actualizado es: {self.saldo}")
        else:
            print("No tiene el monto suficiente para retirar")

user1 = BankAccount("Jose")
user1.saldo = 2
user1.depositar(30)
user1.retirar(2)



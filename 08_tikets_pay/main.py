import uuid
import time

"""
Este mini programa se trata de pagar el tiket recibiendo la informacion detalla
del servicio que ofrecemos

Una seccion de menu para que el usuario tenga la option de elegir

Los datos seran guardados en un archivo .json
id unico

tratare de hacer 

"""

class PayTikets:
    def __init__(self, id: int, name: str, value: float,
                time_now: int, go_out: int, dni: int):
        self.id = id
        self.name = name
        self.value = value
        self.time_now = time_now 
        self.go_out = go_out
        self.__dni = dni

    def __str__(self) -> str:
        return f"""
                Info:
                For: {self.name}
                Dni: {self.__dni}
                Recivido: {self.time_now}
                Hora de salida: {self.go_out}

                Total valor: {self.value}
                """

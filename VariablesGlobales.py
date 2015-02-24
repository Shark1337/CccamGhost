import random
from random import choice

class VariablesGlobales:
    """Clase que contiene las variables globales"""
    def __init__(self):
        self.RandomA = str(random.randrange(0,255))
        self.RandomB = str(random.randrange(0,255))
        self.valores = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
        self.longitud = 10
        self.PASS = ""
        self.PASS = self.PASS.join([choice(self.valores) for i in range(self.longitud)])
        self.RutaArchTemp = "temp"


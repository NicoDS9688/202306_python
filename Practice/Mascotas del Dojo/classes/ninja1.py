"""Ninja"""

class Ninja:
    """Clase Ninja"""
    def __init__(self, nombre, apellido, premios, comida_mascota, mascota)-> None:
        self.nombre = nombre
        self.apellido = apellido
        self.premios = premios
        self.comida_mascota = comida_mascota
        self.mascota = mascota

    def caminar(self):
        """Metodo para sacar a caminar a la mascota"""
        self.mascota.jugar()
        print(f"Paseando a {self.mascota.nombre}")
        return self

    def alimentar(self):
        """Metodo para alimentar a la mascota"""
        self.mascota.comer()
        print(f"Alimentando a {self.mascota.nombre}")
        return self

    def banhar(self):
        """Metodo para bañar a la mascota"""
        self.mascota.ruido()
        print(f"Limpiando a {self.mascota.nombre}")
        return self

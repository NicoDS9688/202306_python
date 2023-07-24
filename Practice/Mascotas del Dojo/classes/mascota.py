"""Mascota"""
class Mascota:
    """Clase Mascota"""
    def __init__(self, nombre, tipo, golosinas, sonido)-> None:
        self.nombre = nombre
        self.tipo = tipo
        self.golosinas = golosinas
        self.salud = 100
        self.energia = 100
        self.sonido = sonido

    def dormir(self):
        """Metodo para que la mascota duerma"""
        self.energia += 25
        return self

    def comer(self):
        """Metodo para que la mascota coma"""
        self.energia += 5
        self.salud += 10
        return self

    def jugar(self):
        """Metodo para que la mascota juegue"""
        self.salud += 5
        return self

    def ruido(self):
        """Metodo para que la mascota haga un sonido"""
        print(self.sonido)
        return self
    
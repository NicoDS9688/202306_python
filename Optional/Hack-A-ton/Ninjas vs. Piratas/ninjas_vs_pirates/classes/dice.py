"""Dado"""
import random

class Dice():
    """Clase que representa al dado"""
    def rolldice(self):
        """Metodo que realiza el lanzamiento del dado"""
        return random.randint(1, 6)

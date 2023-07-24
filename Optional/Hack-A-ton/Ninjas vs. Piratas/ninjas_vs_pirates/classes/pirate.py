"""Pirata"""
from classes.personaje import Personaje

class Pirate(Personaje):
    """Clase que representa al pirata"""
    def __init__(self , name):
        super().__init__(name)
        self.strength = 15
        self.speed = 3

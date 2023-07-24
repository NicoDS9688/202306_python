"""Ninja"""
from classes.personaje import Personaje

class Ninja(Personaje):
    """Clase que representa al ninja"""
    def __init__(self , name):
        super().__init__(name)
        self.strength = 10
        self.speed = 5

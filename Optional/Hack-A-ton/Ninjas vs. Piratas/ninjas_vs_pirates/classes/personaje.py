"""Personaje"""
from classes.dice import Dice
dice = Dice()

class Personaje:
    """Clase que representa al personaje"""
    def __init__(self , name):
        self.name = name
        self.strength = 15
        self.speed = 3
        self.health = 100

    def show_stats(self):
        """Metodo para mostrar los stats del personaje"""
        print(f"Name: {self.name}\nStrength: {self.strength}\nSpeed: {self.speed}\nHealth: {self.health}\n")

    def attack(self, objetivo):
        """Metodo para que el personaje ataque"""
        diceroll = dice.rolldice()
        if diceroll == 6:
            damage = self.strength * 2
            objetivo.health -= damage
            print('==================')
            print(f"Sacaste un {diceroll}")
            print(f"Ataque Crítico de {self.name} a {objetivo.name}.")
            print(f"Salud de {objetivo.name}: {objetivo.health}")
            print('==================')
        elif diceroll >= 3:
            damage = self.strength
            objetivo.health -= damage
            print('==================')
            print(f"Sacaste un {diceroll}")
            print(f"Ataque normal de {self.name} a {objetivo.name}.")
            print(f"Salud de {objetivo.name}: {objetivo.health}")
            print('==================')
        else:
            print('==================')
            print(f"Sacaste un {diceroll}")
            print(f"{self.name} falló su ataque.")
            print(f"Salud de {objetivo.name}: {objetivo.health}")
            print('==================')

def check_game_over(ninja, pirate):
    """Revisa si alguno de los personajes aun tiene salud"""
    if ninja.health <= 0:
        print(f"{ninja.name} ha sido derrotado. ¡{pirate.name} es el ganador!")
        return True
    elif pirate.health <= 0:
        print(f"{pirate.name} ha sido derrotado. ¡{ninja.name} es el ganador!")
        return True
    return False

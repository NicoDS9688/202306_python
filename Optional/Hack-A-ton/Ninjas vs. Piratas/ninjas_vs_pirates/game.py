"""Partida"""
from classes.ninja import Ninja
from classes.pirate import Pirate
from classes.personaje import Personaje
from classes.personaje import check_game_over

michelangelo = Ninja("Michelangelo")

jack_sparrow = Pirate("Jack Sparrow")

objetivo = Personaje("Objectivo")
jack_sparrow.show_stats()
michelangelo.show_stats()

michelangelo = Ninja("Michelangelo")
jack_sparrow = Pirate("Jack Sparrow")

turno = 0

while True:
    if turno % 2 == 0:
        ninja = michelangelo
        pirate = jack_sparrow
    else:
        ninja = jack_sparrow
        pirate = michelangelo

    print(f"Turno de {ninja.name}. Escribe 'lanzar' para lanzar el dado.")
    accion = input("Acción: ")

    if accion == "lanzar":
        ninja.attack(pirate)
        if check_game_over(ninja, pirate):
            break
    else:
        print("Acción inválida. Debes escribir 'lanzar' para lanzar el dado.")

    turno += 1

# 1. TAREA: imprime "Hola, mundo"
print("Hola, mundo".title())
# 2. imprime "Hola, Noelle" con el nombre en una variable
name = "Nico"
print("Hola", name)  # con una coma
print("Hola " + name)  # con un +
# 3. imprimir "Hola 42!" con el número en una variable
name = 8
print("Hola", name)  # con una coma
print("Hola " + str(name))  # con una +	-- este debería arrojar un error!
# 4. imprimir "Amo comer sushi y pizza" con las comidas en variables
fave_food1 = "pizza"
fave_food2 = "milanesas"
print("Amo comer {} y {}".format(fave_food1,
      fave_food2).swapcase())  # con .format()
print(f"Amo comer {fave_food1} y {fave_food2}".upper())  # con una cadena f

# 1.-Cuenta regresiva: crea una función que acepte un número como entrada. Devuelve una lista nueva que cuente de uno en uno, desde el número (como elemento 0) hasta 0 (como último elemento). 
#      Ejemplo: countdown(5) debería devolver [5,4,3,2,1,0]

num = 0
def countdown(num):
    return list(range(num, -1, -1))

countdown_numbers = countdown(num)
print(countdown(10))
print(countdown(5))
print(countdown(3))


# 2.- Imprimir y devolver: crea una función que reciba una lista con dos números. Imprime el primer valor y devuelve el segundo.
#        Ejemplo: imprimir_y_devolver([1,2]) debe imprimir 1 y devolver 2

def list_of_numbers(a, b):
    print(a)
    return b
print(list_of_numbers(5, 3))
print(list_of_numbers(2, 9))

# 3.- Primero más longitud: crea una función que acepte una lista y devuelva la suma del primer valor de la lista, más la longitud de la lista.
#        Ejemplo: primero_mas_longitud([1,2,3,4,5]) debe devolver 6 (primer valor: 1 +length: 5)

def add_lists(list):
    c = list[0]
    long = len(list)
    add = c + long
    return add
list1 = add_lists([10, 5, 7, 4])
print(list1)


# 4.-Valores mayores que el segundo: escribe una función que acepte una lista y cree una nueva que contenga solo los valores de la lista original que sean mayores que su segundo valor. Imprime cuántos valores son y luego devuelve la lista nueva. Si la lista tiene menos de 2 elementos, has que la función devuelva False
#       Ejemplo: valores_mayores_que_el_segundo([5,2,3,2,1,4]) debe imprimir 3 y devolver [5,3,4]
#       Ejemplo: valores_mayores_que_el_segundo([3]) debe devolver False

def create_list(list):
    if len(list) < 2:
        return False
    
    second = list[1]
    highest_values = []
    for value in list:
        if value > second:
            highest_values.append(value)
    
    newlist = len(highest_values)
    print(newlist)
    return highest_values

create_list([5,2,3,2,1,4])


# 5.-Esta longitud, ese valor: escribe una función que acepte dos enteros como parámetros: tamaño y valor. La función debe crear y devolver una lista cuya longitud sea igual al tamaño dado, y cuyos valores sean todos el valor dado.
#      Ejemplo: length_and_value(4,7) debe devolver [7,7,7,7]
#      Ejemplo: length_and_value(6,2) debe devolver [2,2,2,2,2,2]

def return_list(length, value):
    list = [value] * length
    return list
list1 = return_list(4,7)
print(list1)
list2 = return_list(6,2)
print(list2)
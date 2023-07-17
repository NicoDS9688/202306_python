
# 1.- Actualizar valores en diccionarios y listas

x = [ [5,2,3], [10,8,9] ]

b = x[1]
b[0] = 15
print(x)

print('--'*10)

estudiantes = [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'}
]

jugador1 = estudiantes[0]
jugador1['last_name'] = 'Bryant'
print(estudiantes)

print('--'*10)


directorio_deportes = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'fútbol' : ['Messi', 'Ronaldo', 'Rooney']
}

futbol = directorio_deportes['fútbol']
futbol[0] = 'Andres'
print(directorio_deportes)

print('--'*10)


z = [ {'x': 10, 'y': 20} ]

valores = z[0]
valores['y'] = 30
print(z)

print('<>'*10)



# 2.-Iterar a través de una lista de diccionarios
#    Crea una función iterateDictionary(some_list)para que, dada una lista de diccionarios,
#    la función recorra cada diccionarios de la lista e imprima cada llave y el valor asociado.

estudiantes = [
         {'first_name':  'Michael', 'last_name' : 'Jordan'},
         {'first_name' : 'John', 'last_name' : 'Rosales'},
         {'first_name' : 'Mark', 'last_name' : 'Guillen'},
         {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]

def iterateDictionary(some_list):
    for estudiante in some_list:
        for etiqueta, valor in estudiante.items():
            print(f"{etiqueta} - {valor}", end= " ")
        print()


iterateDictionary(estudiantes)


print('<>'*10)

# 3.- Obtener valores de una lista de diccionarios
#     Crea una función iterateDictionary2(key_name, some_list)que,
#     dada una lista de diccionarios y un nombre de clave,
#     la función imprima el valor almacenado en esa clave para cada diccionario.

def  iterateDictionary2(name, some_list):
    for diccionario in some_list:
        if name in diccionario:
            valor = diccionario[name]
            print(valor)

iterateDictionary2('first_name', estudiantes)
iterateDictionary2('last_name', estudiantes)

print('<>'*10)


# 4.- Iterar a través de un diccionarios con valores de lista
#     Crea una función printInfo(some_dict)que, dado un diccionario cuyos valores son todos listas,
#     imprima el nombre de cada clave junto con el tamaño de su lista,
#     y luego imprima los valores asociados dentro de la lista de cada clave.


dojo = {
   'ubicaciones': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
   'instructores': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}


instructores = dojo['instructores']

def printInfo(some_dict):
    ubicaciones = dojo['ubicaciones']
    cantidad1 = len(ubicaciones)
    print(f"{cantidad1}" + " UBICACIONES")
    for ubicacion in ubicaciones:
        print(ubicacion)

    print("--"*10)

    instructores = dojo['instructores']
    cantidad2 = len(instructores)
    print(f"{cantidad2}" + " INSTRUCTORES")
    for instructor in instructores:
        print(instructor)


printInfo(dojo)




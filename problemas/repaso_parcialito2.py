'''Todas las funciones desarrolladas deben tener su respectivo typehint y deben seguir buenas prácticas de progra- mación.
Ejercicio 1
Se tiene una lista que contiene diccionarios con las claves ?nombre?, ?mesa?, y ?especial?.
Sacados del archivo csv.'''

def csv_to_dict(archivo:str):
    ''' '''
    lista = []
    with open(archivo) as f:
        categorias = f.readline().strip().split()
        texto = f.readlines().strip().split('\n')
        for linea in texto:
            datos = linea.split(',')
            lista.append({categorias[0]:datos[0],
                          categorias[1]:datos[1],
                          categorias[2]:datos[2]})
    return lista


csv_to_dict('clientes.csv')

'''Un ejemplo de listas de este
tipo es el siguiente:
 [{"nombre": "Gabi", "mesa": 3, "especial": "si"},
 {"nombre": "Dani", "mesa": 1, "especial": "no"},
 {"nombre": "Aike", "mesa": 3, "especial": "si"},
 {"nombre": "Pato", "mesa": 1, "especial": "si"},
 {"nombre": "Indigo", "mesa": 1, "especial": "si"},
 {"nombre": "Sora", "mesa": 2, "especial": "si"},
 {"nombre": "Cris", "mesa": 2, "especial": "no"},
 {"nombre": "Matu", "mesa": 3, "especial": "no"},
 {"nombre": "Alex", "mesa": 1, "especial": "no"},
 {"nombre": "Xue", "mesa": 2, "especial": "no"},
 {"nombre": "Ariel", "mesa": 2, "especial": "no"}]
1. Implementar una función que tome una lista con este formato y la ordene por nombre . 
2. Implementar una función que tome una lista con este formato y la ordene por mesa .
No está permitido usar la función built-in sorted , ni el método sort de las listas, 
ni el algoritmo bubblesort.'''



'''Ejercicio 2
Dada una de las listas que se obtiene como resultado de aplicar una de las funciones 
desarrolladas en el punto anterior, implementar una función que dado un nombre nos indique 
qué mesa le corresponde. El peor caso de la función debe resolverse en un tiempo mejor que 
?(?), donde ? es la cantidad de elementos en la lista.
Justifique cuál de las funciones desarrolladas en el primer ejercicio convendría utilizar 
para ordenar la lista original.'''

'''Ejercicio 3
Considerando una de las listas del ejemplo, implementar una función recursiva que mediante la estrategia Divide &
Conquer nos devuelva cuántos diccionarios hay en los cuales ?si? es el valor asociado a la clave ?especial?.'''
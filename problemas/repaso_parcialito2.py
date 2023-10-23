'''Todas las funciones desarrolladas deben tener su respectivo typehint y deben seguir buenas prácticas de progra- mación.
Ejercicio 1
Se tiene una lista que contiene diccionarios con las claves ?nombre?, ?mesa?, y ?especial?.
Sacados del archivo csv.'''

def csv_to_dict(archivo:str)->list[dict]:
    ''' '''
    lista = []
    with open(archivo) as f:
        claves = f.readline().rstrip('\n').split(',')
        texto = f.readlines()
        for linea in texto:
            datos = linea.rstrip('\n').split(',')
            lista.append({claves[0]:datos[0].strip(),
                          claves[1]:int(datos[1].strip()),
                          claves[2]:datos[2].strip()})
    return lista


lista = csv_to_dict("problemas/clientes.csv")

'''Un ejemplo de listas de este
tipo es el siguiente:'''
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

'''1. Implementar una función que tome una lista con este formato y la ordene por nombre . 
2. Implementar una función que tome una lista con este formato y la ordene por mesa .
No está permitido usar la función built-in sorted , ni el método sort de las listas, 
ni el algoritmo bubblesort.'''

def orden_nombre(lista:list):
    '''     '''
    for i in range(len(lista)-1):
        minimo = i
        for j in range(i, len(lista)):
            if lista[minimo]["nombre"] > lista[j]["nombre"]:
                minimo = j
        lista[minimo],lista[i] = lista[i],lista[minimo]
    return lista
lista1 = orden_nombre(lista)

def orden_mesa(lista:list):
    '''     '''
    for i in range(len(lista)-1):
        minimo = i
        for j in range(i, len(lista)):
            if lista[minimo]["mesa"] > lista[j]["mesa"]:
                minimo = j
        lista[minimo],lista[i] = lista[i],lista[minimo]
    return lista
orden_mesa(lista)

'''Ejercicio 2
Dada una de las listas que se obtiene como resultado de aplicar una de las funciones 
desarrolladas en el punto anterior, implementar una función que dado un nombre nos indique 
qué mesa le corresponde. El peor caso de la función debe resolverse en un tiempo mejor que 
O(n), donde n es la cantidad de elementos en la lista.
Justifique cuál de las funciones desarrolladas en el primer ejercicio convendría utilizar 
para ordenar la lista original.'''

def mesa_nombre(lista:list,nombre:str)->int:
    medio = len(lista)//2
    while lista[medio]["nombre"] != nombre:
        if lista[medio]["nombre"]<nombre:
            medio = len(lista[:medio])//2
        else:
            medio = len(lista[medio:])//2
    return lista[medio]["mesa"]

print(mesa_nombre(lista1,"Cris"))

'''Ejercicio 3
Considerando una de las listas del ejemplo, implementar una función recursiva que mediante 
la estrategia Divide & Conquer nos devuelva cuántos diccionarios hay en los cuales 
?si? es el valor asociado a la clave ?especial?.'''
#%%
lista = [{"nombre": "Gabi", "mesa": 3, "especial": "si"},
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

def especial_si(lista):
    if len(lista)==1:
        if lista[0]["especial"]=="si":
            return 1
        else: return 0
    else:
        medio = len(lista)//2
        lista1,lista2 = lista[:medio],lista[medio:]
        return especial_si(lista2) + especial_si(lista1)
especial_si(lista)
# %%

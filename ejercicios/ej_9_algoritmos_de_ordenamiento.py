#%% 1 SELECCION
''' Implementar una función que tome una lista de números y la ordene de menor a mayor 
usando el algoritmo de selección.'''
def seleccion(lista:list):
    '''     '''
    for i in range(len(lista)-1):
        minimo = i
        for j in range(i,len(lista)):
            if lista[j]<lista[minimo]:
                minimo = j
            j = i
        lista[minimo],lista[i] = lista[i],lista[minimo]
    return lista
l = [3,5,2,1,4]
print(seleccion(l))
# %% 2 INSERCION
'''Implementar una función que tome una lista de números y la ordene de menor a mayor 
usando el algoritmo de inserción.'''
def insercion(lista):
    '''     '''
    for i in range(1,len(lista)):
        actual = lista[i]
        k = i
        while k>0 and lista[k-1]>actual:
            lista[k]=lista[k-1]
            k = k-1
        lista[k]=actual
    return lista
l = [3,5,2,1,4]
print(insercion(l))
# %% 3 BURBUJEO
''' Implementar una función que tome una lista de números y la ordene de menor a mayor 
usando el algoritmo de burbujeo.'''
def burbujeo(lista):
    for j in range(len(lista)-1):
        for k in range(1,len(lista)-j):
            if lista[k]<lista[k-1]:
                lista[k],lista[k-1]=lista[k-1],lista[k]
    return lista
l = [3,5,2,1,4]
print(burbujeo(l))           
# %% 4 y 5
'''Se tiene una lista que contiene diccionarios con las claves ?id?, ?descripcion?, ?costo? 
y ?stock?. Un ejemplo de listas de este tipo es el siguiente:'''

l=[{"id": 4, "descripcion": "Girgola", "costo": 449.0, "stock": 324},
{"id": 2, "descripcion": "Espinaca", "costo": 799.0, "stock": 3501},
{"id": 3, "descripcion": "Champignon", "costo": 629.0, "stock": 723},
{"id": 12, "descripcion": "Kiwi", "costo": 1299.0, "stock": 150},
{"id": 10, "descripcion": "Mandarina Okitsu", "costo": 389.0, "stock": 430},
{"id": 11, "descripcion": "Mandarina Nova", "costo": 389.0, "stock": 900}]

'''Implementar una función que tome una lista con este formato y la ordene por id.
Implementar una función que tome una lista con este formato y la ordene por costo.
No está permitido usar la función built-in sorted, ni el método sort de las listas.'''
'''Realice el ejercicio anterior pero usando los 
otros dos algoritmos de ordenamiento vistos en clase.'''
#INSERCION
def ordenar_costo_insercion(lista):
    '''     '''
    for j in range(1,len(lista)-1):
        actual = lista[j]
        k = j
        while k > 0 and (lista[k]["id"]<lista[k-1]["id"]):
            lista[k]=lista[k-1]
            k = k-1
        lista[k]=actual
    return lista
print(ordenar_costo_insercion(l))

#SELECCION
def ordenar_costo_seleccion(lista):
    '''     '''
    for i in range(len(lista)-1):
        minimo = i
        for j in range(i,len(lista)):
            if lista[j]["id"]<lista[minimo]["id"]:
                minimo = j
            j = i
        lista[j],lista[minimo] = lista[minimo],lista[j]
    return lista
print(ordenar_costo_seleccion(l))

#BURBUJEO
def ordenar_costo_burbujeo(lista):
    '''     '''
    for i in range(len(lista)-1):
        for k in range(1,len(lista)-i):
            if lista[k]["id"]<lista[k-1]["id"]:
                lista[k],lista[k-1]=lista[k-1],lista[k]
    return lista
print(ordenar_costo_burbujeo(l))
# %% 6 y 7
'''Se tiene una lista que contiene diccionarios con las claves ?nombre?, ?mesa?, y ?especial?. 
Un ejemplo de listas de este tipo es el siguiente:'''
l=[{"nombre": "Gabi", "mesa": 3, "especial": "si"},
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

'''Implementar una función que tome una lista con este formato y la ordene por nombre.
Implementar una función que tome una lista con este formato y la ordene por mesa.
No está permitido usar la función built-in sorted, ni el método sort de las listas.

Realice el ejercicio anterior pero usando los 
otros dos algoritmos de ordenamiento vistos en clase.'''

#INSERCION
def ordenar_costo_insercion(lista):
    '''     '''
    for j in range(1,len(lista)):
        actual = lista[j]
        k = j
        while k > 0 and (actual["nombre"]<lista[k-1]["nombre"]):
            lista[k]=lista[k-1]
            k = k-1
        lista[k]=actual
    return lista
print(ordenar_costo_insercion(l))

#SELECCION
def ordenar_costo_seleccion(lista):
    '''     '''
    for i in range(len(lista)-1):
        minimo = i
        for j in range(i,len(lista)):
            if lista[j]["nombre"]<lista[minimo]["nombre"]:
                minimo = j
            j = i
        lista[j],lista[minimo] = lista[minimo],lista[j]
    return lista
print(ordenar_costo_seleccion(l))

#BURBUJEO
def ordenar_costo_burbujeo(lista):
    '''     '''
    for i in range(len(lista)-1):
        for k in range(1,len(lista)-i):
            if lista[k]["nombre"]<lista[k-1]["nombre"]:
                lista[k],lista[k-1]=lista[k-1],lista[k]
    return lista
print(ordenar_costo_burbujeo(l))

# %%

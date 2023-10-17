#%% 1
'''Implementar una función que tome una lista de números y un número 
y devuelva la posición de la primera aparición de ese número en la lista. 
Si el número no está en la lista debe devolver -1.'''
def posicion(lista:list, numero:int)->int:
    '''     '''
    if numero in lista:
        for elemento in range(len(lista)):
            if lista[elemento] == numero:
                return elemento
    else: return -1    
lista=[1,2,3,4,5]
posicion(lista,4)
# %% 2
'''Implementar una función que tome una lista de números y un número y devuelva 
la posición de la última aparición de ese número en la lista. 
Si el número no está en la lista debe devolver -1.'''
def posicion(lista:list, numero:int)->int:
    '''     '''
    if numero in lista:
        posiciones_elemento = []
        for i in range (len(lista)):
            if lista[i] == numero:
                posiciones_elemento += [i]
        return posiciones_elemento[-1]
    else: return -1    
lista=[1,2,3,4,5,2,3]
posicion(lista,2)

# %% 3
''' Implementar una función que tome una lista de números ordenada 
de menor a mayor y un número y devuelva la posición de alguna aparición de ese número 
en la lista. Si el número no está en la lista debe devolver -1.'''

def busqueda(listita:list,numero:int)->int:
    '''     '''
    lista = listita.copy()
    while lista[len(lista)//2]!=numero:
        if lista[len(lista)//2]>numero:
            lista = lista[:len(lista)//2]
        elif lista[len(lista)//2]>numero:
            lista = lista[len(lista)//2:]
    if lista[len(lista)//2]==numero:
        return lista.index(lista[len(lista)//2])
    
lista = [2,3,4,5,6,7,8,9]
busqueda(lista,3)

# %% 4
'''Se tiene una lista que contiene diccionarios con las claves ?id?, ?descripcion?, ?costo? 
y ?stock?. Un ejemplo de listas de este tipo es el siguiente:'''

lista = [{"id": 4, "descripcion": "Girgola", "costo": 449.0, "stock": 324},
{"id": 2, "descripcion": "Espinaca", "costo": 799.0, "stock": 3501},
{"id": 3, "descripcion": "Champignon", "costo": 629.0, "stock": 723},
{"id": 12, "descripcion": "Kiwi", "costo": 1299.0, "stock": 150},
{"id": 10, "descripcion": "Mandarina Okitsu", "costo": 389.0, "stock": 430},
{"id": 11, "descripcion": "Mandarina Nova", "costo": 389.0, "stock": 900}]

'''Implementar una función que tome una lista con este formato y un id y devuelva el 
elemento de la lista cuyo id conincida.
Implementar una función que tome una lista con este formato y una descripcion y devuelva 
el stock del elemento de la lista cuya descripcion conincida.'''

def buscador(lista, id):
    for diccionario in lista:
        if diccionario['id']==id:
            return diccionario['descripcion']
print(buscador(lista,3)) 

def buscador2(lista, descripcion):
    for diccionario in lista:
        if diccionario['descripcion']==descripcion:
            return diccionario['stock']
print(buscador2(lista,'Kiwi'))

# %% 5 TERMINAR EL B
''' Se tiene la misma lista que en el ejercicio anterior pero ordenada por id:'''

lista = [{"id": 2, "descripcion": "Espinaca", "costo": 799.0, "stock": 3501},
{"id": 3, "descripcion": "Champignon", "costo": 629.0, "stock": 723},
{"id": 4, "descripcion": "Girgola", "costo": 449.0, "stock": 324},
{"id": 10, "descripcion": "Mandarina Okitsu", "costo": 389.0, "stock": 430},
{"id": 11, "descripcion": "Mandarina Nova", "costo": 389.0, "stock": 900},
{"id": 12, "descripcion": "Kiwi", "costo": 1299.0, "stock": 150}]

'''Implementar una función que dada una descripcion de un producto y una cantidad 
a comprar nos devuelva si hay stock suficiente para poder realizar esa compra.

Implementar una función que dado un id de un producto nos devuelva su precio, 
siendo el precio igual al costo + 20%. El peor caso de la función debe resolverse 
en un tiempo mejor que , donde  es la cantidad de elementos en la lista.'''

def producto_comprar(lista, descripcion, cantidad):
    for diccionario in lista:
        if diccionario['descripcion']==descripcion.capitalize():
            if cantidad <= diccionario['stock']:
                return 'Hay stock suficionte'
            else: return 'NO hay stock suficiente'
producto_comprar(lista,'Espinaca',3502)

def id_precio(lista,id):
    l = lista.copy()
    medio = int(len(l)//2)
    while l[medio]['id'] != id: #division entera
        if l[medio]['id']<id:
            l = l[medio:]
            medio = int(len(l)//2)
            continue
        else:
            l = l[:medio]
            medio = int(len(l)//2)
            continue

    if id == l[medio]['id']:
        precio = int(l[medio]['costo'])*1.2
        return precio
print(id_precio(lista,3))
# %% 6
'''Se tiene una lista que contiene diccionarios con las claves 
?nombre?, ?mesa?, y ?especial?. Un ejemplo de listas de este tipo es el siguiente:'''

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

'''Implementar una función que tome una lista con este formato y un nombre y devuelva 
la mesa en la que se encuentra la persona con ese nombre.'''

def encontrar_mesa(lista,nombre:str):
    for diccionario in lista:
        if diccionario['nombre'] == nombre.capitalize():
            return diccionario['mesa']
encontrar_mesa(lista,'Cris')
# %% 7
'''Se tiene la misma lista que en el ejercicio anterior pero ordenada por nombre:'''

lista = [{'nombre': 'Aike', 'mesa': 3, 'especial': 'si'},
{'nombre': 'Alex', 'mesa': 1, 'especial': 'no'},
{'nombre': 'Ariel', 'mesa': 2, 'especial': 'no'},
{'nombre': 'Cris', 'mesa': 2, 'especial': 'no'},
{'nombre': 'Dani', 'mesa': 1, 'especial': 'no'},
{'nombre': 'Gabi', 'mesa': 3, 'especial': 'si'},
{'nombre': 'Indigo', 'mesa': 1, 'especial': 'si'},
{'nombre': 'Matu', 'mesa': 3, 'especial': 'no'},
{'nombre': 'Pato', 'mesa': 1, 'especial': 'si'},
{'nombre': 'Sora', 'mesa': 2, 'especial': 'si'},
{'nombre': 'Xue', 'mesa': 2, 'especial': 'no'}]

'''Implementar una función que tome una lista con este formato y un nombre y devuelva 
la mesa en la que se encuentra la persona con ese nombre.
El peor caso de la función debe resolverse en un tiempo mejor que , 
donde  es la cantidad de elementos en la lista.'''

def encontrar(lista,nombre):
    l = lista.copy()
    medio = len(lista)//2
    while l[medio]['nombre']!=nombre:
        if l[medio]['nombre']>nombre:
                l = l[:medio]
                continue
        else:
            l = l[medio:]
            continue
    if l[medio]['nombre']==nombre:
            return l[medio]['mesa']
    
encontrar(lista,'Xue')        
# %%

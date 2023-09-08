#8/9

# DICCIONARIOS
    #las claves pueden ser CUALQUIER COSA que sea INMUTABLE (xq tiene que ser unica)
    #los valores cualquier cosa
'''si lo defino y no existe, me lo argega'''
    #defino: libro["categoria"] = comedia (no hay problema)
'''si intento acceder a algo que no existe, tira ERROR'''
    #si busco/indexo: x = libro["cccc"] y no existe --> ERROR
    #NO HAY ORDEN
libro = {
      "titulo": "Python for Beginners",
      "autor": "John Smith",
      "año": 2020,
      "categoría": ["Programación", "Informática", "Ingeniería"],
      "paginas": 300,
      "precio": 2999.9}
#pertenencia --> in
"titulo" in libro #-> True
#eliminar --> del libro["precio"] // del libro
    #se pueden eliminar elementos de los mutables
del libro["precio"]

#metodos de diccionarios
#conocer todas las claves .keys() .values() .items() --> devuelve un ITERABLE (no una lista)
list(libro.keys())
for nombre in libro.keys(): #usar nombres representativos
    print(nombre)
#item() --> por default, defino solo un elemtno, te tira tupla
for elemento in libro.items():
    print(elemento) #-> ("titulo","Python for Beginners)
for elemento, item in libro.items():
    print(elemento, item) #se guardan por separado


# .get(clave, "mensaje si no encuentra") --> si no lo encuentra: -> None
# .pop() -> lo elimina y te devuelve el valor 
        #si le pones mensaje de error, no te tira error (si no le poner --> ERROR)

#diccionarios POR COMPRENSION
# {<new.key>:<new.value> for <item> in <iterable>}
lista = ["diez", "veinte", "treinta"]
d1 = {10*k:v for (k,v) in enumerate(lista, 1)} #-> {10: "diez", 20: "veinte", 30: "treinta"}
d2 = {m:cadena.upper() for m,cadena in d1.items()} #-> {10: "DIEZ", 20: "VEINTE", 30: "TREINTA"}

#DICCIONARIO DE FUNCIONES

#%%
'''Implemente un programa que solicite al usuario un texto 
e imprima por pantalla una tabla con cada caracter presente en el texto 
y la cantidad de veces que se repite. Debe ser case sensitive'''
texto = input("Ingrese un texto: ")
lista = []
for caracter in texto:
    if caracter.isalpha():
        repeticiones_caracter = texto.count(caracter)
        if caracter not in lista: 
            print(f"{caracter} {repeticiones_caracter}")
        lista+=caracter

# %%

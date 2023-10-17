#17/10
'''Implemente un programa que lea un archivo de texto y genere otro archivo 
donde se guarde una lista de palabras (separadas por un salto de línea) 
ordenadas de acuerdo a su frecuencia de aparición (cantidad de veces que la palabra se 
repite en el texto original) e indicar dicha frecuencia al lado de cada una 
(espacio de por medio). Por ejemplo:
saltamonte 14
tarima 12
tractor 8
El programa debe utilizar diccionarios y un algoritmo de ordenamiento 
basado en los ya vistos (sin usar el método sort()).
En el campus está disponible el archivo de prueba enigma.txt'''

with open('problemas/enigma.txt', encoding='utf-8') as file:
    for linea in file:
        palabras = [palabras for palabras in linea.rstrip("\n").split()]

    diccionario_palabras = {}
    for palabra in palabras:
        if palabra not in diccionario_palabras:
            diccionario_palabras[palabra]=0
        diccionario_palabras[palabra] += 1

    ord_palabras = list(diccionario_palabras.keys())
    n=len(ord_palabras)
    swapped = True
    while swapped:
        swapped = False
        for i in range(1,n):
            if diccionario_palabras[ord_palabras[i-1]]>diccionario_palabras[i]:
                ord_palabras[i-1],ord_palabras[i] = ord_palabras[i],ord_palabras[i-1]
                swapped = True
    for palabra in ord_palabras:
        print(f"{palabra}:{diccionario_palabras[palabra]}")

'''CORREGIR'''
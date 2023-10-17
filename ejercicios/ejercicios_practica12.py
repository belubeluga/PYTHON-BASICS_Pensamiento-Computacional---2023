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
with open("enigma.txt") as file:
    for linea in file:
        print([palabras for palabras in linea.rstrip("\n").split(' ')])

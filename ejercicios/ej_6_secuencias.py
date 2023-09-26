#%% 1
'''Corrija este código defectuoso para que imprima la longitud de un string:'''
print(len("Esto es un texto"))

#%% 2
'''Completar la función count_A para cuente la cantidad de letras A 
que se encuentran en un texto (y devuelva dicha cantidad). Complete el siguiente código:'''

def count_A(the_string: str) -> int:
    '''docstring'''
    return the_string.count('A')
aa = 'ALKLKALLAAA'
count_A(aa)

#%% 3
'''Escriba una función count(s, character) que cuente cuántas veces 
aparece el carácter character en la cadena s. Complete el siguiente código:'''

def count(s: str, character: str) -> int:
    contador = 0
    for c in s:
        if c == character:
            contador += 1
    return contador

'''Escriba un programa que le pida al usuario un carácter y un texto y luego 
muestre la cantidad de ocurrencias del carácter en el texto ingresado. 
Por ejemplo, puede seguir la siguiente interfaz:
texto: podemos ingresar una cadena relativamente larga y contar la cantidad de 
ocurrencias de un carácter carácter: a
> la cantidad de "a" en el texto es: 15'''
caracter = input("caracter: ")
texto = input("texto: ")
print(f'la cantidad de {caracter} en el texto es: {count(texto, caracter)}')

'''Escriba un programa que le pida al usuario un texto y dos caracters e indique 
qué carácter tiene más ocurrencias. Por ejemplo, puede seguir la siguiente interfaz:
texto: podemos ingresar una cadena relativamente larga y contar la cantidad de 
ocurrencias de un carácter
carácter 1: a
carácter 2: e
El texto tiene más "a" que "e".'''
caracter2 = input("caracter 2: ")
print(f'Caracter 1: {caracter}')
print(f'Caracter 2: {caracter2}')
if count(texto, caracter)>count(texto,caracter2): print(f'El texto tiene más {caracter} que {caracter2}.')
elif count(texto, caracter)<count(texto,caracter2):print(f'El texto tiene más {caracter2} que {caracter}.')
else: print(f'El texto tiene la misma cantidad de {caracter} y {caracter2}')
#%% 4
'''Escriba una función que tome una cadena de texto y retorne una nueva cadena 
formada por la letra inicial, la letra del medio, y la letra final, de la cadena inicial.'''

def shorten(s: str) -> str:
    if len(s)<3: return s
    else:
        l1 = s[0]
        lu = s[-1]
        lm = s[int(len(s)/2)]
        return l1+lm+lu

shorten('code')

#%% 5
'''Una dirección IP (IPv4) es una cuarteto de números entre 0 y 255 (inclusive) 
separados por '.', y es la dirección única de cada dispositivo conectado a una red, 
como la dirección postal de una casa en una ciudad. Escribir una función que dada una 
dirección IPv4 válida, devuelva una versión modificada de esa dirección IP, 
a esta versión modificada la llamaremos 'IP con colmillos'. Una dirección IP 
con colmillos reemplaza cada punto '.' de la dirección IP original con '[.]'.'''

def colmillos(IPv4):
    IP = IPv4.split('.')
    return '[.]'.join(IP)
IPv4 = input('IPv4: ')
print(colmillos(IPv4))

#%% 6
'''Algunos tipos de piedras son joyas, y todas las joyas son piedras. 
Vamos a representar cada piedra con un carácter, por ejemplo la 'a', 
por lo que una cadena de caracteres representa un conjunto de piedras, 
por ejemplo 'aaAb' es un conjunto de piedras. 
Dada una cadena de caracteres que representa los tipos de piedras que son joyas, 
y otra cadena de caracteres que representa las piedras que tienes, 
quieres saber cuántas joyas tienes, es decir, cuántas de las piedras que tienes 
son también joyas.
Las letras distinguen entre mayúsculas y minúsculas, 
por lo que 'a' se considera un tipo de piedra diferente de 'A'.'''

def joyas(piedras, joyas)-> int:
    '''     '''
    contador = 0
    for piedra in piedras:
        if piedra in joyas:
            contador+=1
    return contador

Piedras1 = 'aAAbbbb'
joyas1 = 'aA'

Piedras2 = 'ZZ'
joyas2 = 'z'

print(joyas(Piedras1,joyas1))
print(joyas(Piedras2, joyas2))







#%% EJERCICIOS CLASE DE PROBLEMAS ejercicio 7
'''Queremos acortar el largo de un mensaje para que entre 
en una cantidad fija de caracteres, n. Si el mensaje tiene más de n 
caracteres, es decir, no entra en n caracteres, entonces eliminaremos
el excedente y lo completaremos con ?.? hasta completar los n 
caracteres, y a lo sumo 3 puntos. En la tabla siguiente se muestran,
dados un mensaje y un n, 
se muestran ejemplos del resultado esperado.'''
texto = "algo de texto para probar"
largo_impresion = 5
largo_texto = len(texto)
if largo_impresion < 4:
    print("."*largo_impresion)
elif largo_texto > largo_impresion:
    print(f'{texto[:largo_impresion-2:]}...')
else: print(texto)







# %% EJERCICIOS CLASE DE PROBLEMAS
'''Realizar una funcion que dad una lista de enteros,
devuelva tres listas:
1. La misma lista en reversa
2. La lista pero solamente sus elementos pares
3. La lista pero cada elemento elevado al cuadrado'''

def f_listas(lista_a):
    b = lista_a[::-1]
    c = [num for num in lista_a if num%2 == 0]
    d = [num**2 for num in lista_a]
    return b,c,d

print(*f_listas([4,5,6,8,2,4,2,99])) # el * al principio desempaqueta todo
# %% EJERCICIOS CLASE DE PROBLEMAS
'''Realizar una funcion que dad una lista de numeros,
devuelva la suma de los elementos positivos y la suma de los elementos negativos'''
def sumas(numeros:list)-> tuple:
    pos = sum([num for num in numeros if num >=0])
    neg = sum([num for num in numeros if num <0])
    return pos, neg
#%% ejercicio 12 EJERCICIOS CLASE DE PROBLEMAS
'''Implementar una funcion que dadas 2 secuencias recibidas como argumentos, retorne los indices de cada una de ellas
a partir de los cuales se obtiene la subsecuencia en comun de mayor longitud, 
y retorne tmb la longitus de dicha secuencia'''
def alineacion(seq1, seq2):
    max_coincidencia = ''
    for i1,c1 in enumerate(seq1):
        for i2,c2 in enumerate(seq2):
            largo = 0
            while i1+largo < len(seq1) and i2+largo < len(seq2) and seq1[i1+largo] == seq2[i2+largo]:
                largo += 1
            if len(max_coincidencia)<largo:
                max_coincidencia = seq1[i1: i1+largo]
                max_i1 = i1
                max_i2 = i2
    return max_coincidencia, max_i1, max_i2
seq1 = ""
seq2 = ""
print(alineacion(seq1,seq2))

#%% EJERCICIOS CLASE DE PROBLEMAS
lis = ["6", "31"] 
lista = []
for i in (lis):
    lista += [int(i)]
lista
# %% EJERCICIOS CLASE DE PROBLEMAS
'''Imprima en la consola de Python interactivo los números pares del 0 al 100'''
counter = 0
while counter<100:
    counter += 1
    print(counter)

# %% EJERCICIOS CLASE DE PROBLEMAS
'''Escriba un programa que imprima en pantalla los números que son 
a la vez múltiplos de 7 y 23 (por ejemplo, 161 es múltiplo de ambos, 
21 es múltiplo de 7 pero no de 23 y 46 es múltiplo de 23 pero no de 7).'''
num = int(input("num: "))
for i in range (num):
    if i%7==0 and i%23==0:
        print(i)
#%% EJERCICIOS CLASE DE PROBLEMAS
'''Escribir un programa que pida al usuario dos números A y B e 
imprima en la pantalla todos los números múltiplos de, a la vez, 7 y 23, 
en el intervalo [A, B).'''

A = int(input("A: "))
B = int(input("B: "))
if A > B:
    A,B = B,A
for i in range (A, B):
    if i%7==0 and i%23==0:
        print(i)

#%% EJERCICIOS CLASE DE PROBLEMAS
'''Escribir un programa que pida al usuario cuatro números A, B, C, y D 
e imprima en la pantalla todos los números múltiplos de, a la vez, C y D, 
en el intervalo [A, B).'''
A = int(input("A: "))
B = int(input("B: "))
C = int(input("C: "))
D = int(input("D: "))
if A > B:
    A,B = B,A
for i in range (A, B):
    if i%C==0 and i%D==0:
        print(i)
#%% EJERCICIOS CLASE DE PROBLEMAS
'''Escriba un programa que imprima el producto entre dos números 
haciendo una suma repetida (sin utilizar el operador de multiplicación * 
del lenguaje de programación).'''
A = int(input("A: "))
B = int(input("B: "))
a1 = 0
for i in range(1,B+1):
    a1 += A
a1 
# %% EJERCICIOS CLASE DE PROBLEMAS
'''La suma de Gauss permite hallar el resultado de sumar los números naturales entre 1 y n, 
es decir: 1 + 2 + ? + (n - 1) + n. 
Escriba un programa que compute esta suma (iterando) y que tenga como entrada el número n. 
Luego verifique si el resultado es correcto comparándolo con la forma cerrada 
de acuerdo a la siguiente ecuación: '''
A = int(input("A: "))
B = int(input("B: "))
a1 = 0 #!!!!!!!!!!!!!!!!!
for i in range(0,B+1):
    A += 1

# %% EJERCICIOS CLASE DE PROBLEMAS
#ejercicios clase secuencias 6/9
'''A partir de la siguiente lista, extraiga las siguientes listas aplicando slicing'''
lista = [2,4,6,8,10,12,14,16,18]
lista1 = lista[:4]
lista2 = lista[6::]
lista3 = lista[1::3]
lista4 = lista [::-2]
# %% EJERCICIOS CLASE DE PROBLEMAS
#ejercicios clase secuencias 6/9
cadena = input("cadena: ")
lista = []
def MAYUSC(cadena):
    for letra in (cadena):
        if letra.isupper():
            a = ord(letra)+32
        elif letra.islower():
            a = ord(letra)-32
        else: a = ord(letra)
        x=chr(a)
        lista.append(x)
    return ''.join(lista)
MAYUSC(cadena)
# %% EJERCICIOS CLASE DE PROBLEMAS
#ejercicios clase secuencias 6/9
'''escriba una funcion q reciba una oracion ingresada por el usuario y devuelva una lista (q haga lo del split)'''
oracion = input("oracion: ")
#def separador(oracion:str)->list:
    #hd
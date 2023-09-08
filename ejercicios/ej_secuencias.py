#%% ejercicio 7
texto = "algo de texto para probar"
largo_impresion = 5
largo_texto = len(texto)
if largo_impresion < 4:
    print("."*largo_impresion)
elif largo_texto > largo_impresion:
    print(f'{texto[:largo_impresion-2:]}...')
else: print(texto)
# %%
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
# %%
'''Realizar una funcion que dad una lista de numeros,
devuelva la suma de los elementos positivos y la suma de los elementos negativos'''
def sumas(numeros:list)-> tuple:
    pos = sum([num for num in numeros if num >=0])
    neg = sum([num for num in numeros if num <0])
    return pos, neg
#%% ejercicio 12
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

#%%
lis = ["6", "31"] 
lista = []
for i in (lis):
    lista += [int(i)]
lista
# %%
'''Imprima en la consola de Python interactivo los números pares del 0 al 100'''
counter = 0
while counter<100:
    counter += 1
    print(counter)

# %%
'''Escriba un programa que imprima en pantalla los números que son 
a la vez múltiplos de 7 y 23 (por ejemplo, 161 es múltiplo de ambos, 
21 es múltiplo de 7 pero no de 23 y 46 es múltiplo de 23 pero no de 7).'''
num = int(input("num: "))
for i in range (num):
    if i%7==0 and i%23==0:
        print(i)
#%%
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

#%%
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
#%%
'''Escriba un programa que imprima el producto entre dos números 
haciendo una suma repetida (sin utilizar el operador de multiplicación * 
del lenguaje de programación).'''
A = int(input("A: "))
B = int(input("B: "))
a1 = 0
for i in range(1,B+1):
    a1 += A
a1 
# %%
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

# %%
#ejercicios clase secuencias 6/9
'''A partir de la siguiente lista, extraiga las siguientes listas aplicando slicing'''
lista = [2,4,6,8,10,12,14,16,18]
lista1 = lista[:4]
lista2 = lista[6::]
lista3 = lista[1::3]
lista4 = lista [::-2]
# %%
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
# %%
#ejercicios clase secuencias 6/9
'''escriba una funcion q reciba una oracion ingresada por el usuario y devuelva una lista (q haga lo del split)'''
oracion = input("oracion: ")
def separador(oracion:str)->list:
    #
# %%

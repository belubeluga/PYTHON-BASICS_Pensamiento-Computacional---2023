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

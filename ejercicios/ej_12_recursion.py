#%% 1
''' Para cada inciso, implementá una función recursiva que reciba 
un número z y un entero k y retorne:

z + k (sumando unos),
z * k (sumas sucesivas), y
z ^ k (multiplicaciones sucesivas).'''

def sumar(z:float,k:int)->int:
    if k < 1:
        return z
    else: return 1 + sumar(z,k-1)
sumar(20,3)

def mult(z,k):
    if k ==1:
        return z
    else: return z + mult(z,k-1)
mult(12,2)

def mutl_sucesivas(z,k):
    if k == 1:
        return z
    else: return z * mutl_sucesivas(z,k-1)
mutl_sucesivas(11,2)

# %% 2
'''Implementar una función recursiva que retorne la cantidad de dígitos de un número entero.'''
def cant_digitos(numero:int):
    if len(str(numero)) == 1:
        return 1
    else: return 1 + cant_digitos(numero//10)
cant_digitos(4) 

#%% 3
'''Implementar una función recursiva que reciba un entero no negativo y retorne dicho número 
espejado, es decir, para el 1234 retorna 4321.'''
def invertir(numero:int):
    if len(str(numero)) == 1:
        return str(numero)[-1]
    else: return str(numero)[-1] + invertir(str(numero)[:-1])
invertir(1234)

# %% 4
'''Escribir una función recursiva que calcule el n-ésimo número triangular 
(el número triangular de n es 1 + 2 + 3 + ··· + n).'''
def suma_n(n):
    if n == 1:
        return n
    else: return n + suma_n(n-1)
suma_n(6)

# %% 5
''' Implementar una función recursiva que dados dos números n y b retorne True si 
n es potencia de b.'''
def chequeo_potencia(n,b):
    if n > b:
        return chequeo_potencia(n/b,b)
    else: 
        if n == b:
            return True
        else: return False
chequeo_potencia(11,2)

# %% 6



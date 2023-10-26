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
''' Escribir una función recursiva que encuentre el mayor elemento de un vector.'''
def encontrar_mayor(vector):
    '''     '''
    if len(vector)<=1:
        return vector[0]
    if vector[1]<vector[0]:    
        vector[1],vector[0] = vector[0],vector[1]
    return encontrar_mayor(vector[1:])
encontrar_mayor([2,5,3,9,1])

#%% 7 
'''Escribir una función recursiva que calcule el n-ésimo número de la sucesión de Fibonacci. 
La misma se define como F_n = F_{n-1} + F_{n-2}, F_0 = F_1 = 1.

Dibuje un esquema (árbol de recursividad) de las llamadas recursivas para n = 6.'''

def fibonacci(n):
    '''     '''
    if n == 0 or n == 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

fibonacci(6)

# %% 8
''' Implementar una función recursiva que calcule el máximo común divisor (gcd) de 2 enteros 
x e y. El gcd de los enteros x e y es el mayor entero que divide a ambos números 
con resto cero.

Resuelva primero por fuerza bruta: comience a probar números desde y en orden descendiente.
Una mejora es utilizar la siguiente definición recursiva:

si y es igual a 0, entonces gcd(x, y) es x

si no gcd(x, y) es gcd(y, x % y).

Un tercer algoritmo es:

   si m y n son iguales:
       m es el gcd
   si m es mayor a n:
       el gcd(m, n) es gcd(m - n, n)
   si no:
       el gcd(m, n) es gcd(m, n - m)
'''
def gcd(x,y):
    ''' '''
    if y == 0:
        return x
    return gcd(y,x%y)
print(gcd(15,20))

def gcd2(x,y):
    ''' '''
    if x == y:
        return x
    if x > y:
        return gcd(y-x,x)
    else:
        return gcd(x,y-x)
print(gcd2(15,20))

#%% 9
''' Escribir una función recursiva que dado un arreglo de números, retorne el máximo, 
usando dividir y conquistar.'''
def encontrar_mayor(numeros):
    '''     '''
    if len(numeros)<=2:
        return max(numeros)
    if numeros[1]<numeros[0]:    
        numeros[1],numeros[0] = numeros[0],numeros[1]
    if encontrar_mayor(numeros[1:len(numeros)//2]) > encontrar_mayor(numeros[len(numeros)//2:]):
        return  encontrar_mayor(numeros[1:len(numeros)//2])
    else: return encontrar_mayor(numeros[len(numeros)//2:])

encontrar_mayor([4, 5, 3, 6, 4, 9, 1])
# %% 10
'''El triángulo de Pascal es un arreglo triangular de números que se define de la siguiente 
manera:

Las filas se enumeran desde n = 0, de arriba hacia abajo.
Los valores de cada fila se enumeran desde k = 0 (de izquierda a derecha).
Los valores que se encuentran en los bordes del triángulo son 1.
Cualquier otro valor se calcula sumando los dos valores contiguos de la fila de arriba.

Escribir una función recursiva pascal(n, k) que calcule el número correspondiente. 
Tener en cuenta que:
pascal(n, 0) = pascal(n, n) = 1 si n >= 0
pascal(n, k) = pascal(n - 1, k) + pascal(n - 1, k - 1) si n > k > 0.
Dibujar el árbol de recursividad para alguna llamada de interés.'''
def pascal(n,k):
    if (k == 0) or (k == n) and (n>=0):
        return 1
    if (n > k) and (k>0):
        return pascal(n-1,k)+pascal(n-1,k-1)
    else: return pascal(k-1,n)+pascal(k-1,n-1)
pascal(5,3)

# %% 11 HACER
'''Escribir una función recursiva que aplique las reglas del game de tenis, 
hasta ganar el game. Si consideramos los puntajes de tenis como 0, 15, 30, 40, 50 (Ventaja), 
60 (Punto), un jugador gana el game siempre que alcanza los 60 puntos. 
Si un jugador A con 40 puntos anota, y el otro jugador B tiene menos de 40 puntos, 
entonces A pasa directamente a 60 puntos y gana el game. Si, en cambio, 
ambos jugadores tienen 40 puntos, quien anota pasa a tener 50 puntos, o ventaja. 
Cuando un jugador tiene ventaja, puede ocurrir que gane el siguiente tanto, 
en cuyo caso gana el game, o puede ocurrir que el oponente gane el tanto, 
entonces pasan a tener ambos 40 puntos nuevamente.'''

def tenis(x,y, jugador):
    if jugador == x:
        if x in [0,15]:
            x += 15
        if x == 30:
            x = 40
        if y == 40 and (y == 40):
            y == 60
        if x == 40 and (y<40):
            x == 60
            return f'Ganadror = {jugador} --> {x,y}'
    if jugador == y:
        if y in [0,15]:
            y += 15
        if y == 30:
            x = 40
        if y == 40 and (x<40):
            y == 60
            return f'Ganadror = {jugador} --> {x,y}'
        if y == 40 and (x == 40):
            y == 60
    tenis(x,y,input("ganador"))
def tenis(x,,)
# %%

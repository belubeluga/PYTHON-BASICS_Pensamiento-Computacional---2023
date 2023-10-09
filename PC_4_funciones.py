#-------------------- FUNCIONES --------------------18/8

# FUNCIONES
        #entrada         --->       salida
        #argumentos      --->       valor retorno
        #parametros      --->       resultado
    # definir parametros de entradas
    # que sean chiquitas y reutilizables    (una tarea en particular)
import math
#keyword/nombre(parametros)
def beat (f1, f2, t):
    '''
    (Como funciona la funcion (manual)) --> lo busco con help(funcion)
    Compute a beat signal value at time t from cosine functions Of f1 and f 2 frequencies.
    f1 -- first cosine frequency
    f2 -- second cosine frequency
    t -- time at which to evaluate the beat
    Returns:
    beat signal
    '''
    tau = 2 * 3.14
    v1 = math.cos(tau * f1 * t)
    v2 = math.cos(tau * f2 * t)
    return v1 + v2 #NUNCA RETORNAR PRINT (hacer que te devuelvan valor solo, asi son reutilizables)
        # return no deberia MOSTRAR/imprimir el resultado
        # solo devolver valor
beat(110, 104, 0.2)
#%%
def greet(name):
    """Returns a string to greet someone.
    Arguments:
    Name -- name of the person to greet
    """
    return f'Hello, {name}' #indentacion
greet("Yoda") #invocacion
#%%
def suma(a, b):
    c = a + b
    return c
x = 2 #genero todos los parametros
y = 1 #Global frame   #(la cantidad que permite la funcion)
mensaje = "Resultado: "
f = suma(x, y) #se asignana los valores 
#                |--> (stack frame) // memoria temporal a = 2 // b = 1 
print(mensaje, f)

help(suma) #me devuelve el docstring de la funcion

# PYTHON TUTOR



#%%
# Problema 1
clave = "Correcto"
clave1 = input("Ingrese la clave:")
intentos = 1 #!!!!!

while clave1 != clave and intentos < 3:
    print("Clave incorrecta, intente otra vez\n")
    clave1 = input("Ingrese la clave:")
    intentos += 1
     
if clave1 != clave:
    print("Clave incorrecta. Se excedio la cantidad de intentos")
elif clave1 == clave:
    print("Clave correcta. Accediendo al sistema")
# %%
#ejercicio 2 (22/8)
#problemas 4
import random

for _ in range(100):
    num = random.randint(1,6)
    print(num)

#%%
#ejercicio 3
#problemas 4

notas = []
nota = input("nota o -1: ")


while nota != "-1":
    notas += [int(nota)]
    nota = input("nota o -1: ")

# forma 1
promedio = sum(notas) / len(notas)

# forma 2
suma = 0
for notaa in notas:
    suma += notaa
promedio1 = suma / len(notas)

print(promedio,'\n',promedio1)

# %%
p = bool(int(input('p = 1 o 0: ')))
q = bool(int(input('q = 1 o 0: ')))
r = bool(int(input('r = 1 o 0: ')))

if p:
    if q == r:
        z = 0
    elif q != r:
        z = 1
elif not(p):
    if q == r:
        z = 1
    else:
        z = 0
print(z)
# %%
x = 1
y = -2
z = 0

if y == 1:
    z = 2
if z == 1:
    w = x + y
    print("alpha")
elif z == 1 and x == 0:
    print("beta")
    w = z + x + y
    if w == 4:
        w = 2
    print("gamma")
elif z == 2:
    z = 1
    print("delta")
else:
    w = 10
    print("epsilon")

print("z =", z)
print("w =", w)
# %%
si = "flores" - "es"
# %%
bi = float("2.0")
print(bi)
# %%
x = bool(2)
print(x)
# %%
y = int('1.0')
print(y)
# %%
li = ["ab", 3, 35]
print(len(li))
# %%
tup = (2,3,"i")
print(len(tup))
print(len(str(tup)))
print(tup)
# %%
# CLASE 28/8


# Argumentos por omision:
def suma_geografica(r, n, a=1): #siempre el argumento x omision al FINAL
    '''Compute a geometric sum of n terms, w/ coefficient a and ratio r
    Argumentos:
    r -- ratio
    n -- terms to sum
    a -- coefficient (default: 1)
    (si no se define abajo el c, se toma c=1 por default)'''
    total = 0
    for i in range (0, n):
        total = total + n + a * r ** i
    return total
def name(x, *arg2): #el '*' delante del argumento --> Multiples parametros
    ''''''
                    # arg es una TUPLA que guarda todos los parametros
                    # ingresados en esa posicion
def name(x, **arg2): #'**' permiten MULTIPLES PARAMETROS con NOMBRE EXPLICITO
                    # se arma un DICCIONARIO dentro de la funcion
    ''''''

# TIPADO : hay lenguajes con TIPADO DINAMICO (ej python) o con TIPADO ESTATICO (C)
#TYPE HINTS
def nombre(arg: int)->int: #NO OBLIGA a que sea int, sino que sugiere
    ''''''            #salida

#%%
# FUNCIONES LAMBDA
# (funciones anonimas)
#lambda argumentos : expresiones
greet = lambda name: f"Hello, {name}"
#puedo darle nombre tmb
print((lambda name: f"Hello, {name}")("Pedro")) #definida y evaluada en 1 linea
print((lambda a, b: a + b)(3, 5))
# %%
# Fail fast, return early
    #probar errores al principio

def make_merengue(huevos, azucar, batidora, bowl):
    if not(huevos==4):
        return "ERROR_HUEVOS"
    if not(azucar == 170):
        return "ERROR_BATIDORA"
  #...
#ver como optimizar con SINGLE ENTRY, SINGLE EXIT
    # con ifs

# MODULOS
    #archivos python (xx.py)
#import modulo1
#import repaso_parcialito1
#import practica2
# y para despues acceder a las variables de esos modulos se usa
# repaso_parcialito1.x (x: variable)
#import modulo1
#r = modulo1.get_radius #get_radius siendo funcion de modulo1
#importar con un Alias
#import modulo1 as mod
# importar solo los elementos especificados
#from modulo1 import pi, get_radius

#MODULOS COMUNES:
import math
import random 
#import pandas as pd

#FUNCION MAIN
def suma(a,b):
    return a + b
def main():
    x = 2
    y = 3
    s = suma(x,y)

if __name__ == "__main__":
    main()



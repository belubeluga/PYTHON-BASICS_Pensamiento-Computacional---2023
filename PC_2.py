# CICLO WHILE
#estructuras basicas que REPITE
#%%
x = int(input("edad:"))

while x <= 8:
    print("Valor actual:", x)
    x += 1

# necesitamos un VALOR DE CORTE (condición de salida) ==> ctrl C para salir
# desconocemos la cantidad de ITERACIONES

pregunta = 'si'
while pregunta == 'si':
    palabra = input('\nIngrese una palabra: ')
    print(f'Palabra ingresada --> {palabra}')
    pregunta = input('Desea continuar? ')
print('\nSalimos del ciclo!')

#iniciar Valor
#    mientras condicion1 != centinela (salir)
#    mostrar Valor
#mensaje de fin

palabra = ''
while palabra != 'salir':
     palabra = input('Ingrese una palabra: ')
     print(f'Palabra ingresada --> {palabra}\n')
print('Salimos del ciclo!')

# BREAK
numero = 0
while numero < 100:
     numero = int(input('Ingrese un número: '))
     if numero == 8:
         print('El número es 8!! rompemos\n')
         break          # ROMPER
     print(f'Número ingresado --> {numero}\n')
print('Salimos del ciclo!')

numero = 0
while numero < 100:
     numero = int(input('Ingrese un número: '))
     if numero == 8:
         print('El número es 8!! continuamos\n')
         continue      # CONTINUAR
     print(f'Número ingresado --> {numero}\n')
print('Salimos del ciclo!')

# ALGORITMO DE HERÓN
z = 113
guess = 10
while abs(guess ** 2 - z) > 0.0001:
    guess = (guess + z / guess) / 2
print(f"El valor final de guess es {guess}")



# USAR DEBUGGER

# %%
# Problema 2

lista = []
texto = ''
while texto != "q":
        texto = input("nombre: ")
        lista += [texto]
        continue
if texto == "q":  
    print(lista) #ver de no imprimir q


#%%
nombre = input("ingrese nombre: ") #completar/corregir
apellido = input("ingrese apellido: ")
edad = input("inrese edad: ")
lista = [nombre, apellido, edad]
datos = nombre + apellido + edad
puntuacion = "." or "," or ";" 
while datos:
    nombre = input("ingrese nombre: ")
    apellido = input("ingrese apellido: ")
    edad = input("inrese edad: ")
    if puntuacion in datos: 
        print("intente nuevamente sin signos de puntuación")
        continue
    if puntuacion not in datos:
        break
print(lista)
# %%
nombre = '' #corregir
apellido = ''
edad = ''
lista = [nombre, apellido, edad]
datos = nombre + apellido + edad
 
while "." or "," or ";" in datos:
    nombre = input("ingrese nombre: ")
    apellido = input("ingrese apellido: ")
    edad = int(input("inrese edad: "))
    if "." or "," or ";" in datos:
        print("intente nuevamente sin signos de puntuación")
        continue
    elif "." or "," or ";" not in datos:
        break
    print(lista)
# %%




# CICLO DEFINIDO
#for <variable> in <iterable>:
#    <sentencia_usando_valor>

# Funcion RANGE()
    #range(start, stop, step) #--> objeto iterable
        # INT!!         (tienen que ser numeros ENTEROS)

    # x default: #start = 0
             #stop = 10
             #step = 1 (cuanto sumo)
for i in range(3, 17, 2):
    print(i, end=" ") # 3 5 7 9 11 13 15

#%%
lista = [-2, '123', 'beta', True, False, 1500]
for e in lista:
  print(e)
print('Finalizó el ciclo!')

#%%
#EJ: suma de numeros naturales
n_max = int(input("n maximo?"))
suma = 0
for i in range(n_max + 1):
    suma += i
print(f"La suma de 0 a {n_max} es {suma}")

#%%
#EJ2: 
"""Calcula n!"""
n = int(input("¿n? "))
result = 1
for i in range(1, n + 1):
  result *= i
print(f"El factorial de {n} es {result}")

#%%
#Problema 1
# Implemente un programa que imprima en pantalla una tabla con tres columnas. 
# La primera debe ser un número entero x entre 1 y n; 
# la segunda el “resto” de la división entre x y un número k (x%k); 
# la tercera, debe indicar (con True/False) si x es múltiplo de k. 
# El programa debe solicitar al usuario dos entradas: 
#       1) el número máximo n; 
#       2) el número entero k.

#numero%divisor → resto de número/divisor

n = int(input("ingrese el número máximo n: "))
k = int(input("ingrese el número entero k: "))

categorias = "Número   Resto   Múltiplo?"
print(categorias)
num = 1

for i in range(1,n+1):
    if i % k == 0:
        multiplo = True
    else:
        multiplo = False
    print(i,'\t',i%k,'\t',multiplo)
    

        #CAMBIAR ESQUEMA DE RESULTADOS

# %%
# PROBLEMA 2
#Se requiere implementar un programa que 
#dado un número representado en base binaria ingresado por el usuario 
#(ejemplo: 010011011) lo convierta a base decimal y lo muestre en pantalla. 
#El número binario ingresado puede tener una cantidad de bits arbitraria.
#Seguir la siguiente regla para la conversión de binario a decimal:
base_decimal = 0
binario = str(input("escriba un num binario: "))
for i in range (0, len(binario)):
    base_decimal += int(binario[i])*(2**int((len(binario)-int(i+1))))
print("Número binario:", binario)
print("Número decimal:", base_decimal)

# %%
#PROBLEMA EJEMPLO 6 (15/8)
edad = int(input("Edad:"))
cupon = input("Tiene cupon? si/no")

if edad <= 4:
    precio = 0
elif 5<= edad < 18:
    precio = 250
elif edad >= 18:
    precio = 500

if cupon == "si":
    precio_final = precio*0.5 # o hacer precio /= 2 (le vuelve a asignar otro valor a precio)
else:
    precio_final = precio #y aca imprimiría precio

print(f'Precio es ${precio_final}')

# %%
#18/8
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

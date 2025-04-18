#-------------------- CICLOS WHILE --------------------
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

# %% Problema 2
lista = []
texto = ''
while texto != "q":
        texto = input("nombre: ")
        lista += [texto]
        continue
if texto == "q":  
    print(lista) #ver de no imprimir q


#%% ejemplo
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
# %% ejemplo
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
# %% CICLO DEFINIDO
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

#%% ejemplo
lista = [-2, '123', 'beta', True, False, 1500]
for e in lista:
  print(e)
print('Finalizó el ciclo!')

#%% ej1: suma de numeros naturales
n_max = int(input("n maximo?"))
suma = 0
for i in range(n_max + 1):
    suma += i
print(f"La suma de 0 a {n_max} es {suma}")

#%% ej2 
"""Calcula n!"""
n = int(input("¿n? "))
result = 1
for i in range(1, n + 1):
  result *= i
print(f"El factorial de {n} es {result}")

#%% Problema 1
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

# %% Problema 2
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

# %% Problema EJEMPLO 6 (15/8)
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

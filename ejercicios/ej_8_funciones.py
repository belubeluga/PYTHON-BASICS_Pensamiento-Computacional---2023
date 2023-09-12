#1 para no tener que repetir codigo y optimizarlo
import math
#%% 2
'''Escriba una función que devuelva el cuadrado de un número (sin 
utilizar el operador de potencia del lenguaje de programación).'''
def potencia(num:int):
    'este programa eleva el numero insertado (num) al cuadrado'
    return num ** 2
x = int(input("num: "))
print(potencia(x))

#%% 3
'''Escriba una función llamada sumador que recibe dos argumentos 
y devuelva su suma. Luego, ejecute pruebas con distintos tipos de 
datos (dos strings, dos en punto flotante, un int y un str, etc.).'''
def sumador(x:int, y:int)->int:
    'recibidos dos numeros (x,y), te devuelve su suma'
    return x + y
a = int(input("num1: "))
b = int(input("num2: "))
print(sumador(a,b))

# %% 4
def multiply(a, b):
    return a * b

#%% 5
'''Implemente una función que solicite un número por la consola, que represente 
el radio de una circunferencia, y muestre en pantalla el perímetro 
de dicha circunferencia. En la consola se debe ver lo siguiente:
Ingrese un valor que representa el radio de una circunferencia: [ENTRADA]
El perímetro resultante es [RESULTADO]'''

def perimetro_circ(radio:float):
    'cumple consdigna'
    pi = 3.141592653589793
    return 2*pi*radio
radio = float(input("Ingrese un valor que respresenta el radio de una circunferencia: "))
print(f'El perimetro resultante es {perimetro_circ(radio)}')

# %% 6
'''Para la función definida en el siguiente código, encuentre una implementación 
alternativa que permita implementar la misma función pero reduciendo 
las 7 líneas del cuerpo de su definición a un cuerpo de sólo 2 líneas.'''
def some_function(name, last_name, age, profesion):
    return (('Name: ', name, last_name),('Age: ', age, 'years'), ('Profesion: ', profesion))
    
#%% 7
'''Escriba una función que redondee un número de tipo flotante 
al entero más cercano y devuelva este número entero.'''
def redondeo(num:float)->int:
    '''consigna'''
    if num%1 >= 0.5:
        return int(num) + 1
    else: return int(num)

'''Escriba un programa que pida al usuario el número y muestre en la consola interactiva 
el resultado de ejecutar la función desarrollada.'''
x = float(input("elegir un num: "))
print(redondeo(x))

# %% 8
'''Escriba:
- una función que dada una tasa de interés anual, una cantidad de años y 
un capital inicial, retorne el capital al finalizar el período.

- un programa que pida al usuario los datos necesarios y muestre en 
la consola interactiva el resultado de ejecutar la función desarrollada.'''

def interes_simple(interes_anual, años, capital_inicial):
    '''docstring'''
    return capital_inicial*(1 + años*interes_anual)

i = float(input("tasa de interes anual: "))
k = int(input('años: '))
ci = float(input('capital inicial: '))
print(f'Capital final: ${interes_simple(i,k,ci)}')

# %% 9
'''Escriba:
- una función que dada una tasa de interés anual, una cantidad de años y un 
capital inicial, retorne el capital al finalizar el período.
- un programa que pida al usuario los datos necesarios y muestre en la consola 
interactiva el resultado de ejecutar la función desarrollada'''

def interes_compuesto(interes_anual, años, capital_inicial):
    '''docstring'''
    return capital_inicial*((1 + interes_anual)**años)

i = float(input("tasa de interes anual: "))
k = int(input('años: '))
ci = float(input('capital inicial: '))
print(f'Capital final: ${round(interes_compuesto(i,k,ci),2)}')

# %% 10
'''Escriba:
- una función que dada una tasa de interés nominal anual y períodos de composiciones
mensuales calcule la tasa efectiva anual para todo el año.
- un programa que pida al usuario los datos necesarios y muestre en la consola 
interactiva el resultado de ejecutar la función desarrollada.'''

def tasa_interes(i,n):
    '''i = tasa de interes nominal
    n = cantidad de periodos de composicion (o frecuencia)'''
    return (1 + (i/n))**n - 1

int_nominal = float(input("tasa de interes nominal: "))
frecuencia = int(input('cantidad de periodos: '))
print(f'Tasa de interes efectiva: {round(tasa_interes(int_nominal, frecuencia),4)}')

#%% 11 
'''Escriba:
- una función que dados los tres primeros items 
del listado anterior, obtenga el monto final ().
- un programa que pida al usuario los datos necesarios y muestre 
en la consola interactiva el resultado de ejecutar la función desarrollada.'''
def valor_futuro(c,k,i):
    ''''''
    return c*((1 + i)**k - 1)/i

print(valor_futuro(float(input('c: ')), float(input('k: ')), float(input('i: '))))

# %% 12
'''Escriba una función que dadas la hora, minutos y segundos devuelva el tiempo en segundos.
Escriba un programa que pida la hora al usuario y muestre el tiempo en segundos.'''
def contador_segundos(hora,minutos,segundos):
    '''docstrings'''
    return hora*60*60 + minutos*60 + segundos
hora = int(input('hora: '))
min = int(input('min: '))
sec = int(input('sec: '))
print(contador_segundos(hora,min,sec))

# %% 13
'''Escriba una función que dado un número devuelva el primer número 
múltiplo de 10 inferior o igual a él. 
Por ejemplo, para 153 debe devolver 150.'''

def min_multiplo10(num)->int:
    '''docstring'''
    return (num // 10) * 10
num = int(input('numero: '))
print(f'minimo multiplo de 10 para el numero {num} es {min_multiplo10(num)}')

#%% 14
'''Escriba una función que dado un tiempo en segundos, retorne el tiempo en horas, 
minutos y segundos (similar al ejercicio 12). 
Por ejemplo, para 3745 debe devolver 1, 2, 25.'''
def horas_min_sec(segundos)->tuple:
    '''consigna'''
    horas = segundos//(60*60)
    mins = (segundos-horas*(60*60))//60
    secs = segundos-horas*60*60-mins*60
    return horas, mins, secs
print(horas_min_sec(int(input('segundos: '))))

# %% 15
'''Escribir una función que dada una lista de números y un entero n,
retorne una nueva lista donde cada elemento de la nueva lista es el 
promedio de n elementos consecutivos de la lista original. 
Por ejemplo, para [7.0, 9, 3.0, 6, 6, 2] y n = 4, retorna [6.25, 6.0, 4.25]. 
Donde 6.25 es el promedio de 7, 9, 3, y 6, 
mientras que 4.25 es el promedio de 3, 6, 6, y 2.'''
def promedio_n(lista:list, n:int)->list:
    '''consigna'''
    if n > len(lista): return None
    else: return sum(lista[0:n])/n

lista = [5,6,7,9,9]
promedio_n(lista,3)

# %% 16
'''Escribir una función que dado un día del año (un número del 1 a 366) 
retorne el día de la semana que le corresponde. 
Debe suponer que el año comenzó un domingo. 
Por ejemplo: si se ingresa '5', retorna 'jueves', si se ingresa '10' retorna 'martes', 
si se ingresa '294' retorna 'sabado'.

Escribir un programa que le pida al usuario un número y, 
usando la función desarrollada, imprima el día correspondiente.'''

def dia_semana(dia):
    '''docstring (año comenzado un domingo)'''
    if dia%7==0:
        return 'Sabado'
    elif dia%7==1:
        return 'Domingo'
    elif dia%7==2:
        return 'Lunes'
    elif dia%7==3:
        return 'Martes'
    elif dia%7==4:
        return 'Miercoles'
    elif dia%7==5:
        return 'Jueves'
    elif dia%7==6:
        return 'Viernes'
    
num = int(input('num dia: '))
print(dia_semana(num))
    

# %%

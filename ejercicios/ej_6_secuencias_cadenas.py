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

#%% 7 REHACER/REVISAR

'''Queremos acortar el largo de un mensaje para que entre en una cantidad fija de caracteres, 
n. Si el mensaje tiene más de n caracteres, es decir, no entra en n caracteres, entonces 
eliminaremos el excedente y lo completaremos con '.' hasta completar los n caracteres, 
y a lo sumo 3 puntos. En la tabla siguiente se muestran, 
dados un mensaje y un n, se muestran ejemplos del resultado esperado.'''


n = int(input("n: "))
mensaje = input("mensaje: ")

if len(mensaje) > n:
    for i,caracter in enumerate(mensaje,1):
        mensaje_n = ''
        while i<=n:
            mensaje_n += caracter
        if len(mensaje)-len(mensaje_n)>3:
            print(mensaje_n + '.'*3)
        else: print(mensaje_n + '.'*(len(mensaje)-len(mensaje_n)))
else: print(mensaje)

#%% 8 REVISAR/REHACER
'''Programar una función que retorne True si un password (string) cumple con los siguientes requisitos:

Tiene que tener por lo menos una letra minúscula.
Tiene que tener por lo menos una letra mayúscula.
Tiene que tener por lo menos un número.
Tiene que tener por lo menos un signo no alfanumérico (p.ej. ! ó $).
Tiene que tener entre 8 y 31 caracteres.'''

contraseña = input("contraseña: ")
contador = 0
def password(contraseña:str)->bool:
    ''' Chequea si una contraseña cumple con todas las siguientes condiciones:
        1) Tiene que tener por lo menos una letra minúscula.
        Tiene que tener por lo menos una letra mayúscula.
        Tiene que tener por lo menos un número.
        Tiene que tener por lo menos un signo no alfanumérico (p.ej. ! ó $).
        Tiene que tener entre 8 y 31 caracteres.

        minuscula : bool que chequea si se cumple la consigna 1
        mayuscula: bool consigna 2
        numero: bool consigna 3
        signo: bool consigna 4
        largo: bool consigna 5

        Devuelve True si la contraseña cumple con todo, y False en caso contrario
      '''
    if 8<=len(contraseña)<=31:
        largo = True
    mayuscula = True in [caracter.isupper() for caracter in contraseña] 
    minuscula = True in [caracter.islower() for caracter in contraseña]
    numero = True in [caracter.isdecimal() for caracter in contraseña]  
    signo = True in [not(caracter.isalnum()) for caracter in contraseña]  
    if largo + minuscula + mayuscula + numero + signo == 5:
        return True
    else: return False

#%% 9
'''Escribir una función que reciba una cadena, representando una fecha en formato AAAA-MM-DD, 
y retorne un True si esa fecha corresponde a Sagitario, el signo del zodiaco. 
Sagitario es entre el 22 de noviembre y el 21 de diciembre (ambas fechas inclusive).
En el formato AAAA-MM-DD, AAAA representa el año con 4 dígitos, MM el mes con 2 dígitos, 
y DD el día con 2 dígitos.'''
cadena = input('fecha: ')

def is_sagitario(fecha:str)->bool:
    '''     '''
    lista_fecha = cadena.strip().split('-')
    if int(lista_fecha[1])==11 and int(lista_fecha[2])>=22:
        return True
    elif int(lista_fecha[1])==12 and int(lista_fecha[2])<=21:
        return True
    else: return False

is_sagitario(cadena)

#%% 10
'''El cifrado César es un tipo de cifrado de mensajes que se basa en intercambiar 
unas letras por otras, según un desplazamiento, como se muestra en la figura a continuación:

Caesar's Cipher
En este cifrado, se toman todas las letras que se van a utilizar, por ejemplo, 
de la A a la Z y de la a a la z. Luego, se define una rotación, un número que utilizaremos 
para desplazar cada letra, por ejemplo, en la figura es 3. De ese modo, 
la A se convertirá en una D, la B en E, la C en F, la X en A, la Y en B y la Z en C.

Implemente dos funciones, una para cifrar y una para descifrar un mensaje. 
Para probar el funcionamiento, considere que decipher(cipher(msg)) devuelve el 
mensaje original. La siguiente tabla contiene ejemplos de cifrados.'''
# A = 65    Z = 90      a = 97    z = 122
n=int(input('n: '))
mensaje = list(input("mensaje: "))
def cipher(n:int,cadena:str)->str:
    '''     '''
    mensaje = list(cadena)
    for i in range(len(mensaje)):
        mensaje[i] = ord(mensaje[i])
        if mensaje[i]<91 and mensaje[i]+n>90:
            mensaje[i] = chr(mensaje[i]+n-26)
        elif 97<=mensaje[i]<=122 and mensaje[i]+n>122:
            mensaje[i] = chr(mensaje[i]+n-26)
        else: mensaje[i] = chr(mensaje[i]+n)   
    texto = ''
    for letra in mensaje:
        texto+=letra
    return texto  

def decipher(n:int, cadena:str)->str:
    '''     '''
    mensaje = list(cadena)
    for i in range(len(mensaje)):
        mensaje[i] = ord(mensaje[i])
        if mensaje[i]<91 and mensaje[i]-n<65:
            mensaje[i] = chr(mensaje[i]-n+26)
        elif 97<=mensaje[i]<=122 and mensaje[i]+n<97:
            mensaje[i] = chr(mensaje[i]-n+26)
        else: mensaje[i] = chr(mensaje[i]-n)   
    texto = ''
    for letra in mensaje:
        texto+=letra
    return texto
decipher(n,cipher(n,mensaje))

#%% 10 rehecho
n=int(input('n: '))
mensaje = list(input("mensaje: "))
def cipher(n:int,cadena:str)->str:
    for i,letra in enumerate(cadena):
        if letra.isupper():
            num_letra = ord(letra)-ord('A')
            num_letra = (num_letra + n)%26 #el resto es cuanto me muevo desde la 'A'
            mensaje[i] = chr(ord('A') + num_letra)
        elif letra.islower():
            num_letra = ord(letra)-ord('a')
            num_letra = (num_letra + n)%26 #el resto es cuanto me muevo desde la 'A'
            mensaje[i] = chr(ord('a') + num_letra)
    texto = ''
    for letra in mensaje:
        texto+=letra
    return texto
cipher(n,mensaje)
#%% 11 HACER!!!!
'''Escribir una función que permita determinar si una cadena podría formar una palabra, 
del siguiente modo: el carácter ??? sirve de comodín para cualquier letra, 
mientras que sea 1 (una) letra, por lo que ??oca? puede formar la palabra ?poca?, 
también la palabra ?boca?, o ?roca?. La palabra ??? puede formar cualquier cadena de largo 1, 
mientras que ??o?a? puede formar ?poca?, ?bota?, ?rosa?, etc.

La función debe cumplir el siguiente prototipo:'''

def matches(base: str, word: str) -> bool:
    '''     '''
    reemplazos = ['r','t','p','c','b','s','l']
    
        

# complete me
'''El siguiente código debe funcionar sin errores con la función desarrollada:'''

def test_matches():
    if matches("?", ""):
        return False
    if not matches("?", "a"):
        return False
    if matches("?", "aa"):
        return False
    if matches("x", "a"):
        return False
    if not matches("?o?a", "rota"):
        return False
    if not matches("?o?a", "poca"):
        return False
    if not matches("?o?a", "bota"):
        return False
    if not matches("?o?a", "sola"):
        return False
    if not matches("?o?a", "cosa"):
        return False
    if matches("?osa", "rota"):
        return False
    if matches("?ola", "poca"):
        return False
    if matches("co?a", "bota"):
        return False
    if matches("mo?a", "sola"):
        return False
    if matches("so?a", "cosa"):
        return False

if test_matches() is False:
    print("Esto no funciona")
#%% 12
'''Implementar una función que dadas 2 secuencias recibidas como argumento retorne los 
índices de cada una de ellas a partir de los cuales se obtiene la subsecuencia en común 
de mayor longitud, y retorne también la longitud de dicha secuencia. 
Por ejemplo, las cadenas:
"TAGGTTAATGGGCCATTTTCGGCACCCTAGGTAGCTTATT", y
"ACCATACTATGGTTTTTCCTAAGCGATTGGCATTTTCTTG"
tienen un solapamiento máximo de 7 caracteres, como se muestra a continuación:
                 TAGGTTAATGGGCCATTTTCGGCACCCTAGGTAGCTTATT
ACCATACTATGGTTTTTCCTAAGCGATTGGCATTTTCTTG
                              ^^^^^^^
Mientras que las cadenas:
"TACCAGTCTATGTCATCCAGGGTAGCTGTTTGATTGTCCC", y
"CGAACGGAGAAAGTTAGCATTCCCAGTTGTCGGGTCTACG"
tienen un solapamiento máximo de 5 caracteres:

                    TACCAGTCTATGTCATCCAGGGTAGCTGTTTGATTGTCCC
CGAACGGAGAAAGTTAGCATTCCCAGTTGTCGGGTCTACG
                      ^^^^^'''
def solapamiento(cadena1:str,cadena2:str)->tuple:

    coincidencia = ''
    for i1 in range(len(cadena1)):
        for i2 in range(len(cadena2)):
            largo = 0

            while (i1+largo<len(cadena1)) and (i2+largo<len(cadena2)) and (cadena1[i1+largo] == cadena2[i2+largo]):
                largo +=1
                
            if len(cadena1[i1:i1+largo])>len(coincidencia):
                coincidencia = cadena1[i1:i1+largo] 

    return coincidencia, cadena1.find(coincidencia) ,cadena2.find(coincidencia)
solapamiento("TACCAGTCTATGTCATCCAGGGTAGCTGTTTGATTGTCCC","CGAACGGAGAAAGTTAGCATTCCCAGTTGTCGGGTCTACG")  


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
def longest_common_substring(s1: str, s2: str) -> tuple[int, int, int]:
    """
    It checks the longest common substring between two strings.

    Parameters
    ----------
    s1 : str
        First string.
    s2 : str
        Second string.

    Returns
    -------
    start1 : int
        Start index of the first string.
    start2 : int
        Start index of the second string.
    length : int
        Length of the longest common substring.
    """
    max_start1 = -1
    max_start2 = -1
    max_length = 0
    for start1 in range(len(s1)):
        for start2 in range(len(s2)):
            length = 0
            # Tengo que chequear que no me pase de los límites de las cadenas, y después que los caracteres sean iguales
            while ((start1 + length < len(s1)) and (start2 + length < len(s2)) and (s1[start1 + length] == s2[start2 + length])):
                length += 1
            
            if length > max_length:
                max_length = length
                max_start1 = start1
                max_start2 = start2

    return max_start1, max_start2, max_length

def main():
    s1 = "TAGGTTAATGGGCCATTTTCGGCACCCTAGGTAGCTTATT"
    s2 = "ACCATACTATGGTTTTTCCTAAGCGATTGGCATTTTCTTG"

    start1, start2, length = longest_common_substring(s1, s2)
    print(start1, start2, length)

if __name__ == "__main__":
    main()

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

#%%
def print_names2(people):
    """Print a list of people's names, which each person's name
       is itself a list of names (first name, second name etc)
    """
    
    count = 0
    while count < len(people):
        to_print = ""
        count2 = 0
        while count2 < len(people[count]):
            to_print += people[count][count2]+' '
            count2 +=1
        count +=1
        print(to_print)
print_names2([['John', 'Smith'], ['Mary', 'Keyes'], ['Jane', 'Doe']])
# %%
puntaje=[0,0]
matchpoint = 0
while matchpoint == 0:
    entrada = int(input("jugador que gano: 1/2"))
    puntaje[entrada-1] += 1
    print(puntaje[0],puntaje[1])
    if puntaje[0]==4 or puntaje[1]==4:
        matchpoint += 1
        print(puntaje[0],puntaje[1])
while matchpoint == 1:
    if (puntaje[0]-puntaje[1])%1 == 0:
        entrada = int(input("jugador que gano: 1/2"))
        puntaje[entrada-1] += 1
    elif (puntaje[0]-puntaje[1])%1 > 0:
        entrada = int(input("jugador que gano: 1/2"))
        puntaje[entrada-1] += 1
        matchpoint +=1
if matchpoint == 2:
    print(f'Ganador: jugador {puntaje.find(max(puntaje))+1}')
        

#%%

# %%
ppp = [1,2]
print(ppp[0],ppp[1])
# %%
-3%4
# %%

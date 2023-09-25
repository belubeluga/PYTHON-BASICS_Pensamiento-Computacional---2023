#%% 1
'''Escriba una función, llamada less, que reciba un archivo e imprima su contenido.'''
def less(archivo:str): 
    with open (archivo, 'r') as f:
       return f.read()

print(less('archivo.txt'))
# %% 2
'''Escriba una función, llamada head, 
que reciba un archivo y un número N e imprima las primeras N líneas.'''
def head(archivo:str, N:int)->list:
    ''' '''
    with open(archivo) as f:
            lineas = f.readlines()
    return lineas[:N:]
      
head('archivo.txt', 3)

# %% 3
'''Escriba una función, llamada tail, que reciba un archivo 
y un número N e imprima las últimas N líneas.'''
def tail(archivo, N:int):
    with open(archivo) as f:
        lista = f.read().split('\n')[-N::1]
        return lista #como hacer que se imprima el texto solo
tail('archivo.txt',2)

# %% 4
'''Escribir una función, llamada touch, 
que reciba el nombre de un archivo a guardar, 
y genere un archivo de texto vacío.'''

def touch(nombre:str):
    archivo = open(nombre, 'w')
    archivo.close()

touch('archivo.prueba2.txt')

# %% 5
'''Escribir una función, llamada cp, que copie 
todo el contenido de un archivo a otro, 
de modo que quede exactamente igual.'''
def cp(nombre1:str, nombre2:str):
    archivo = open(nombre1)
    with open (nombre2, 'w') as f:
        for linea in archivo: f.write(linea)

cp('archivo.txt','archivo.prueba.txt')

# %% 6
'''Escribir una función, llamada wc, que dado un archivo de texto, 
lo procese e imprima por pantalla cuántas líneas, cuántas palabras, 
cuántos caracteres contiene el archivo, y el nombre del archivo.

Ejemplo:
> wc('file.txt')
> 9 21 243 file.txt'''

def wc(archivo:str):
    contenido = open(archivo).read()
    return len(contenido.split('\n')), len(contenido.split()),len(contenido),archivo
wc('archivo.prueba.txt')

# %% 7
'''Escribir una función, llamada grep, que reciba una cadena y un archivo, 
e imprima las líneas del archivo que contienen esa cadena.'''
def grep(cadena:str, archivo:str)->str:
    contenido = open(archivo).read().split()
    return [linea for linea in contenido if cadena in linea]

grep('s', 'archivo.prueba.txt')

# %% 8
'''Escribir una función, llamada cat, que reciba dos cadenas referidas 
a los nombres de dos archivos, y guarde en un tercer archivo 
el contenido de los dos archivos, concatenado.'''

def cat(nombre1:str, nombre2:str):
    archivo1 = open (nombre1).read()
    archivo2 = open(nombre2).read()
    archivo_final = open('archivo_final','w')
    archivo_final.write(archivo1+'\n'+archivo2)


cat('archivo.txt', 'archivo.prueba.txt')

# %% 9 ???????????

'''Escribir una función, llamada rot13, que reciba un archivo de texto de origen 
y uno de destino, de modo que para cada línea del archivo origen, 
se guarde una línea cifrada en el archivo destino. 
El algoritmo de cifrado a utilizar será muy sencillo: a cada caracter comprendido 
entre la a y la z (del alfabeto inglés), se le suma 13 y luego se aplica el módulo 26, 
para obtener un nuevo caracter.'''

def rot123(origen:str, destino:str):
    archivo_origen = open(origen).read().split()
    archivo_destino = open(destino, 'w')
    for palabra in archivo_origen:
        archivo_destino.write(' '.join([chr(ord(caracter)+13) for caracter in palabra \
                               if caracter.isalpha()]))

rot123('archivo_final', 'archivo.txt')
# %%
for letra in 'u | y n { |q |   r p  n   |p v { p | r v ':
    print(chr(ord(letra)-13))

# %% 10
'''Escribir una función load_data que reciba un nombre de archivo, 
cuyo contenido tiene el formato key:value, 
y devuelva un diccionario con el primer campo como clave y el segundo como diccionario.'''

def load_data(nombre:str):
    ''' '''
load_data('diccionario.txt')
# %%
'''def load_data(archivo:str):
    r = open(archivo).read()
    archivo_nuevo1 = open('archivo_nuevo1','w')
    archivo_nuevo2 = open('archivo_nuevo2','w')
    archivo_nuevo1.write(dict(';'.join(r).keys()))
    archivo_nuevo2.write(dict(';'.join(r)).values())
load_data('diccionario.txt')'''
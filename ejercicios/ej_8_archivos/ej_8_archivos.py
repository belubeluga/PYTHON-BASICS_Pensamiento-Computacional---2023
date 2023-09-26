import math
#%% 1
'''Escriba una función, llamada less, que reciba un archivo e imprima su contenido.'''
def less(archivo:str): 
    with open (archivo, 'r') as f:
       return f.read()

print(less('dic.txt'))
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
    return [linea for linea in contenido if cadena in linea] #POR COMPRENSION

grep('s', 'archivo.prueba.txt')

# %% 8
'''Escribir una función, llamada cat, que reciba dos cadenas referidas 
a los nombres de dos archivos, y guarde en un tercer archivo 
el contenido de los dos archivos, concatenado.'''

def cat(nombre1:str, nombre2:str)->None: #typeskin!!!
    archivo1 = open(nombre1).read()
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
    archivo_destino = open(destino, 'w') #ACLARAR W PARA ESCRIBIR
    for palabra in archivo_origen:
        archivo_destino.write(' '.join([chr(ord(caracter)+13) for caracter in palabra \
                               if caracter.isalpha()]))

rot123('archivo_final', 'archivo.txt')

# %% 10
'''Escribir una función load_data que reciba un nombre de archivo, 
cuyo contenido tiene el formato key:value, 
y devuelva un diccionario con el primer campo como clave y el segundo como diccionario.'''

def load_data(nombre:str):
    ''' '''
    archivo = open(nombre)
    dic = {}
    for linea in archivo:
        elementos = linea.split(':')
        dic[elementos[0]] = elementos[1] #agregar a diccionario
    archivo.close()
    return dic
load_data('diccionario.txt')

# %% 11
'''Escribir una función save_data que reciba un diccionario y un nombre de archivo, 
y guarde el contenido del diccionario en el archivo, con el formato key:value.'''
def save_data(dic:dict, nombre:str)->None:
    ''' '''
    with open(nombre, 'w') as f:
        f.write(str(dic)) #lo de adentro del write tiene que ser STR!!!
diccionario = {'hola':1,
               2: "hola",
               'chau':3}
save_data(diccionario, 'dic.txt')

#%% 12
'''Escribir una función, llamada sed, que reciba el nombre de un archivo, y dos cadenas. 
La primera cadena en el archivo es la que queremos reemplazar por la segunda.'''
#??????? que reciba una cadena y 
def sed(archivo:str, cadena1:str, cadena2:str): #cadena es string???
    ''' '''

    Lectura = open(archivo) #solo para leer
    if str(cadena1) in Lectura.read(): #STR!!! SI BUSCO QUE ALGO ADENTRO DEL ARCHIVO 
        Lectura.close()
        Archivo = open(archivo, 'w') #xq aca quiero que escriba desde el principio borrando todo, habiendolo leido antes
        Archivo.write(str(cadena2))
        Archivo.close()

diccionario = {'hola':1,
               2: "hola",
               'chau':3}
sed('dic.txt', diccionario, 'holahola')        
    
#%% 13
'''Un archivo CSV (Comma Separated Value) es un archivo de texto que, en cada línea,
almacena un registro. Cada registro está compuesto por campos. 
En el archivo, cada campo está separado por comas (,), de ahí el nombre. 
El siguiente texto es un ejemplo del contenido de un archivo con el mencionado formato:

First Name,Last Name,Country,Year of Birth
Emanuel,Ginobili,Argentina,1977
Donald,Trump,USA,1946
Carl,Gauss,Germany,1855

Escribir una función que reciba la información que se quiere escribir en un archivo en formato
CSV. Esta información tiene que estar estructurada en una secuencia de secuencias.
Ejemplo:
> info = [
  ["First Name","Last Name","Country","Year of Birth"],
  ["Emanuel","Ginobili","Argentina","1977"],
  ["Donald","Trump","USA","1946"],
  ["Carl","Gauss","Germany","1855"]
]'''

def formato_csv(*categorias:list)->None: #  VER DIFERENCIA ENTRE * Y **
    ''' '''         #*algo devuelve tuplas (**diccionarios)
    with open('archivonuevo.csv','x') as f:
        for lista in list(categorias):
            #for elemento in lista:
                #general.append(str(elemento))
                f.write(f"{','.join(lista)}\n") #OJO COMO FORMULAR XQ EL CURSOR NO HACE ENTER SOLO
            
formato_csv(['categoria 1', 'ganador'],['1','2'])

#%% 14
'''Un archivo TSV (Tab Separated Value) es un archivo, similar al CSV, 
que está escrito del siguiente modo:
    First Name\tLast Name\tCountry\Year of Birth
    Lewis\tHamilton\tUnited Kingdom\t1985
    Max\tVerstappen\tBelgium\t1997
    Charles\tLeclerc\tMonaco\t1997
Donde cada espacio es un caracter tabular ('\t'); 
en ASCII es el código 09 (distinto al caracter espacio).

Escribir una función que reciba la información que se quiere escribir en un archivo 
en formato TSV. Esta información tiene que estar estructurada en una secuencia de secuencias.
'''

def funcion_tsv(categorias:list)->None:
    with open('archivonuevo.tsv','x') as f:
        for lista in categorias:
            f.write(f"{','.join(lista)}\n") #transformarlo en lista!!!

funcion_tsv([
  ["First Name","Last Name","Country","Date of Birth"],
  ["Lewis","Hamilton","United Kingdom","1985"],
  ["Max","Verstappen","Belgium","1997"],
  ["Charles","Leclerc","Monaco","1997"]
])

#%% 15

'''Dado dos archivos en formato CSV, dinosaurs1.csv y dinosaurs2.csv, 
escribir un programa que lea los dos archivos guardados en disco, 
y luego imprima los nombres de los dinosaurios bípedos, 
desde el más lento al más rápido.'''
dino1 = open('dinasours1.csv')
dino2 = open('dinasours2.csv')



g = 9.8 # gravity constant
#velocity = ((list(dino2[1]) / list(dino1(1))) - 1) * math.sqrt(list(dino1(1)) * g)

#%% 16

#%% pruebas

def formato_csv(**categorias)->None: #  VER DIFERENCIA ENTRE * Y **
    ''' '''
    dic = {}
    for key,value in categorias.items():#PARENTESIS
        dic[key] = value
    return dic
formato_csv(categoria='juegos', ganador='yo')
# %%

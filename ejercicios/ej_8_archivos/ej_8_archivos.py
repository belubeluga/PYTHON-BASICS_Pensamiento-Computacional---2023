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
        dic[elementos[0]] = elementos[1].strip() #agregar a diccionario
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

#%% 15 TERMINAR!!!!!!!!

'''Dado dos archivos en formato CSV, dinosaurs1.csv y dinosaurs2.csv, 
escribir un programa que lea los dos archivos guardados en disco, 
y luego imprima los nombres de los dinosaurios bípedos, 
desde el más lento al más rápido.'''
dino1 = open('dinasours1.csv')
dino2 = open('dinasours2.csv')
lista1 = [elemento.split(',') for elemento in list(dino1)]

for i, linea in enumerate(lista1,1):
    dic = {}
    dic = {(str(lista1[0][0])+str(i)):linea[0],
           (lista1[0][1]+str(i)):linea[1],
           (lista1[0][2]+str(i)):linea[2],}

print(dic)
#print(lista1)
g = 9.8 # gravity constant
#velocity = ((list(dino2[1]) / list(dino1(1))) - 1) * math.sqrt(list(dino1(1)) * g)

#%% 16
'''Dado un archivo en formato CSV, que contiene canciones (nombre, duración, artista), 
escribir un programa que lea el archivo e imprima por pantalla la lista con el 
siguiente formato.
+----------------------------+------+-----------------+
| Name                       | Time | Artist          |
+----------------------------+------+-----------------+
| Candy Shop                 | 3:45 | 50 Cent         |
| In Da Club                 | 3:13 | 50 Cent         |
| What Up Gangsta            | 2:58 | 50 Cent         |
| In The Night Of Wilderness | 5:26 | Blackmill       |
| Wicked                     | 2:53 | Future          |
| Cudi Montage               | 3:16 | KIDS SEE GHOSTS |
| Cellular                   | 2:58 | King Krule      |
| Pull Up                    | 3:35 | Playboi Carti   |
| The Birthday Party         | 4:45 | The 1975        |
| One                        | 4:36 | U2              |
+----------------------------+------+-----------------+     '''
musica = open('musica.csv')
lista_musica = [linea.rstrip().split(',') for linea in list(musica)] 
    #rstrip cuando leo archivos x el \n                  lista de lineas
    #y el split para tener lista de listas
print('+----------------------------+------+-----------------+')
print('| Name                       | Time | Artist          |')
print('+----------------------------+------+-----------------+')
for i,linea in enumerate(lista_musica,0):
    print(f'| {lista_musica[i][0]}{(27-len(lista_musica[i][0]))*(" ")}| {lista_musica[i][1]}{(5-len(lista_musica[i][1]))*" "}| {lista_musica[i][2]}{(16-len(lista_musica[i][2]))*" "}|')
print('+----------------------------+------+-----------------+')

#%% 17 ?????? No lo puedo convertir a dict
'''Un archivo en formato JSON, es un archivo de texto, 
pero que su contenido está escrito del siguiente modo:
    {"id": 22264,
    "name": "Jack",
    "last_name": "Hunt",
    "age": 38,
    "children": false,
    "siblings": "Jessica Hunt, Robin Hunt",
    "ssn": "1234-99-0012"}
Tiene el mismo formato que un diccionario de Python, 
pero esta escrito en un archivo de texto.

Escribir una función que lea el archivo en formato JSON, 
y transforme el contenido a un diccionario de Python. 
Imprimir el diccionario por pantalla.'''
def JASON(nombreJSON:str)->dict:
    texto = open(nombreJSON).read().split('\n')
    lista_linea = ''
    for linea in texto:
        lista_linea += linea.strip()
    return dict(lista_linea)
JASON('17.JSON')

#%% 18
'''Tenemos un archivo que contiene, en cada línea del mismo, 
los siguientes datos separados por '\t': continente, país, ciudad, 
y cantidad de habitantes.

Escribir una función que lea el archivo y devuelva los datos 
cargados en una lista.'''

def lectura_tab(archivo:str)->list:
    with open(archivo) as f: #acordarse del strip abajo!!!!! por los \n
        elementos = [linea.strip().split(maxsplit=3) for linea in f.readlines()]

    return elementos
'''Escribir un programa que solicite al usuario el nombre de un 
archivo como el descripto y una cantidad de habitantes y guarde, 
en un nuevo archivo, los datos de todas las ciudades 
que tengan más habitantes que los ingresados por el usuario.'''
nombre_archivo = input('nombre de archivo: ')
cantidad_habitantes = int(input('cantidad_habitantes: '))
lista = [linea for linea in lectura_tab(nombre_archivo) if int(linea[-1])>cantidad_habitantes]
print(lista) #en vez de guardarlos en un nuevo archivo los imprime

#%% 19
'''Tenemos una colección de libros en un único archivo de texto. 
Esta colección pertenece al mismo autor, y queremos escribir un 
programa para conocer las palabras favoritas o, 
al menos, las más utilizadas por esta persona.
Para ello: escribir una función que reciba el nombre de un archivo 
(que ya ha sido parcialmente procesado y sólo contiene oraciones, 
sin signos de puntuación), lo lea, y devuelva un diccionario con 
la cantidad de ocurrencias de cada palabra.'''

def repeticiones(archivo:str):
    with open(archivo) as f:
        palabras = [palabra for palabra in f.read().split()]
        dic = {palabra:(palabras.count(palabra)) for palabra in palabras}
                            #lista.count(elemento)
    return dic

repeticiones('archivolibro.txt')
#%% 19 b (como optimizar?????)
'''escribir una función que recibe dicho diccionario y devuelve 
las 10 (yo uso 3) palabras con mayor frecuencia (y sus ocurrencias).'''
dictionary = {'hakuna': 1, 'matata': 4, 'hola': 1, 'si': 3, 'Y': 1, 'y': 4, 'h': 7}

def muy_repe(diccionario:dict)->list:
    '''     '''    
    maximo = []
    valores = list(diccionario.values())
    while len(maximo) < 3:
        maximo += [max(valores)] #valor maximo
        valores.remove(maximo[-1])

    maximos = [] #maximos en items
    items = diccionario.items()
    for tupla in items:
        if tupla[1] in maximo:
            maximos.append(tupla)
    return maximos

muy_repe(dictionary)
#%% 19 c
'''escribir una función que recibe el nombre de un archivo y el 
resultado de la función anterior, y guarda cada palabra con su 
cantidad de ocurrencias en un archivo de texto, un par 
'palabra:ocurrencias' por línea.'''
def pares_ocurrencias(lista:list)->None:
    with open('archivonuevo_pares', 'x') as f:
        for linea in lista:
            f.write(f'{linea[0]}:{linea[1]}\n') #IMPORTANTE \N
lista_de_listas = [('matata', 4), ('y', 4), ('h', 7)]
pares_ocurrencias(lista_de_listas) 

#%% 20
'''Una casa tiene, entre otras cosas, aberturas, 
entre las cuales nos interesan: ventanas, puertas y tragaluces. 
Cada abertura tiene dos estados posibles, abierto o cerrado. 
A nosotros nos interesa generar algún tipo de resumen que permita 
conocer el estado general de la casa, es decir, 
si está completamente cerrada o si hay alguna abertura abierta 
(en cuyo caso querríamos saber a qué grupo o grupos pertenecen estas 
aberturas).
Se pide:
escribir una función resumen_aberturas que, 
a partir de un diccionario con la información de cada una de las 
aberturas, nos permita generar un archivo de texto que indique 
si la casa está completamente cerrada o no. Si la casa no está 
cerrada, se debe agregar un listado de las aberturas abiertas. 
Un True asociado a una clave del diccionario implica que la 
abertura en cuestión (una clave del diccionario) está cerrada, 
mientras que un False implica lo contrario.'''
#ventanas, puertas, tragaluces
#estado = 'abierto'

def resumen_aberturas(diccionario:dict)->str:
    '''     '''
    elemento_estado = diccionario.items()
    estados = [int(elemento[1]) for elemento in elemento_estado]
    if sum(estados)<len(estados):
        abiertos = [clave[0] for clave in elemento_estado if int(clave[1]) == 0]
        texto = ''
        for i in range (len(abiertos)):
            texto += f'* {abiertos[i]}\n'
        return f'Algo abierto.\n{texto}'
    else: return 'cerrado!\n'

casa1 = {'ventana': True,
         'puerta': True,
         'balcon': False}
print(resumen_aberturas(casa1))

casa2 = {'ventana': True,
         'puerta': True,
         'balcon': True}
print(resumen_aberturas(casa2))

casa3 = estado_casa = {'ventanas': True, 'puertas': True, 'tragaluces': True}
print(resumen_aberturas(casa3))

casa4 = estado_casa = {'ventanas': False, 'puertas': True, 'tragaluces': False}
print(resumen_aberturas(casa4))
#%% pruebas

def formato_csv(**categorias)->None: #  VER DIFERENCIA ENTRE * Y **
    ''' '''
    dic = {}
    for key,value in categorias.items():#PARENTESIS
        dic[key] = value
    return dic
formato_csv(categoria='juegos', ganador='yo')
# %%
dict({"id": 22264,
"name": "Jack",
"last_name": "Hunt",
"age": 38,
"children": False,
"siblings": "Jessica Hunt, Robin Hunt",
"ssn": "1234-99-0012"})
# %%

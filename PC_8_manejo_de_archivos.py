# 11/9

# CODIGO ASCII
# UNICODE --> incluye TODOS los caracteres
ord() #-->convierte valor a unicode
chr() #-->viceversa

# ARCHIVOS: secuencia de datos almacenados en la memoria
    # TEXTO PLANO: SOLO caracteres unicode (sin info extra, solo 1 y 0)
        # ej, txt, .py, CSV (para agrupar datos)
    # BINARIOS: cualquier cosa guardada en la compu con 0 y 1 (beats)
'''importante para el parcial'''

# apertura de archivos
f = open("file.txt", mode="r") #r y texto por default
linea = f.readline() #--> str \n
lineas = f.readlines()
#lineas = 'linea1 \n linea2 \n ...'

'''                 LECTURA     ESCRIBIR    SI NO EXISTE    SI EXISTE
r = read                si          no             error    desde el inicio
w = write               no          si           lo crea    BORRA
a = append              no          si           lo crea    añade al final
x = create              no          si           lo crea    Error
r+ = lect + escr        si          si             Error    desde el inicio
w+ = lect + escr        si          si           lo crea    BORRA (trunca)
a+ = lect + añadidura   si          si           lo crea    añade al final
x+ = lect + escr        si          si           lo crea    error
b = binario
t = texto
+ = r+w
'''
#../ r = -> atras
# OJO CON COMO SE MUEVE EL CURSOR AL LEER LINEAS (ej con breaks)

# cierre de archivos
f.close() # los cambios no se guardan hasta que se cierre
#%%
archivo = open('nombre.txt', 'rt') #read y texto
linea = archivo.readline()
n = 5 # largo maximo de la linea
while linea != '': #mientras no llegue al final
         # hacer algo con la línea
         print(f"Línea con {n} caracteres maximo: {linea}") #x default pone /n
         linea = archivo.readline(n)
archivo.close() #guardo
# %%

# STRIP LSTRIP RSTRIP
cadena1 = '(que esta pasando?'
print(cadena1.strip("())?")) #extremos  # que esta pasando
print(cadena1.rstrip('(?)')) #derecha   # (que esta pasando
print(cadena1.lstrip('(?'))  #izq       # que esta pasando?
#frena al encontrar uno que no esta (siempre por los costados, en el medio no)
print(cadena1.strip()) #x default borra cualquier caracter no imprimible
# %%

# ITERAR ARCHIVOA (lineas)
archivo = open('nombre.txt', 'rt')
for linea in archivo:
    print(f'linea: {linea}')
archivo.close()

# o crear lista de lineas
archivo = open('nombre.txt', 'rt')
lista_de_lineas = archivo.readlines()
archivo.close()

# OPERADOR DE CONTEXTO
with open('nombre.txt', 'rt') as archivo:
       '''hacer algo con el archivo'''
#aca ya esta automaticamente cerrado el archivo
#%%
with open('nombre.txt', 'rt') as archivo: #archivo es el objeto
       for i, linea in enumerate(archivo, 1):
           linea = linea.rstrip('\n') #saco el \n del print
           print(f"{i}: {linea}")
# %%
# ESCRITURA DE ARCHIVOS DE TEXTO
f = open('archivo.txt', 'w')
f.write("cadena1\n") #salto de linea porque sino el cursor se queda ahi y sigue escribiendo desde alla
f.write("cadena2\n")
'''
cadena1
cadena2
'''
lista_str = ['lista\n', 'de\n', 'lineas\n'] #IMP EL \N
f.writelines(lista_str) #Escribe en el archivo las cadenas pasadas como lista de strings (hay que agregar a mano '\n' al final). Es similar a invocar .write() múltiples vece

#%%
with open('numerar.py', 'wt') as dest:
      dest.write("with open ('numerar.py','rt') as archivo:\n")
      dest.write("    for i, linea in enumerate(archivo, 1):\n")
      dest.write("        print(f'{i}: {linea}', end='')\n")

# %%

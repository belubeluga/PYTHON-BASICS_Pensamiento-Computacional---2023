#%%
'''Escriba una programa que lea archivo.txt y guarde en otro archivo, tabla.csv,
una tabla donde la primer columna sean las palabras presentes (sin repetir) en el archivo
original y la segunda columna con la cantidad de veces que se repite cada palabra.
No deben incluirse como parte de la palabra signos de puntuacion 9, . ; : -).'''
archivo = open('archivo.txt')
texto = [linea for linea in archivo.read()]
archivo.close()
repeticiones = []
with open('tabla.csv', 'a+') as f:
    for palabra in texto:
        if palabra.strip() not in repeticiones:
            repeticiones += palabra.strip()
        for palabra in repeticiones:
            f.write((palabra,texto.count(palabra)))

#%%
def contacts(*dato:tuple):
    '''     '''
    agenda = []
    final = []
    for n in range(len(dato)):
        if n%2==0:
            if dato[n]=='add':
                agenda.append((dato[n+1]))
                final.append(f'{dato[n+1]} agregado')
            if dato[n]=='find':
                apariciones = 0
                for elemento in agenda:
                    if dato[n+1] in elemento:
                        apariciones += 1
                    final += apariciones
    return final            
        
print(contacts('add', 'hola', 'add','holanda'))

#%%
'''Ejercicio 3#

Se necesita implementar una función que muestre en pantalla una pregunta con sus opciones 
y permita que el usuario ingrese la opción elegida. La función debe retornar la opción 
ingresada por el usuario. Para ello se dispone de un diccionario con toda la información 
necesaria para esa pregunta: el enunciado de la pregunta, las opciones a mostrar y 
la respuesta correcta a cada pregunta. Por ejemplo:

Implemente una función quiz(question: dict) -> str:, 
donde question es la estructura de la pregunta que se quiere mostrar. 
Considere que el número de opciones puede ser variable (es decir no siempre serán 4 opciones). 
La salida por consola debe verse como en el siguiente ejemplo 
(> es el prompt que indica la espera del ingreso de una opción):

output:

¿En que año el hombre llegó a la luna?
1. 1959
2. 1797
3. 1969
4. 1979
>'''

def quiz(question:dict)->str:
    '''
    ¿En que año el hombre llegó a la luna?
    1. 1959
    2. 1797
    3. 1969
    4. 1979
    '''
    
    print(question['enunciado'])
    for opcion,rta in question['opciones'].items():
        print(f"{opcion}. {rta}")
    return input('>')

pregunta = {'enunciado': '¿En que año el hombre llegó a la luna?',
            'opciones': {'1': '1959','2': '1787', '3': '1969', '4': '1979'},
            'respuesta': '3'}
print(quiz(pregunta))

#continuo
rta_ingresada = quiz(pregunta)
if rta_ingresada == pregunta['respuesta']:
    print('Correcto')
else: print('Incorrecto')''''''
# %%
def contandoMinas(campo):
    linea = len(campo)/2
    campo1 = campo[:len(campo)/2:]
    campo2 = campo[len(campo)/2::]
    for i1,elemento in enumerate(campo1):
        campo1[i1]=sum([-1 in campo1[i1-1], -1 in campo1[i1+1], -1 in campo2[i2-1],-1 in campo2[i2],-1 in campo2[i2+1]])
    for i2,elemento in enumerate(campo2):   
        campo1[i2]=sum([-1 in campo1[i2-1], -1 in campo1[i2+1], -1 in campo2[i1-1],-1 in campo2[i1],-1 in campo2[i1+1]])
    return campo1+campo2
# %%

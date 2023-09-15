# ERRORES
#error de sintaxis --> mensaje de error
#error semantico --> no genera excepcion
#error de ejecucion --> genera excepcion

#para que no se corte el programa:
    # TRY
try:
    '''lo q puede llegar a cortar el programa'''
except:
    '''en vez de cortar el programa (si falla) se ejecuta lo que dice aca'''

# VER APUNTE HACER EXCEPCIONES !!!

#ej
print('vamos a dividir x por y')
try:
    x = int(input('Ingrese numero x: '))
    y = int(input('ingrese numero y: '))
    print('Resultado: ',x/y)
except:
    print('Error')



'''                 REPASIO                 '''


    #dic.items() lo levanta como tuplas


#%%
# zip
#agarra uno de cada lista (de dos) y si uno tiene menos 'recorta' hasta el ultimo en el q ambos tenian data
lista1 = ['rojo', 'verde','azul']
lista2 = [1,2,3,4]
lista3 = zip(lista1,lista2) #--> te devuelve tuplas SOLOI TE AGRUPA LA INFO
#vos lo tenes que castear a lista para que te lo devuelva (como el enumerate)
print(list(lista3)) #para acceder a la data, o lo itero


# NO hacer return print
# cuando una lista pasa x una funcion QUEDA MODIFICADA
'''CUANDO ENVIO COSAS MUTABLES A UNA FUNCION, QUEDA MODIFICADA
con las no mutables no, xq se envia una copia'''


# ponerle docstring a solo 1
# PERO SI O SI EL TYPE
# la clave de dics puede ser cualquier cosa inmutable
#li = lista3.pop('clave si es un dic', 'error, no existe')
li = lista1.pop(2)
li
lista1
# %%
#puedo indexar infinitamente un str


#%% 
with open('nombre.txt', 'w+') as f:
    L = ['gato\n', 'perro\n']
    f.writelines(L)

    #EL PUNTERO QUEDO AL FINAL de lo q se escribio
    #si itero desde ahi no saco nada
    '''deberia volver a abrirlo'''

    f.seek(0) #o esto, mueve el cursor al byte especificado

    #w borra
    #r+ va reescribiendo
    #el a empieza desde el final

    #HACER EJERCICIOS TIPO PARCIAL

# TSV se separa por un \t
# CSV separa con comas

#%%
def archivo_tsv(lista:list):
    ''' no devuelve nada
    w, para crear'''
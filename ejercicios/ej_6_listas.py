#%% 1 listas
'''Programar una función que tome una lista de números y compute la suma de todos los números 
en la lista.'''
def sumador(lista:list)->int:
    total = 0
    for numero in lista:
        total += numero
    return total
sumador([1,2,3,4,5])
# %% 2 listas
'''Programar una función que elimine todas las ocurrencias de un cierto elemento en una lista.'''
def eliminar(lista:list)->list:
    while len(lista)>0:
        lista.remove(lista[0])
    return lista
eliminar([1,2,3,4,5])
# %% 3 listas
'''Programar una función que tome una lista y elimine todos los elementos duplicados.'''
def repes(lista:list):
    for elemento in lista:
        while(lista.count(elemento))>1:
            lista.remove(elemento)
    return lista
repes([2,2,1,4,5,5])
# %% 4 listas
'''Programar una función que tome dos listas y retorne True si las listas tienen por lo menos 
un elemento en común'''

def chequeo(lista1,lista2):
    if len([c for c in lista1 if c in lista2])>0:
        return True
    else: return False

chequeo([1,2,3],[4,1,5,6])

#%% 11 listas
temp_diarias = [15, 20, 21, 21, 21, 20, 17]
temp_diarias_copia = temp_diarias.copy()
temp_diarias_copia[2:4] = [22, 22]
print(temp_diarias)
#%% 12 listas
alumnos_legajo = (("Nicolas", 110405), ("Javier", 121402), ("Juan", 98407))
for i in range(1, 2):
    print(alumnos_legajo[i][1])

# %% 4 tuplas
'''Dadas tres listas: tps compuesta por tuplas con 3 floats, parcial que contiene números, 
y nombres que contiene cadenas, crear una nueva lista que contenga tuplas (nombre, valor), 
únicamente con los nombres para los que el promedio de tps y parcial da mayor o igual que 4, 
donde valor es el promedio. Puede asumir que las listas tienen todas igual longitud, 
que las tuplas de tps tienen todas igual longitud, y que los índices de las listas 
se encuentran asociados.

Por ejemplo, dadas:

tps que contiene las tuplas (1.2, 2.5, 3), (4, 5.7, 6), y (5, 4.1, 4).
parcial que contiene los valores 9, 5.2, y 1.
nombres que contiene los valores ?Ariel?, ?Dani?, ?Cami?.
El resultado debe ser [(?Dani?, 5.225)].'''

tps = [(1.2, 2.5, 3), (4, 5.7, 6), (5, 4.1, 4)]
parcial = [9, 5.2, 1]
nombres = ['Ariel','Dani','Cami']

for i in range(len(parcial)-1):
    tp_nota = tps[i][0]+tps[i][1]+tps[i][2]
    nota = (tp_nota + parcial[i])/4
    if nota >= 4:
        print((nombres[i], nota))
# %% 1 mix
'''El equipo de investigación de la facultad se encuentra trabajando sobre un problema 
de alineación de secuencias de ADN. Se detectó un nuevo virus que posiblemente tenga impacto 
en nuestro país y para poder saber como actuar frente a este debemos buscar si existe otro 
virus similar del cual ya se conozca un tratamiento viable. De encontrarlo, podríamos tener 
una potencial cura. Gracias a la base de datos mundial de secuenciación de ADN provista por 
NCBI, descargamos listado de sencuencias que debemos investigar. En pos de paralelizar el 
trabajo, se nos asigna la tarea de crear una función find_matches con las siguientes carácterísticas:

Recibe 3 argumentos: query de tipo string, threshold de tipo float y corpus de tipo iterable.
query representa la secuencia de ADN de la que queremos encontrar similares.
threshold es el porcentaje de similtud mínimos que queremos para considerar que existe un match.
corpus es un iterable que representa la colección de secuencias de ADN 
en la que queremos encontrar matches.
Devuelve una lista con todos los miembros del corpus que tienen un grado de similitud superior
a threshold.
El retorno de dicha función será una lista de tuplas, cada tupla contiene como primer 
elemento la secuencia encontrada y como segundo elemento el grado de similitud (0% a 100%).

Dado que el volúmen de información es grande debemos pensar en una solución eficiente.'''

def similitudes(cadena1:str,cadena2:str):

    coincidencia = ''
    for i1 in range(len(cadena1)):
        for i2 in range(len(cadena2)):
            largo = 0

            while (i1+largo<len(cadena1)) and (i2+largo<len(cadena2)) and (cadena1[i1+largo] == cadena2[i2+largo]):
                largo +=1
                
            if len(cadena1[i1:i1+largo])>len(coincidencia):
                coincidencia = cadena1[i1:i1+largo] 

    return coincidencia

def find_matches(query:str,threshold:float,corpus:list)->list:
    '''
    query: secuencia de ADN
    threshold: porcentaje de similtud mínimo
    corpus: lista donde buscarmos similitudes con query

    retorna:
    lista de tuplas con querys con grado_de_similitud > threshold
    ejemplo: [(query, grado_de_similitud)]
    '''
    for secuencia in corpus:
        grado_de_similitud = (len(similitudes(query,secuencia))/len(query))
        if grado_de_similitud >threshold:
            return secuencia,grado_de_similitud
query='abcd' 
threshold = 0.5
corpus = ['acsd','abc','bcad','scd']    
find_matches(query,threshold,corpus)

# %% 2 mix
'''Escribir un programa que reciba una lista de tuplas, siendo el primer elemento de cada 
tupla una acción (add o find) y el segundo elemento sea un string. El programa representa 
una agenda de contactos. Las acciones que nos envían se traducen en:

insertar el nuevo nombre en la agenda, y
encontrar todos los nombres que comiencen con el string.
El programa debe tener una función principal, contacts, que reciba la lista de tuplas y 
retorne una lista donde cada elemento es la cantidad matches que encuentra 
en cada operación de find.'''

def contacts(*dato:tuple):
    '''     '''
    agenda = []
    final = []
    for n in range(len(dato)):
        if n%2==0:
            if dato[n]=='add':
                agenda.append((dato[n+1]))
            elif dato[n]=='find':
                apariciones = 0
                for elemento in agenda:
                    if dato[n+1] in elemento:
                        apariciones += 1
                final.append(apariciones)
    if len(final)>0: return final 
        
contacts('add', 'hola', 'add','holanda','add','santi','find','ho','find','sa','add','sandra','find','se')
# %%

# %%

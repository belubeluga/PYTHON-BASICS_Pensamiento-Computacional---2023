#--------------------ALGORITMOS DE BUSQUEDA-------------------- 9/10
#find index in

#busqueda lineal:
def buscar(lista:list, target) -> int:
    """
    Obtener el menor índice en lista donde se encuentre target.
    Argumentos:
    lista (secuencia) -- secuencia donde buscar target
    target -- elemento a buscar en la lista
    Retorna -1 en caso de no encontrar el elemento.
    """
    for i in range(len(lista)):
        if lista[i] == target:
            return i
    return -1 

#busqueda lineal con corte:
        #(si esta ordenado)
'''Para todo i entre 0 y N (no inclusive): 
    si lista[i] es igual a target entonces:
        devolver i
    si lista[i] es mayor a target entonces: 
        devolver -1 
    devolver -1'''
#(si el el elemento es mayor al target y todavia no lo encontro, se corta) xq todos los que siguen tmb van a ser mayores
#NO busco hasta el final

#busqueda binaria
    #ir subdividiendo aprox a la mitad
'''izquierda <-- 0
    derecha <-- N - 1
    mientras izquierda sea menor o igual a derecha:
        medio <-- (izquierda + derecha)/2 (redondeado para abajo) 
        si lista[medio] es igual a target:
            devolver medio
        si target es mayor a lista[medio]:
            izquierda <-- medio + 1 
        sino:
            derecha <-- medio - 1 
    devolver -1'''
# defino dos variables (principio y final)
# busco medio (y redondeo para abajo)
    # si medio es igual a target, devuelvo medio
    # si no, redefino limites y vuelvo a calcular medio
        # si target > medio: izquierda = medio + 1
        # si target < medio: derecha = medio -1


# COMPLEJIDAD:
''' Analisis para T(N)
    k: largo de secuencia
    expresar k en funcion de N:
        N = 2^k ---> k = log2(N) '''
    #       T(N) --directamente proporcional--> log(N)


#-------------------- ALGORITMOS DE ORDENAMIENTO --------------------
#notacion Big-O 
    #costo temporal de nuestro algoritmo T(N)

'''conviene usarlo cuando vamos a hacer muchas busquedas (xq solo se ordena una vez)'''
#mientras mas busquedas, se diluye el costo del ordenamiento

#PROPIEDADES: se suma el Big-O del peor caso
#sumatoria de la cantidad de iteraciones

'''     Orden         Nombre
        -----------------------
        O(1)       |  constante
        O(log n)   |  logarítmica
        O(n)       |  lineal
        O(n log n) |  casi lineal
        O(n2)      |  cuadrática
        O(n3)      |  cúbica
        O(an)      |  exponencial
        O(n!)      |  factorial      '''

#VER EJEMPLOS!!!!! y como calcularlo matematicamente
n = input()
j=0
#a)
if n%2==0:      #complejidad = O(1)
    for i in range(n):
        print('par')
    else:
        print('impar')
#b)
for i in range(n):  #complejidad = O(n)
    if i%2==0:
        j += 2
    print(i,j)
#c)
for i in range(n):
    for j in range(n):  #complejidad = O(n**2)
        if i%2==0:
            print(i)
            print(j)
print(i+j)
#d)
for i in range(n):
    if i%2==0:      #complejidad = O(n**2)
        print(i)
for i in range(n):
    for k in range(n):
        print(k)
#e)
i=1
while i<n:   #complejidad = O(log(n))
    i*=2
    print(i)
#f)
for i in range(n):
    j=1
    while j<n:  #complejidad = O(n*log(n))
        j*=2
        print(j)
#%%
lista = [5,6,2,4,1,3] 
n = len(lista)
lista_nueva = []   
#ORDENAMIENTO POR SELECCION
for j in range(0,n-1): #(n-2 incluido) xq el ultimo no lo ordeno 
    #for k in range(j,n):#(n-1 incluido) k indica la sublista ->  complejidad =O(n**2) (xq depende del anterior)
        #chequear y guardar MIN de sublista
        #intercambiar minimo con inicio de lista sin ordenar -> complejidad = O(1)
    minimo = min(lista)
    lista_nueva+=[minimo]
    lista.remove(minimo)
#print(lista_nueva)
#%% implementacion codigo por seleccion
def selection_sort(lista):
    for j in range(len(lista)-1):
        i_minimo = j
        for k in range(j, len(lista)):
            if lista[k]<lista[i_minimo]:
                i_minimo = k
            k = j
        lista[i_minimo],lista[j] = lista[j],lista[i_minimo]    

lista = [4,5,8,72,3]
selection_sort(lista)
lista
#%%
#ORDENAMIENTO POR BURBUJEO
#implementacion bubble sort
def bubble_sort(lista):
    for j in range(1,len(lista)):
        for k in range(1, len(lista)-j+1):
            if lista[k]<lista[k-1]:
                lista[k-1],lista[k]=lista[k],lista[k-1]
lista = [4,5,8,72,3]
bubble_sort(lista)
lista
#%%
#INSERTION SORT
#%% implementacion algoritmo de insercion con lista de numeros
def insertion_sort(lista):
    for j in range(1,len(lista)):
        actual = lista[j]
        k = j
        while k > 0 and (lista[k-1]>actual):
            lista[k] = lista[k-1]
            k = k-1
        lista[k] = actual

lista = [4,5,8,72,3]
insertion_sort(lista)
print(lista)
#%%


# %% Problema 1
'''Generar una lista de números aleatorios. 
Luego, implementar el ordenamiento de la lista mediante una función que ordene por burbujeo. 
Ejemplo:
   lista = [2, 1, 5, 6, -4, 0]
   lista_ordenada = burbujeo(lista)
   print(lista)
   print(lista_ordenada)'''
lista = [7,6,9,8,4,5,2,1,0,-2,-8]

def burbujeo(lista):
    '''     '''
    n=len(lista)
    for j in range(1,n):
        for k in range(0,j):
            if lista[j]>=lista[k]:
               #quedan igual
               lista
            else: 
                lista[j],lista[k] = lista[k],lista[j]
    return lista                  
lista_ordenada = burbujeo(lista)
#print(lista_ordenada)
# %% Problema 2
'''Implementar una función busqueda_corte(numero, lista) que reciba una lista ?ordenada? 
de números enteros y busque en la lista la posición del número pasado por argumento. 
Si el número no se encuentra en la lista, debe retornar -1. Ejemplo:
lista = [-4, 0, 1, 2, 5, 6]
indice_numero = busqueda_corte(5, lista)
print(indice_numero)
indice_numero = busqueda_corte(8, lista)
print(indice_numero)'''
def busqueda_corte(numero,lista):
    '''     '''
    if numero in lista:
        return lista.index(numero)
    else: return -1
lista = [-4, 0, 1, 2, 5, 6]
indice_numero = busqueda_corte(5, lista)
#print(indice_numero)
indice_numero = busqueda_corte(8, lista)
#print(indice_numero)

#%% ejercicio 2 clase tutorial

def ordenar(lista,campo):
    if campo.lower() == 'puntos':
        index = 1
    elif campo.lower() == 'nombre':
        index = 0
    for j in range(1,len(lista)):
        for k in range(1, len(lista)-j+1):
            if lista[k][index]<lista[k-1][index]:
                lista[k-1],lista[k]=lista[k],lista[k-1]

lista = [['Mara', 47],['Matias',16],['Ines',14],['Tomas',12],['Joaquin',8],['Sebastian',48],['Belen',18]]
ordenar(lista,'Puntos')
lista
#%%
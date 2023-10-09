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

#PROPIEDADES: se suma el Big-O del peor caso

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

#VER EJEMPLOS!!!!!
n = input()
j=0

if n%2==0:      #complejidad = O(1)
    for i in range(n):
        print('par')
    else:
        print('impar')

for i in range(n):  #complejidad = O(n)
    if i%2==0:
        j += 2
    print(i,j)
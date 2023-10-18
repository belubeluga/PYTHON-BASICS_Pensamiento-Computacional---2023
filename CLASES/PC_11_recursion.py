#-------------------- RECURSION -------------------- 17/10

#caso recursivo
#caso base: donde termina la recursion

#algoritmicamente (divide y reinaras)
#semanticamente "llamarse a si mismo"

#stack frame (cuando la funcion finaliza, desaparece (en orden))    (ultimo en entrar primero en salir)


#%% ejemplo
def mult(a:int,b:int)->int:
    '''     '''
    if b==1:
        return a
    else:
        return a + mult(a,b-1)
    
mult(7,7)
# %% ejemplo fibonacci
def fibonacci(n):
    '''     '''
    if n == 0 or n == 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

fibonacci(15)
# %% MEMOIZATION    fibonacci con memoization
#Memoization: evitar tener q volver a hacer una recursion si ya la hice antes
def fibo (n, d) :
    if n in d:
        return d[n]
    else:
        d[n] = fibo (n-1,d) + fibo (n-2,d)
    return d[n]
d= {0:0, 1:1}
print(fibo (9, d))
print(d)

# %% suma Gauss
def suma_gauss(n):
    '''     '''
    if n < 1:
        return n
    else: return n + suma_gauss(n-1)

suma_gauss(7)
# %%
def power(a,b):
    if b == 1:
        return a
    else: 
        return a * power(a, b-1)
power(2,3)
# %% Convertir de decimal a binario
def convertir_binario(numero:int)->str:
    if numero>0: #o 1
        return convertir_binario(numero//2)+str(numero%2)
    else: return '' #y aca str(numero)
convertir_binario(12)
#%% "" en una linea
def convertir_binario(numero:int):return convertir_binario(numero//2)+str(numero%2) if numero>0 else ''
convertir_binario(12)
# %% ordenamiento x seleccion recursivo
def seleccion_recursiva(lista:list):
    if len(lista)<=1:
        return lista
    else: 
        minimo_idx = 0
        for i, elem in enumerate(lista):
            if elem<lista[minimo_idx]:
                minimo_idx = i
        lista[minimo_idx],lista[0]=lista[0],lista[minimo_idx]
        return [lista[0]]+seleccion_recursiva(lista[1:])

lista = [1,4,2,3]
print(seleccion_recursiva(lista))
# %% 
def seleccion_recursiva(lista:list):
    if len(lista)<=1:
        return lista
    else: 
        minimo = min(lista) #te hace un for
        minimo_idx = lista.index(minimo) #te hace otro
        lista[minimo_idx],lista[0]=lista[0],lista[minimo_idx]
        return [lista[0]]+seleccion_recursiva(lista[1:])
#x eso es mas rapido el anterior, pero ambos funcionan y == complejidad
lista = [1,4,2,3]
print(seleccion_recursiva(lista))
# %%

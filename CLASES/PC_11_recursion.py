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
def fibo (n, d) :
    if n in d:
        return d[n]
    else:
        print (f'f({n}) Recursión')
        d[n] = fibo (n-1,d) + fibo (n-2,d)
    return d[n]
d= {0:0, 1:1}
fibo (15, d)

# %% suma Gauss
def suma_gauss(n):
    '''     '''
    if n < 1:
        return n
    else: return n + suma_gauss(n-1)

suma_gauss(7)
# %%

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
    
mult(3,5)
# %%

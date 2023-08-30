from termcolor import colored, cprint
#estados alumnos en tiempo 0
a = int(input("alumnos despiertos en tiempo 0: ")) #despiertos 
c = int(input("alumnos cansados en tiempo 0: ")) #cansados 
s = int(input("alumnos dormidos en tiempo 0: ")) #dormidos 
total = a + c + s
#constantes 
w = float(input("tasa de despierte: "))#despierte
r = float(input("tasa de somnoliencia: ")) #somnoliencia
N = int(input("numero de minutos: "))

if (a<0) or (c<0) or (s<0) or (N<0):
    print("Error: El tiempo o la cantidad de alumnos no pueden ser negativos")
elif 1<r<0 or 1<w<0:
    print("Error: Las tasas deben ser numeros entre 0 y 1")
else:
    for t in range(0, N+1):  
        at = a + w*s
        if at < 0: a = 0
        else: a = round(at)
        
        ct = c - r*c*s
        if ct < 0: c = 0            #hago casos para evitar restar 15numeros negativos y que se sumen, alterando los numeros
        else: c = round(ct)
        
        st = total - round(a) - round(c)
        if st < 0: s = 0
        else: s = st
       
        cansados = colored(int(c)*'🀫', 'dark_grey')
        dormidos = colored(int(s)*'🀫', 'cyan')
        despiertos = colored(int(a)*'🀫', 'light_red')
        grafico = f'{t:2d} {cansados}{dormidos}{despiertos}    {(int(round(total)))}\r'
        print(grafico,)
    

# %%

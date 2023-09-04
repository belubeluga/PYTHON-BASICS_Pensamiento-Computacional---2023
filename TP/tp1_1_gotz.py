from termcolor import colored, cprint
#estados alumnos en tiempo 0 
c = int(input("alumnos cansados en tiempo 0: ")) #cansados -> gris
s = int(input("alumnos dormidos en tiempo 0: ")) #dormidos -> azul
a = int(input("alumnos despiertos en tiempo 0: ")) #despiertos -> rojo
total = a + c + s
#constantes 
w = float(input("tasa de despierte: ")) #despierte
r = float(input("tasa de somnoliencia: ")) #somnoliencia
N = int(input("numero de minutos: "))


if (a<0) or (c<0) or (s<0) or (N<0):    #casos de inputs invalidos
    print("Error: El tiempo o la cantidad de alumnos no pueden ser negativos")
elif 1<r<0 or 1<w<0:
    print("Error: Las tasas deben ser numeros entre 0 y 1")
else:
     for t in range(1, N+1):
            at = a + w*s
            if at < 0: at = 0 #porque no puede haber una cantidad negativa de alumnos despiertos

            ct = c - r*c*s
            if ct < 0: ct = 0 
            
            st = total - round(at) - round(ct) #para resolver problema de redondeo
            if st < 0: st = 0

            a = at
            c = ct
            s = st
            
            cansados = colored(int(round(c))*'🀫', 'dark_grey')
            dormidos = colored(int(round(s))*'🀫', 'cyan')
            despiertos = colored(int(round(a))*'🀫', 'light_red')
            grafico = f'{t:3d} {cansados}{dormidos}{despiertos}    {(int(round(total)))}\r'
            print(grafico)

w = 0
N = 100
a = 0
c = 46
s = 1
total = 47
r = 0.001 #0.001 = 1/1000 
while c>=1: #se ejecutan "vueltas" mientras no se llegue a que todos los alumnos esten dormidos
    r+=0.0001 #al comienzo de cada vuelta, aumento el valor de r
    a = 0
    c = 46
    s = 1  
    for t in range(0,N+1):
        at = a + w*s
        if at < 0: at = 0 #mismo codigo de antes

        ct = c - r*c*s
        if ct < 0: ct = 0 
            
        st = total - round(at) - round(ct) 
        if st < 0: st = 0

        a = at
        c = ct
        s = st

        if t == 100 and ct>=1: 
            continue #mientras no todos esten dormidos, se repite el ciclo, no se llego al max
        

print(round(r,4)) #se imprime el valor de r, redondeado
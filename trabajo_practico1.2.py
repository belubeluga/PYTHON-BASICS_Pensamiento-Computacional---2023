w = 0
N = 100
a = 0
c = 46
s = 1
ls = []
total = 47
#0.001 = 1/1000 (probando entre valores sabia que tenia que estar entre 0.001 y 0.002)
for r in (15,100): #se ejecutan "vueltas" mientras no se llegue a que todos los alumnos esten dormidos
    rr = r/1000 #al comienzo de cada vuelta, aumento el valor de r
    a = 0
    c = 46
    s = 1  
    for t in range(0,N+1):
        at = a + w*s
        if at < 0: at = 0 #mismo codigo de antes

        ct = c - rr*c*s
        if ct < 0: ct = 0 
            
        st = total - round(at) - round(ct) 
        if st < 0: st = 0

        a = at
        c = ct
        s = st

    if t == 100 and ct>=1: 
            ls += [rr]
    continue #mientras no todos esten dormidos, se repite el ciclo, no se llego al max
        

print(ls) #se imprime el valor de r, redondeado
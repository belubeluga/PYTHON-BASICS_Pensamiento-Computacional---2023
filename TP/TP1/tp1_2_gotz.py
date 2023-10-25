#constantes
w = 0
N = 100
a = 0
c = 46
s = 1
ls = []
total = 47

for r in range (100): #para probar los diversos valores de r
    rr = r/10000 #porque las iteraciones solo funcionan con int
    a = 0
    c = 46
    s = 1 
    for t in range(1, N+1): #para cada r, llegamos a los valores en tiempo N
            at = a + w*s
            if at < 0: at = 0 

            ct = c - rr*c*s
            if ct < 0: ct = 0 
            
            st = total - round(at) - round(ct)
            if st < 0: st = 0

            a = at
            c = ct
            s = st

            if t == 100 and st<=46: #si en el tiempo 100 no todos estan dormidos
                ls += [rr] #se agrega el rr valido a la lista
      

print(round(max(ls),4)) #se imprime el maximo valor de r, redondeado
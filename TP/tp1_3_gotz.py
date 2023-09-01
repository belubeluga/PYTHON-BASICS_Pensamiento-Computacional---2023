
w =0.03 #variables
r= 0.002
a = 0
c = 46
s = 1
N = 100
total = 47
valores_s = [] #lista a la cual se van a agregar todos los valores de s en cada minuto

for t in range(0, N+1):  
        at = a + w*s
        if at < 0: at = 0

        ct = c - r*c*s
        if ct < 0: ct = 0 
        
        st = total - round(at) - round(ct) #para resolver problema de redondeo
        if st < 0: st = 0

        a = at
        c = ct
        s = st

        valores_s +=[s] #agregar valores de s a la lista
print(max(valores_s))

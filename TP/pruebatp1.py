from funciones_tp1 import despiertos
from funciones_tp1 import cansados
from funciones_tp1 import dormidos
from termcolor import colored
N = 100
a = 0
c = 46
s = 1
w = 0
ls = []
total = 47
for rr in range(1,100):
    r = rr/1000
    for t in range(1,N+1):
        at = despiertos(a,w,s)
        ct = cansados(c,r,s)
        st = dormidos(a,c,s,r)
        a = at
        c = ct
        s = st
        if c<1:
            break
        if t == 100 and c>=1: 
            ls += [r]

print(ls)
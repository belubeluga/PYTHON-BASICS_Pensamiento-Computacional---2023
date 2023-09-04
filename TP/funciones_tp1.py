
def despiertos (a,s,w=0):
    at = a + w*s
    if at < 0: at = 0 #porque no puede haber una cantidad negativa de alumnos despiertos
    return at
def cansados(c,s,r):
    ct = c - r*c*s
    if ct < 0: ct = 0 
    return ct
def dormidos(a,c,s,r):
    total = a + c + s
    st = total - round(despiertos(a,s)) - round(cansados(c,s,r)) #para resolver problema de redondeo
    if st < 0: st = 0
    return st

            
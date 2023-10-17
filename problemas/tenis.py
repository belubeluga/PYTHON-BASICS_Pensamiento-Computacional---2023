import math
'''puntaje=[0,0]
matchpoint = 0
while matchpoint == 0:
    entrada = int(input("jugador que gano: 1/2: "))
    puntaje[entrada-1] += 15
    if puntaje[0]>30:
        puntaje[0]=40
        matchpoint += 1
    elif puntaje[1]>30:
        puntaje[1]=40
        matchpoint += 1
    print(puntaje[0],puntaje[1])
while matchpoint == 1:
    entrada = int(input("jugador que gano: 1/2: "))
    puntaje[entrada-1] += 15
    
    if abs(puntaje[0]-puntaje[1])>=15:
        if 45 in puntaje:
            matchpoint=2
        else: print(puntaje[0],puntaje[1])

    elif (puntaje[0]-puntaje[1]) < 15:
        if puntaje[0]>puntaje[1]: print('Adv',40)
        elif puntaje[0]<puntaje[1]: print(40,'Adv')
        else: print (40,40)
    
if matchpoint == 2:
    if puntaje[0]>puntaje[1]: ganador = 1 
    else: ganador = 2
    print(f'Ganador: jugador {ganador}')
      '''  
#%%
(-2)%1
# %%
def make_dictionary(archivo)->dict:
    ''' '''
    dic = {}
    with open(archivo) as f:
        lista = [linea.strip() for linea in f.readlines()]
        for elemento in lista:
            dic[elemento]=lista.count(elemento)
        
    return dic
# %%
def contandoMinas(campo):
    linea = len(campo)/2
    campo1 = campo[:len(campo)/2:]
    campo2 = campo[len(campo)/2::]
    for i1,elemento in enumerate(campo1):
        campo1[i1]=sum([-1 in campo1[i1-1], -1 in campo1[i1+1], -1 in campo2[i2-1],-1 in campo2[i2],-1 in campo2[i2+1]])
    for i2,elemento in enumerate(campo2):   
        campo1[i2]=sum([-1 in campo1[i2-1], -1 in campo1[i2+1], -1 in campo2[i1-1],-1 in campo2[i1],-1 in campo2[i1+1]])
    return campo1+campo2


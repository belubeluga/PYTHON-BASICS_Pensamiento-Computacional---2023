# RESÚMEN PARCIALITO 1

# tipos de dato
x = int(5)
y = str("Hola") #inmutable
z = float(5.0)
w = bool(True)
h = None #ausencia de valor

#SUMA --> solo del mismo tipo
x + z  #10.0    
y + "mundo" #Holamundo (concatenación y genera un NUEVO elemento)

lista = ["Bs As", "Vito Dumas", 248]
numero = lista[2] #accedemos al 248
li = lista + [1,2]
li += [1,2] #(no te cambia el elemento, lo expande)

#para acceder a elementos dentro del diccionario --> CLAVES

print(lista) #aplica str al contenido

#ESTUDIAR FUNCIONES BUILT IN !!!!!
# min - max - print - list - etc.
#1) diccionario
#2) estructuras
#3) corregir / justificar xq no funciona


#%%
x = input("")
if float(x) < 0:
    print("numero negativo")
 
if (float(x) > 0 and len(x) > 3) or (float(x)<0 and len(x)>4):
    print("no se hace")
elif (float(x) > 0 and len(x) ==3) or (float(x)<0 and len(x)==4):
    unidades = x[-1]
    decenas = x[-2]
    centenas = x[-3]
    print(f'Unidades = {unidades}\nDecenas = {decenas}\nCentenas = {centenas}')
elif (float(x) > 0 and len(x) ==2) or (float(x)<0 and len(x)==3):
    unidades = x[-1]
    decenas = x[-2]
    centenas = 0
    print(f'Unidades = {unidades}\nDecenas = {decenas}\nCentenas = {centenas}')
else:
    unidades = x[-1]
    decenas = 0
    centenas = 0
    print(f'Unidades = {unidades}\nDecenas = {decenas}\nCentenas = {centenas}')
      
# %%
num = input("numero de 3 digitos")
if len(num) <= 3:
    unidades = int(num)%10
    decenas = (int(num)//10)%10
    centenas = (int(num) // 100) 
    print(f'{centenas}\n{decenas}\n{unidades}')
else: print("error")
# %%
#7)
plata = int(input("$: "))
billetes = 0
if plata >= 500:
    billetes += plata//500
    plata %= 500
if plata >= 200:
    billetes += plata//200
    plata %= 200
if plata >= 100:
    billetes += plata//100
    plata %= 100
if plata >= 50:
    billetes += plata//50
    plata %= 50
if plata >= 20:
    billetes += plata//20
    plata %= 20
if plata >= 10:
    billetes += plata//10
    plata %= 10
if plata >= 5:
    billetes += plata//5
    plata %= 5
print(billetes)






# %%

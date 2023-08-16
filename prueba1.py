#%%
#Condicionales/Decisiones (6)
a = float(input("elija a: "))
b = float(input("elija b: "))
c = float(input("elija c: "))
z = b**2 - 4*a*c
import math #para acceder a la funcion raiz
if z>=0:
    x1 = ((-b)+ math.sqrt(z))/(2*a) #raiz
    x2 = ((-b)- math.sqrt(z))/(2*a)
    print(f'x1={x1}\nx2={x2}')
else:
    print("error")
# %%
#Condicionales/Decisiones (7)
parcialito1 = float(input("nota del parcialito 1: "))
parcialito2 = float(input("nota del parcialito 2: "))
parcialito3 = float(input("nota del parcialito 3: "))
parcial = float(input("nota del parcial: "))
final = float(input("nota del final: "))

a = parcialito1 * 0.1
b = parcialito2 * 0.1
c = parcialito3 * 0.1 
d = parcial * 0.3
e = final * 0.4

notafinal = a + b + c + d + e
print(f'Nota final: {float(notafinal)}')
# %%
#Condicionales/Decisiones (8)
dia = int(input("numero de dia: "))
domingo = 1
lunes = 2
martes = 3
miercoles = 4
jueves = 5
viernes = 6
sabado = 0
if dia%7 == 1:
    print("Domingo")
elif dia%7 == 2:
    print("Lunes")
elif dia%7 == 3:
    print("Martes")
elif dia%7 == 4:
    print("Miercoles")
elif dia%7 == 5:
    print("Jueves")
elif dia%7 == 6:
    print("Viernes")
elif dia%7 == 0:
    print("Sabado")

# %%
#Condicionales/Decisiones (9)
m1 = int(input("elija pendiente de la recta 1: "))
c1 = int(input("elija la ordenada al origen de la recta 1: "))

m2 = int(input("elija pendiente de la recta 2: "))
c2 = int(input("elija la ordenada al origen de la recta 2: "))

y = m1*x1 + c1
x = (y - c1)/m1
y = m2*x + c2

interseccion = (int(x),int(y))
print(interseccion)

# %%
#Condicionales/Decisiones (10)
#(a)
año = int(input("año: "))
if not(año%4):
    if año%100 != 0:
        print(f'{año} es un año bisiesto')
    else:
        if not(año%400):
            print(f'{año} es un año bisiesto')   
else:
     print(f'{año} NO es un año bisiesto')

# %%
#Condicionales/Decisiones (10)
#(b)
año = int(input("año: "))
mes = int(input("mes: "))
mes1 = 31
mes2 = 30
mes3 = 29 #ver en que año
mes4 = 28

if mes%2 == 1: #OJO CON EL ==, NO OLVIDAR
    print(f'{año},{mes}: {mes1}')
elif mes == 2: #casos febrero
    #casos años bisisestos
    if not(año%4):
        if año%100 != 0:
            print(f'{año}, {mes}: {mes3}')
        else:
            if not(año%400):
                print(f'{año}, {mes}: {mes3}')   
    else:
        print(f'{año}, {mes}: {mes4}')
elif not(mes%2):
    print(f'{año}, {mes}: {mes2}')

# %%

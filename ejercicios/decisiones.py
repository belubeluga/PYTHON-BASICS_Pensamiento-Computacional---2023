#resolucion ejercicios
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
dia = int(input("dia"))
mes1 = 31
mes2 = 30
mes3 = 29 #ver en que año
mes4 = 28

if año > 2023 or año < 0 or mes > 12 or mes<1 or dia > 31:
    print("fecha invalida")
elif mes<=7:
    if mes%2 == 1: #OJO CON EL ==, NO OLVIDAR
        print(f'{año},{mes}: {mes1}')
        print(f'Faltan {int(mes1) - dia} para fin de mes')
    elif mes == 2: #casos febrero
    #casos años bisisestos
        if not(año%4):
            if año%100 != 0:
                if dia<30:
                 print(f'{año}, {mes}: {mes3}')
                 print(f'Faltan {int(mes3) - dia} para fin de mes')
                else: print("fecha invalida")
            else:
                if not(año%400):
                    if dia<30:
                        print(f'{año}, {mes}: {mes3}')
                        print(f'Faltan {int(mes3) - dia} para fin de mes')
                    else: print("fecha invalida")
        else:
            if dia<30:
                print(f'{año}, {mes}: {mes4}')
                print(f'Faltan {int(mes4) - dia} para fin de mes')
            else: print("fecha invalida")
    elif not(mes%2):
        if dia<=30:
            print(f'{año}, {mes}: {mes2}')
            print(f'Faltan {int(mes2) - dia} para fin de mes')
        else: print("fecha invalida")
elif mes>7: #a partir de agosto se invierten
    if mes%2 == 1: 
        print(f'{año},{mes}: {mes2}')
        print(f'Faltan {int(mes2) - dia} para fin de mes')
    elif not(mes%2):
        print(f'{año}, {mes}: {mes1}')
        print(f'Faltan {int(mes1) - dia} para fin de mes')


#%%
#Condicionales/Decisiones (11)
dia = int(input("numero de dia:"))
mes = int(input("numero de mes:"))
año = int(input("numero de año: "))
fecha = (dia, mes, año)

bisiesto = bool
if not(año%4):
    if año%100 != 0:
        bisiesto = True
    else:
        if not(año%400):
            bisiesto = True  
else:
     bisiesto = False

dias = 0
if mes > 1:
    dias += 31
if mes > 2:
    if bisiesto:
        dias += 29
    elif not(bisiesto):
        dias += 28
if mes > 3:
    dias += 31
if mes > 4:
    dias += 30
if mes > 5:
    dias += 31
if mes > 6:
    dias += 30
if mes > 7:
    dias += 31
if mes > 8:
    dias += 31
if mes > 9:
    dias += 30
if mes > 10:
    dias += 31
if mes > 11:
    dias += 30
if mes > 12:
    dias += 31

primavera = 31 + 28 + 31 + 30 + 31 + 30 + 31 + 31 + 21
if bisiesto:
    primavera += 1 
if mes <= 9:
    print(f'Faltan {primavera - (dias + dia)} dias para la primavera')
elif mes > 9:
    if bisiesto:
        print(f'Faltan {366 - ((dias + dia) - primavera)} dias para la Primavera')
    else: print(f'Faltan {365 - ((dias + dia) - primavera)} dias para la Primavera')

print(fecha)

#%%
#12)
tna = float(input(""))
capital = float(input(""))
dia = float(input('dia:'))
meses = float(input("dentro de cuantos meses quiere retirar"))
cf = ((tna/100)*capital)*(meses/12) + capital
cf = capital * (tna * 12)

#%%
#13)
capital = float(input('capital: '))
periodo = int(input('meses: '))
lim = 10**6
TOR = "TOR"
XFG = "XFG"

cft = 0
cfx = 0

moneda = TOR or XFG
if moneda == TOR:
    if capital < lim:
        TNA = 0.58
        cft = TNA*capital*periodo/12 + capital
    elif capital >= lim:
        TNA = 0.535
        cft = TNA*capital*periodo/12 + capital
        cfx = cft * 200
        cfx += 0.045*30
elif moneda == XFG:
    TNA2 = 0.5
    cfx = TNA2*capital*periodo/12 + capital

if cft > cfx:
    print("hacer deposito en TOR")
elif cft < cfx:
    print("convertir a XFG")
    print(int(cfx))
else:
    print("da igual")
#%%
#14)
i = 8
j = 2
if i * j > 16:
    if i > 0:
        j = True
    elif j < 0:
        j = True
    j = False
else:
    j = i / 2
    if j < 4:
        j = "Menor"
    else:
        j = "Mayor"
print(j)

#%%
#15)

planeta = str(input("elija un planeta: "))

#es necesario siempre poner planeta ==
if planeta == "Jupiter" or planeta =="Saturno" or planeta =="Urano" or planeta =="Neptuno":
    print("es exterior")
    if planeta == "Jupiter" or planeta =="Saturno":
        print("y gigante gaseoso")
    elif planeta == "Urano" or planeta =="Neptuno": print ('y gigante helado')
else:
    print("es terrestre e interior")



# %%
# Ejercicios Secuencias y condicionales 16/8 (clase tutorial)
# ejercicio 1
a = float(input())
b = float(input())

if b == 0:
    print("error, no se puede dividir por cero")
else:
    print(a/b)
# %%
# Ejercicios Secuencias y condicionales 16/8 (clase tutorial)
# ejercicio 2
a = int(input("elija un num entero"))
print(f'num = {a}')
if a > 0:
    print("A")
    if a%2==0:
        print("C")
    if a%5==0:
        print("D")
elif a < 0:
    print("B")
    if a%4==0:
        print("E")
    if a%7==0:
        print("F")
elif a == 0:
    print("O")
    

# %%
# Ejercicios Secuencias y condicionales 16/8 (clase tutorial)
# ejercicio 3
base = "tomate, mozzarela"
opciones_validasp = ("Pepperoni", "pepperoni","p", 1)
veg_o_no = input("quiere pizza VEGETARIANA? si/no")
if veg_o_no == "si":
    veg = input("Pimiento o Cilantro?: ")
    if veg == "Pimiento" or veg == "pimiento":
        print(f'Pizza: Vegetariana \nIngredientes: {base} y {veg}')
    elif veg == "Cilantro" or veg == "cilantro":
        print(f'Pizza: Vegetariana \nIngredientes: {base} y cilantro')
    else:
        print("error")
elif veg_o_no == "no":
    nov = input("elija 1: Pepperoni, Jamon o Salmon? ")
    if nov in opciones_validasp:
        print(f'Pizza: No vegetariana \nIngredientes: {base} y Pepperoni')
    elif nov == "Jamon" or nov == "jamon":
        print(f'Pizza: No vegetariana \nIngredientes: {base} y Jamon')
    elif nov == "Salmon" or nov == "salmon":
        print(f'Pizza: NO vegetariana \nIngredientes: {base} y Salmon')
    else:
        print("error")
else:
    print("error")
# %%
# Ejercicios Secuencias y condicionales 16/8 (clase tutorial)
# ejercicio 4
a = int(input('elija numero entr 1 y 6:'))
1<=a<=6

n1 = str(" ___________"'\n'"|           |"'\n'"|           |"'\n'"|     *     |"'\n'"|           |"'\n'"|___________|")
n2 = str(" ___________"'\n'"|           |"'\n'"|  *        |"'\n'"|           |"'\n'"|        *  |"'\n'"|___________|")
n3 = str(" ___________"'\n'"|           |"'\n'"|  *        |"'\n'"|     *     |"'\n'"|        *  |"'\n'"|___________|")
n4 = str(" ___________"'\n'"|           |"'\n'"|  *     *  |"'\n'"|           |"'\n'"|  *     *  |"'\n'"|___________|")
n5 = str(" ___________"'\n'"|           |"'\n'"|  *     *  |"'\n'"|     *     |"'\n'"|  *     *  |"'\n'"|___________|")
n6 = str(" ___________"'\n'"|           |"'\n'"|  *     *  |"'\n'"|  *     *  |"'\n'"|  *     *  |"'\n'"|___________|")


if not(1<=a<=6):
    print("error")
else:
    if a == 1:
        print(n1)
    elif a == 2:
        print(n2)
    elif a ==3:
        print(n3)
    elif a == 4:
        print(n4)
    elif a == 5:
        print(n5)
    elif a ==6:
        print(n6)



# %%
num = int(input('elija numero entr 1 y 6:'))

a = " "
b = " "
c = " "
d = " "
e = " "
f = " "
g = " "

if num == 1:
    d = "*"
elif num == 2:
    a = "*"
    g = "*"
elif num == 3:
    a = "*"
    d = "*"
    g = "*"
elif num == 4:
    a = "*"
    e = "*"
    c = "*"
    g = "*"
elif num == 5:
    a = "*"
    e = "*"
    d = "*"
    c = "*"
    g = "*"
elif num == 6:
    a = "*"
    e = "*"
    b = "*"
    f = "*"
    c = "*"
    g = "*"
else: print("error")
    
dado = f'''
 ___________
|           |
|  {a}     {e}  |
|  {b}  {d}  {f}  |
|  {c}     {g}  |
|___________|
'''


# %%
x = (1,2,3)
print(x[1])
# %%

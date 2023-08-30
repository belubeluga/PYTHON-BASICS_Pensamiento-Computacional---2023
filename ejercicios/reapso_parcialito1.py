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

#errores:
# sintacticos 
# semanticos (de logico, el codigo corre pero no hace lo que yo quiero xq yo lo excribi mal)
# ejecucion (excepciones)




# %%

#computable : algoritmo posible o no
#tratable : q funcione en tiempo

#%%
horas = float(input())
pxh=(float(input()))
if horas <= 35:
    salario = horas * pxh
else:
    salario = (35*pxh) + (horas-35)*(pxh*1.5)

if salario <= 500:
    impuestos = 0
else:
    if salario - 500 <= 400:
        impuestos = (salario - 500)*0.25
    else:
        impuestos = (salario - 900)*0.45 + 0.25*400

print(salario - impuestos)
# %%
x = 1
y = 2
z = x + y
w = 3
print(int(2 ** w ** w))
print(int(2 ** (w ** w)))
print(int((2 ** w) ** w))


# %%
a = b = "la puerta azul está abierta"
print(f'{a}\n{b}')

# %%
(x,y,z) = (0.1, 25, 'azul')
#%%
x = 5
respuesta = f'el resultado es {x}'
respuesta
# %%
peras = 5
manzanas = 7
frutas = peras + manzanas
print('Hay', frutas, 'frutas en total.')
# %%
materia1 = input("materia 1: ")
nota1_m1 = float(input("nota 1, materia 1"))
nota2_m1 = float(input("nota 2, materia 1"))
nota3_m1 = float(input("nota 3, materia 1"))

materia2 = input("materia 2: ")
nota1_m2 = float(input("nota 1, materia 2"))
nota2_m2 = float(input("nota 2, materia 2"))
nota3_m2 = float(input("nota 3, materia 2"))

lista_m1 = [nota1_m1, nota2_m1, nota3_m1]
lista_m2 = [nota1_m2, nota2_m2, nota3_m2]
promedio1 = sum(lista_m1)/len(lista_m1)
promedio2 = sum(lista_m2)/len(lista_m2)
notas = {materia1: promedio1,
         materia2: promedio2}

materia_a_consultar = input("ingrese que materia quiere consultar: ")
if materia_a_consultar == materia1:
    print(round(notas[materia1],2))
elif materia_a_consultar == materia2:
    print(round(notas[materia2],2))

# %%

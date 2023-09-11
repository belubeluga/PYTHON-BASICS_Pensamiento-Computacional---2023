#%%
cake = True
if cake == True:
    print("cake es True")
else:
    print("The cake is a lie")
#%%
#determinar si un numero es par o impar
numero = float(input("inserte número"))
if numero%2==0: # % operador de resto (divide y te da el resto)
    print('Es par')
else:
    print('Es impar')



# %%
a = int(input("elija numero a"))
b = int(input("elija numero b"))

if a == b:
    print("diferencia = 0")
elif a > b:
    print("resta a - b = positivo")
else:
    print("resta a - b = negativo")
# %%
print("Ingrese el primer número: x")
x = int(input("x:"))
print("Ingrese el primer número: y")
y = int(input("y:"))

if y == 0:
    print("No se puede dividir por 0")
else:
    division = x / y
    mult = x * y
    print("El resultado de la multiplicación es", mult)
    print("El resultado de la división es", int(division))




# %%

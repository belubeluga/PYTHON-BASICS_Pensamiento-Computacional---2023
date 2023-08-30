#SECUENCIAS
#%%
#1 #2
notas = [5,4,8,9,3,2,6]
print(notas[3])
#%%
#2
notas = (5,4,8,9,3,2,6)
print(notas[3])
#%%
#3
nombres = ["Tomas", "Juan", "Estaban"]
nombres[1] = "Pedro"
nombres
#%%
#4 tuplas son inmutables
#%%
#5
lista=[1,2,3,4,5,6,7,8,9]
print(lista[0], lista[-1])
#%%
#6
lista = [1,2,3]
lista[0] += 7
lista[1] += 7
lista[2]+= 7
lista
#%%
#7
li = [10,5,30]
print(max(li))
print(min(li))
#%%
#8
li = [(20,"juan"), (18, "Pedro"), (25, "Esteban")]
menor = min(li)
menor[1]
#%%
#9
li = [[1,2,3], [4,5,6], [7,8,9]]
print(li[1][0])
print(max(li))
li[0][2] = 30
li

#%%
#DICCIONARIOS

#%%
#1
persona = {"nombre": "Sofia", "edad": 18}
print(persona['nombre'])
persona["edad"] += 1
print("Feliz cumple",persona["nombre"],"ahora tenes",persona["edad"])
if persona["edad"]>=18:
    print(f'{persona["nombre"]} es mayor de edad')
persona["apellido"] = "Ramos"
persona["notas"] = [5,6,7]
persona
print((persona["notas"][0]+persona["notas"][1]+persona["notas"][2])/len(persona["notas"]))
# %%

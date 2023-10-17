timestamp = {'hora':1340,
            'dia':12,
            'mes':4,
            'año': 2022}
y = timestamp.get("año")
print(y)
#print(timestamp)
x = timestamp.pop('año')
y = timestamp.keys()
z = timestamp.items() #clave,valor
print(timestamp)
print(x) #2022 (clave)
print(list(z)) #['hora', 'dia', 'mes']
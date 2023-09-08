#%% CLASE 11/8
# clase 11/8

# SECUENTCIAS (varios elementos con orden)

# CADENAS 
   # str "elementos son caracteres" // inmutable
s = '''cadena de muchas lineas'''
   #Concatenacion (+) // Repeticion (*) // Pertenencia (in)
x1 = "anana" in "banana"
print(x1) #==> True

# TUPLAS 
   # tuple = (los, elementos, 22, "pueden ser", False, "cualquier cosa") // inmutable       tupla = () tupla vacīa     ej: (2.1, 6)  ej: (1,)
x,y=5,6 #asignaciones múltiples
x,y=y,x
tu = ("yo", 2, False)
   #concatenacion(+) // repeticion(*) // pertenencia(in)
 #en la misma tupla // en la misma   //  respuesta en BOOL

# LISTAS 
   # list (c/elemento puede ser cualquier tipo) // MUTABLE
li = ["yo", 2, False]

# len() --> se puede aplicas len()
#print("transforma lo que le des a str")

#%%
t1 = (5,) #tuple
print(t1)
print(len(t1))
#%%
T1 = ("a", "b", "c") + ("d", "e")
T2 = (1, 2, 3) * 3
T3 = (0, 7) in ("hola", 2.5, (0, 7))
print(T1,T2,T3, sep='\n') 
print(" "*len(str(T3)), len(T1))
#%%


# INDEXING []
   # secuencia[int] = x ==> int=índice, numero o expresion o variable mientras se evalue en un num entero
   #  |--> identificador
         # lAS POSICIONES SE CUENTAN DESDE 0
colores = ["red", "green", "blue", "yellow", "white"]
#           0        1        2        3        4
print(colores[0]) 
print(colores[len(colores)-1])  #último
print(colores[len(colores)-2]) # yellow
# tmb se puede hacer INDEXING NEGATIVO (contando desde el final)
print(colores[-4])


#LISTAS O TUPLAS anidadas
secuence = [[int][int][int]] #vas accediendo distintos niveles

L1 = [4, 3, [0,2,4]]             # lista con una lista anidada
L2 = [[1,2,3], [4,5,6], [7,8,9]] # lista de listas (puede usarse como matriz)
L3 = [[1,2,3], # 0 // lista de listas
      [4,5,6], # 1 // luego de cada coma los elementos
      [7,8,9]] # 2 // se pueden escribir en la linea de abajo

print(L3[1]) 
print(L3[1][2]) # acceder al elemento 1, luego al elemento 2 de la sublista
print(L3[2][2])

# KEY-VALUE
   # key = clave para acceder, no pueden repetirse
   #  value = pueden ser cualquier cosa y repetidos
         #recomendado = NO usar float

# DICCIONARIO
   #  tipo = dict
   #  coleccion de elementps, pares key-value
d = {"clave1" : 3, "clave2": "A5", "clave3": (1,2)}


d1 = {10:[2,3,4], 15:[1,3], 23:[0,8,2,1]} #claves=int
d2 = {'Pais':'Argentina', #claves y values=str
        'Provincia':'Buenos Aires',
        'Institución':'UDESA'}
d3 = {'Nombre':'Albert', 'Edad':30, 'DNI':32456789} #claves=string
d4 = {'ID':1234, (2,3):['a','b','c'], 2:'dos', 3:'tres'} #una clave es una tupla

#Para ACCEDER por la clave
v = d1[15] #v = diccionario[key]
#Para MODIFICAR tmb
d3["Edad"] = 32 #diccionario[key] = valor
# diccionario con otro diccionario anidado
D1 = {'alumno':'Pedro',
        'notas':{'parcial1':1, 'parcial2':2, 'tp':9},
        'id':123}
print(D1['alumno'])             # acceder por clave 'alumno'
print(D1['notas']['parcial1'])  # acceder por clave 'notas', luego 'parcial1'
print(D1['notas']['parcial2'])  # acceder por clave 'notas', luego 'parcial2'
print(D1['notas']['tp'])        # acceder por clave 'notas', luego 'tp'

# UNIÓN DE DICCIONARIOS
b1 = {'a':1, 'b':2}
b2 = b1 | {'c':8} #OJO QUE NO SE SUMA, SE USA |
print(b1)
print(b2)

len(str(b1))
#ERRORES 
   #TypeError: unsupported operand type(s) for +: 'int' and 'str'


# PROBLEMA: 
# %%
producto1 = {"nombre":input("nombre:"), 
         "precio": input("precio:"), 
         "cantidad": input("cantidad:")}
producto2 = {"nombre":input("nombre:"), 
       "precio": input("precio:"), 
       "cantidad": input("cantidad:")}
producto3 = {"nombre":input("nombre:"), 
          "precio": input("precio:"), 
          "cantidad": input("cantidad:")}
lista = [producto1, producto2, producto3]
print(lista)
print("El precio de", producto3["nombre"], "es de $",producto3["precio"])

# %%
#int(datos_messi["goles"]) + ...int(datos)

#%%
#Escribir una función que reciba una lista de tuplas, 
# y que devuelva un diccionario en donde 
# las claves sean los primeros elementos de las tuplas, 
# y los valores una lista con los segundos. Por ejemplo:

# l = [ ('Hola', 'don Pepito'), ('Hola', 'don Jose'),('Buenos', 'días') ]
# print(tuplas_a_diccionario(l))
{ 'Hola': ['don Pepito', 'don Jose'], 'Buenos': ['días'] }


# %%

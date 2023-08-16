#%% CLASE 4/8
# clase 4/8

# TIPOS DE DATO
    # INT (enteros)
    # FLOAT (reales)
    # STR ("secuencias de caracteres")  INMUTABLE    ("3" es un str)
    # BOOL (True/False)
    # NONETYPE (ausencia de valor, none)
    # OTROS: list tuple dict set range bytes complex

x = 5
mensaje = "Hola mundo"
velocidad = 25.3
estado_lampara = True

n = 19
print(float(n))
# 19.0

n = n + 1 #solo se hcae una vez (no queda en loop como en la matemática)

# OPERADORES
    # ARITMÉTICOS
        # SUMA + (concatenar) (se puede sumar texto + texto)
        # MULTIPBLICACIÓN * (tmb texto)
        # RESTA Y DIVISIÓN - /
    # LÓGICOS
        # and or not
#not True = False
#not False = True
#%%
num = int(input())
if not(num%10): #if True
   print("el num es divisible por 10")
   if not(num%5) and not(num%2):
      print("el num es divisible por 5 y 2")
elif not(num%3):
   print("el num es divisible por 3")
#%%
    # DE COMPARACIÓN
        # == (contenido) != < <= >=
        # compara la primera primera letra!!!
    # DE ASIGNACIÓN 
    # DE PERTENENCIA
        # in (True esta incluido (a in b))
        # not in     (da respuesta en bool)
    # DE IDENTIDAD
        # is (entidad: contenido, dirección, etc.)
        # is not
# ORDEN DE PRECEDENCIA DE LOS OPERADORES
    # 1.Potenciaciión **
    # 2. * / // %
    # 3. + -
    # 4. == != < <= > >= is  is not  in  not in (comparación identidad y pertenencia)
    # 5. NOT logica not
    # 6. AND lógica and
var1 = 2
var2 = 6
if var1 < 12 and var2 < 8: # AMBAS condiciones se tienen que cumplir
   print("se cumple la condicion") #False and True = False
elif var1 != 0 and var2 > 6: # OJO mayor estricto
   print("Se cumple la condicion 2")
else:
   print("No se cumple la condicion")   
print("Continua el programa")
    # 7. OR lógica
            # True o xxx = True
            # False o xxx = depende del X
            #( AND --> False // OR --> True )
    # 8. Asignación = += -= *= /= //= %= **=


lista = ["Bs As", "Vito Dumas", 248]
numero = lista[2] #accedemos al 248
li = lista + [1,2]
li += [1,2] #(no te cambia el elemento, lo expande)

PI = 3.141592
diameter = 11.2
area = PI * ((diameter/2) ** 2)
circumference = PI * diameter

PI = 3.1415926535
r0 = True
r0 = '00' # como valor que puede cambiar y ser modificado y queda el último
R0 = 0
Tita_ = False

# x = abs(-5)
# (abs = identificador) (-5 = argumento) (x = salida)
# FUNCIONES PYTHON

print("Nombre",) #IMPORTANTE EL ESPACIO
# DEFINIR sep= (separador) //// end=

# \n (salto de linea) \t (tab) \b (borrado de un caracter) \r (****retorno de carro)
# 'HO\'LA'

# BOOL=y/n      (==) comparacion (=asignacion)
   #Casos False: int 0 // string "" (vacío) // float 0.0 // x=none
   #si tienen contenido serían True

   # f-strings 
   # cadena = f"texto1(expresion1)texto2(expresion2)
variable = 7.5

# CONVERSIÓN DE TIPOS
variable_bool = bool(variable)
variable_float = float(variable)
variable_int = int(variable)
variable_str = str(variable)

x1 = bool(2)
x2 = float(100)
x3 = int(25.6)
x4 = float(True)
x5 = float('-56.23')
x6 = bool ('mundo')
x7 = bool ('')
x8 = str(25.6)

# OPERADORES LÓGICOS
   #OPERACIONES UNARIAS X(F) NOT(T) // X(T) NOT(F)
   #OPERACIONES BINARIAS X() Y() AND() OR() (ver presentacion)
    #Operaciones binarias <expresion> and <expresion> // <expresion> or <expresion>

x = False
y = True

z1 = x and y
print(z1)

z2 = x or y
print(z2)

z3 = not x
print(z3)

False
True
True

#//////
x = True
y = True

z3 = not x
print(z3)

z4 = (not x) or y
print(z4)

z5 = not x and (x or y)
print(z5)

False
True
False

# and BUSCA FALSO
False and expresión
    #ya directamente es False (si con and ya alguno es Falso es falso)
# or BUSCA VERDADERO
True or expresión
    #ya directamente lo evalua con el True

level = 5
(level > 0) and (level < 99)
# CHEQUEO
    # (cantidad != 0) and (suma / cantidad < minimo)


# CONDICIONALES
    # if
#<sentencia1>
#if <condicion1>:
#    <sentencia2>
#elif <condicion2>:
#    <sentencia3>
#else:
#   <sentencia4>
#<sentencia5>

x= 5 #EJ 1
if x > 1:
   print('x es mayor a uno')
if x == 0:
   print('x es igual a cero')
if x != 0:
   print('x no es cero')
print('fin del programa')

# x es mayor a uno #resultado
# x no es cero
# fin del programa

x= 5 #EJ 2
if x > 8 or x != 5:
  print('es mayor a 8, o x no es 5')
if 2 < x and x < 10:
  print('x está entre 2 y 10')
if 2 < x < 10:
  print('x está entre 2 y 10')
print('continuamos...')

# x está entre 2 y 10 #resultado
# x está entre 2 y 10
# continuamos...'

# PROBLEMA operadores y condicionales
temperatura_max = 100
T1 = 50
T2 = 103
T3 = 110

if T1 > temperatura_max and T2 > temperatura_max and T3 > temperatura_max:
   print("Peligro!" )

elif T1 > temperatura_max and T2 > temperatura_max and T3 < temperatura_max:
   print ("Alerta")
elif T2 > temperatura_max and T3 > temperatura_max and T1 < temperatura_max:
   print ("Alerta")
elif T3 > temperatura_max and T1 > temperatura_max and T2 < temperatura_max:
   print ("Alerta")

elif T1 > temperatura_max and T2 < temperatura_max and T3 < temperatura_max:
   print ("Alerta")
elif T2 > temperatura_max and T1 < temperatura_max and T3 < temperatura_max:
    print ("Alerta")
elif T3 > temperatura_max and T2 < temperatura_max and T1 < temperatura_max:
    print ("Alerta")

else:
   print("estable")

#OPTIMIZO
temperatura_max = 100
T1 = 50
T2 = 103
T3 = 110

condicion1 = float (T1 > temperatura_max and T2 > temperatura_max and T3 < temperatura_max)
condicion2 = float (T3 > temperatura_max and T2 > temperatura_max and T1 < temperatura_max)
condicion3 = float (T1 > temperatura_max and T3 > temperatura_max and T2 < temperatura_max)

condicion4 = float (T1 > temperatura_max and T3 < temperatura_max and T2 < temperatura_max)
condicion5 = float (T2 > temperatura_max and T3 < temperatura_max and T1 < temperatura_max)
condicion6 = float (T3 > temperatura_max and T1 < temperatura_max and T2 < temperatura_max)

if T1 > temperatura_max and T2 > temperatura_max and T3 > temperatura_max:
   print("Peligro!" )

elif condicion1:
   print ("Alerta")
elif condicion2:
   print ("Alerta")
elif condicion3:
   print ("Alerta")

elif condicion4:
   print ("Alerta")
elif condicion5:
    print ("Alerta")
elif condicion6:
    print ("Alerta")

else:
   print("estable")

   # para optimizar mas = Pensarlo en BOOLEANOS
   # tabla de condiciones (cuando los 3 estan en "1", peligro, etc.)

tm = 100
s1 = 200
s2 = 50
s3 = 100
c1 = s1 > tm
c2 = s2 > tm
c3 = s3 > tm
altos = c1 + c2 + c3
if altos == 3 : print("peligro!")
elif altos == 2 : print("alerta")
elif altos == 1 : print("precaución")
elif altos == 0 : print("estable")

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

t1 = (5,) #tuple
print(t1)
print(len(t1))

T1 = ("a", "b", "c") + ("d", "e")
T2 = (1, 2, 3) * 3
T3 = (0, 7) in ("hola", 2.5, (0, 7))
print(T1, T2, T3)



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
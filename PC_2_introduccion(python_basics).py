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






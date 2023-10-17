#-------------------- OPERADORES Y CONDICIONALES --------------------

#-------------------- OPERADORES LOGICOS --------------------
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

#-------------------- CONDICIONALES --------------------

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
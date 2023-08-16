#%%
num = 42
otro_num = -13.3
texto = "esto es un texto"
var2 = True
var15 = None

print(num)
 #todo lo que haga en la ventana interactiva en paralelo NO se va a guardar acá)

valor1 = 15 #int
valor2 = 0.05 #float
nombre = "script de python" #str (ÚNICO QUE TIENE TAMAÑO)
dato = False #bool

x1 = 100
x2 = 20
x3 = -5
w = x1+x2+x3 - (x1-x2*x3)
v = x1+x2+x3+x1-x2*x3
    #  simplifico utilizando variables
y = x1+x2+x3
z = x1-x2*x3
w = y-z
v = y+z

#%%
num = 23
data1 = False # = 0
data2 = True # = 1
var = 40.0
res1 = num+data1 
res2 = num/data1 #DIVISION POR CERO --> error = NO se puede
res2a = num/data2
res3 = num*var

# int*float = float
# num + str NO SE PUEDE

# %%
print("hola " + "mundo") #hola mundo

# %%
"My name is "*3 #'My name is My name is My name is '
# ENTERO * STRING = concatena (repite el string las veces que indica el entero)
resultado = 5
valor = "158"
var1 = resultado*valor
var1 # '158158158158158'

# %%
23//2 #11
23/2 #11.5

# %%
resultado = 5
valor = "158"
lugar = "payunia"
var1 = resultado*valor #REPITE (sin espacios)
var2 = valor + lugar #CONCATENA
var3 = valor - lugar #NO SE PUEDE
var4 = var + lugar #no existe var : error
# can only concatenate str (not "int") to str

#pruebas con variables
# %%
resultado = -5
valor = "158"
lugar = "payunia"
var1 = resultado*valor 
var1 # " "
# %%
repeat = "my name is"
repeat + ", what? " + repeat + ", who?"

# %%
x = 5
respuesta = "el resultado es " + "x"
respuesta
# %%
variable1 = "hola"
print("texto",variable1, sep='\t', end=" ") #ahí definí el SEParador y el END
# si yo defino [print = variable1] (como una variable) deja de funcionar

#%%
nombre = input("ingrese su nombre")
print ("el nombre es:", nombre)

#data = input("texto que se muestra mientras se esperan datos...")


# %%

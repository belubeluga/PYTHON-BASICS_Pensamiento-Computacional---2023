# 1/9 viernes

#INDEXING
#x = secuencia[int] lectura
#secuencia[int] = x asignacion


#SLICING
# [start:stop: -step] --> generan una lista nueva
# [desde:hasta:paso]
nums = [1,2,3,4,5,6,7,8,9]
some_nums = nums[2:5] #--> [3,4,5,6]
some_nums_otro_orden = nums[5:2:-1] #--> [6,5,4]

palabra =   'COMPUTER'
        #    01234567   indices positivos
        #   -9     -1   indices negativos
palabra[4:7] = 'UTE'
palabra[:] = 'COMPUTER' #xq usas el inicio x default y el final x default
palabra[4:1] = ''
palabra[4:1:-1] = 'UPM'
palabra[4::-1] = 'UPMOC'


#MUTABILIDAD
# listas --> MUTABLES
# tuplas y cadenas --> NO MUTABLE
#%%


#ID
s = 'hola'
print(id(s)) #--> 140586154365040
# es unico
s += 'python'
print(id(s)) #--> 140586154375856
        #cambia el id, xq se crea un nuevo string
    #al modificar el elemento:
# con MUTABLES = id se mantiene
# con INMUTABLES --> SE CREA UN NUEVO ID


# LISTAS POR COMPRENSION
#expresion condicional:
x = 20
1 if x<10 else 0 #no se puede usar elif
#%%
n_par = [2, 4, 6, 8, 10]
n_impar = [e+1 for e in n_par]
print(n_par)
print(n_impar)
#[2, 4, 6, 8, 10]
#[3, 5, 7, 9, 11]
# %%


#DESEMPAQUETADO
mes, dias = ("enero", 31)
nombre, apellido = ("James", "Durbin")
x, y, z = [2.0, 1.5, 0.3]
fecha, nombres = [("enero", 31), ("James", "Durbin")]
a, b = b, a
#%%
def minimax(secuencia):
   minimo = min(secuencia)
   maximo = max(secuencia)
   return minimo, maximo
#Las funciones pueden retornar varios resultados (los empaqueta en una tupla). Luego se puede desempaquetar al invocarla.
seq = [37, 51, -33, -27, -24]
mini, maxi = minimax(seq)
#%%     desempaquetar en ciclos
#for <elem1>, <elem2> in <secuencia_de_secuencias>:
     #<sentencias>
meses = (("enero", 31), ("febrero", 28), ("diciembre", 31))
for mes, dias in meses:
    print(f"{mes} tiene {dias} días.")
#enero tiene 31 días.
#febrero tiene 28 días.
#diciembre tiene 31 días.


#ENUMERADOS
doc_teoricas = ["Pato", "Nacho", "Débora"]
print("¿Quién es el docente de tus teóricas?")
for i, profe in enumerate(doc_teoricas, 1):
   print(f"{i}. {profe}")
#Quién es el docente de tus teóricas?
#1. Pato
#2. Nacho
#3. Débora

txt = 'cadena'
for i,c in enumerate(txt,3):
    print(i,c)
# 3 c 
# 4 a 
# 5 d 
# 6 e 
# 7 n 
# 8 a

#CONVERSION DE SECUENCIAS
#%% 
str([1,2,(1,2,3)])
tuple([1,2,(1,2,3)])
list("hola") #--> ['h', 'o', 'l', 'a']
# %%

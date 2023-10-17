#-------------------- SECUENCIAS -------------------- 1/9 

#INDEXING
#x = secuencia[int] lectura
#secuencia[int] = x asignacion


#SLICING
# [start:stop: -step] --> generan una lista nueva --> el num de inicio se imprime, el de stop NO
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

#%% ejercicios clase 5/9
'''realizar una funcion que reciba una cadena 
y devuelva True si la cadena es un palindromo
y False en caso contrario'''
def palindromo(txt: str) -> bool:
    '''devuelve True si la cadena es un palindromo y False si no'''
    return txt[-1::-1] == txt

palabras = ["banana", "anana", "aca", "neuquen"]
for palabra in palabras:
    print(f'{palabra} {"es" if palindromo(palabra) else "no es"} palindroma')

#%%
'''realizar un programa que imprima los numeros enteros divisibles
por 3 desde el cero hasta el numero que imprima el usuario'''
limite = int(input("numero: "))
div = []
for i in range(limite, 0, -1):
    if i%3 == 0:
        div.append(i)
print(div)
#%%

#MUTABILIDAD
# listas --> MUTABLES
# tuplas y cadenas --> NO MUTABLE

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
lista = [num for num in range(8) if num%2==0]
    #agrega elemento,
            #num variable
                    #rango y condicion
#%%
def f_lista(lista_a):
    b = lista_a[::-1]
    c = [num for num in lista_a if num%2 == 0]
    d = [num**2 for num in lista_a]
    return b,c,d
#%%

#DESEMPAQUETADO  
mes, dias = ("enero", 31) #--> MISMA CANTIDAD
nombre, apellido = ("James", "Durbin")
x, y, z = [2.0, 1.5, 0.3]
fecha, nombres = [("enero", 31), ("James", "Durbin")]
a,b,c = (1,2,3)
#no se puede desempaquetar numeros, si tuplas
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


#ENUMERATE
doc_teoricas = ["Pato", "Nacho", "Débora"]
print("¿Quién es el docente de tus teóricas?")
for i, profe in enumerate(doc_teoricas, 1): #(ELEMENTO, INDICE)
   print(f"{i}. {profe}")
#Quién es el docente de tus teóricas?
#1. Pato
#2. Nacho
#3. Débora
txt = 'cadena'
for i,e in enumerate(txt,3): #3--> con q num empieza a enumerar
    print(i,e)
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
auto = {'nombre': input("nombre"),
        "patente": int(input("patente"))}

# 4/9
# INDEX
#%% <scecuencia>.index(<elemento>) --> int
cadena = "Hola Mundo"
cadena.index('un') #-> 6
# .index
    #sirve para cualquier tipo de secuencia
    # ValueError (se corta el programa) si no lo encuentra
    #te busca la primera 'l' que encuentra
# %%
# FIND
# .find() --> SOLO PARA STR
    #no se corta si no lo encuentra (tira -1)
cadena = "Hola Mundo"
cadena.find('o') #-> 1
# %%

# SPLIT
# <cadena>.split(<delimitador) -> list
    #separa una cadena en listas de cadena
"2022-03-01".split("-") #->['2022', '03', '01']
    #por default () te pone cualquier caracter no imprimible (' ')
        #se puede definir que separe HASTA 'x' vez
cadena = "Leyes de la fisica"
x = cadena.split(maxsplit=2) #default separa por espacios
y = cadena.split('s',maxsplit=2)
print(x) #['Leyes', 'de', 'la fisica']
print(y) #['Leye', ' de la fi', 'ica']
# %%

# JOIN
#<delimitador>.join(<secuencia) --> str
#los elementos tienen que ser STRINGS
lista = ["H","o","l","a"]
''.join(lista) #--> 'Hola'
# %%

# CASING
#<cadena>.upper() --> <todo en mayusculas>
"bazinga".upper() #--> 'BAZINGA'
#<cadena>.lower() --> <todo en minusculas>
# capitalize
"belen".capitalize() #para 1 sola letra mayuscula (crea un str nuevo con la primera mayusc, y el resto todas minusc)
"hOLA".swapcase()
# %%

# IS --> PARA CHEQUEOS
'Abc'.isalpha() #--> devuelve num
'abc123'.isalnum() 
'1234'.isdecimal() #si <0 ('-') dice False y el '.' o coma --> False
'ABC'.isupper() 
'abc'.islower() #OJO TODOS tienen que ser

#%%

#-------------------- LISTAS --------------------

# MODIFICACIONES A LISTAS
# <element>.funcion()
listita = [1,2,3,4,6]
print(listita)

listita.append([3,4]) #añade un elemento al final de la lista (se lo agrega como elemento de lista)
#listita = [1,2,3,4,5,6,[3,4]]

listita.extend([3,4])  #agrega C/elemento
#listita = [1,2,3,4,5,6,3,4]

listita.remove(2) #elimina el elemento  cuyo valor es especificado
#listita = [1,3,4,5,6]

listita.clear()

listita.reverse()
#listita = [6,4,3,2,1]

listita.sort()

listita.count(2) #cuenta la cantidad de veces que aparece el elemento
#1

listita.insert(1,2) #.insert(posicion, elemento) inserta un elemento en la posicion especificada
#listita = [2,1,2,3,4,5,6]

listita.pop(4) #--> devuelve un elemento en la POSICION especificada y lo ELIMINA 
#--> 4 (listita=[1,2,3,6])
#.extend() #añade elementos de un ITERABLE al FINAL de la lista

#%%
# COPY / IDENTIDAD
    #genero una lista nueva
    #.copy .deepcopy()
L = [1,2,3]

La = L #--> MISMA LISTA, distintos nombres
        #quedan encadenadas (borro algo de 1, se elimina de ambas)

L2 = L.copy() #copia lista independientes
# L==L2 --> True
# L2 is L --> False
L.append(4)

print(L2, L) #[1, 2, 3] [1, 2, 3, 4]

L3 = L[:] #slicing de todo --> te devuelve un elemento NUEVO
# L == L3 --> True
# L is L3 --> False

#.deepcopy() (para copiar TODOS los elementos, no que queden con las referencias (atados a otros))

# OJO --> Cuando paso listas x argumentos, 
# si la comidifico en la funcion, SE MODIFICA EN EL MAIN (afuera)
# %%
def sum(a,b):
    return a + b
def rest(a,b):
    return a - b
lista_func = [sum, rest]
def main():
    x = 4
    y = 5
    print("suma: ", lista_func[0](x,y))
    print("suma: ", lista_func[1](x,y))
#if __name__ == '__main__':
    

# %%
 # FIND
#.find --> funciona SOLO para cadenas

ord() #-->convierte valor a unicode
chr() #-->viceversa
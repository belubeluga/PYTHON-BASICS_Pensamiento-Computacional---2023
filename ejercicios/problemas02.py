#%%
# ejercicio 1
a = 50
b = 6
c = 8
d = 2*a + (1/(b-5*c))

e = (a*b + c)/(2-a)
h = (e + ((e+2)/(c+b)))* (1+e)
h

#%%
# ejercicio 2 (1)
pal1="resfrío"
pal2="mar"
pal3="picado"
pal4="pescar"

pal5=str("El " + pal2 + " estaba " + pal3 + " y solo pude " + pal4 + " un "+pal1 )
pal5
# %%
# ejercicio 2 (2)
pal1="ejercicio"
pal2="profesor"
pal3="mirando"
pal4="hacer"

pal5=str("El " + pal2 + " estaba " + pal3 + " y solo pude " + pal4 + " un "+pal1 )
pal5
# %%
# ejercicio 3 (1)
palabra1 = input("escriba palabra 1: ")
palabra2 = input("escriba palabra 2: ")
palabra3 = input("escriba palabra 3: ")
sep = input("escriba separador: ")
end = input("escriba end: ")
full_str = (palabra1 + sep + palabra2 + sep + palabra3 + end)
print(full_str)
# %%
# ejercicio 3 (2)
palabra1 = input("escriba palabra 1: ")
palabra2 = input("escriba palabra 2: ")
palabra3 = input("escriba palabra 3: ")
sep1 = input("escriba separador: ")
end1 = input("escriba end: ")
sep=sep1
end=end1
print(palabra1,palabra2,palabra3, sep=sep1,
end=end1)
# %%
# ejercicio 3 (2)
palabra1 = input("escriba palabra 1: ")
palabra2 = input("escriba palabra 2: ")
palabra3 = input("escriba palabra 3: ")
sep = input("escriba separador: ")
end = input("escriba end: ")
cadena = f'{palabra1}{sep}{palabra2}{sep}{palabra3}{end}'
print(cadena)

# %%
# ejercicio 4 
conversion = float(1.609344)
nombre = input("ingrese su nombre: ")
print("Bienvenido ",nombre)
millas = float(input("ingrese las millas a convertir: "))
resultado = millas * conversion 
s = "Hola " + nombre +", la conversión resulta:"
print(s)
print(f"{' '*len(s)} {resultado} km")
#%%
# ejercicio 5
restaurante = input("inserte nombre del restaurante: ")
costo = float(input("inserte costo: "))
propinaporcentaje = float(input("inserte porcentaje para propina: "))
propina = costo * (propinaporcentaje/100)
precio = propina + costo
calificación = input("calificación")

resumen = f"Restaurante: {restaurante} \nCosto: {costo} \nPropina: {propina} \nPrecio: {precio} \nCalificación: {calificación}"  
print(resumen)
# %%
# ejercicio 6
dibujo = str(" ___________"'\n'"|           |"'\n'"|  *     *  |"'\n'"|  *  *  *  |"'\n'"|  *     *  |"'\n'"|___________|")
print(dibujo)

#%% 

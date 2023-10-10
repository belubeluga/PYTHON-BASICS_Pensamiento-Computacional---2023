import numpy as np
from PIL import Image
#PROBLEMA A RESOLVER: al hacer la convolucion, lo nuevo que nos devuelve no coincide con las dimensiones de las imagenes
def convolucion(imagen,kernel):
    ''' '''
    imagen = Image.open(imagen)
    imagen=np.array(imagen)
    tamaño_imagen = imagen.shape
    dimension = imagen.ndim
    filak,colk = kernel.shape #filas y columnas del kernel
    imagen = np.array(imagen).tolist() #para poder copiar facilmente
    filas_a_agregar = round((filak - 1)/2) #formula de cuantas filas agregar en base al tamaño del kernel
    lista = [] #donde vamos a agregar la matriz agrandada para la convolucion con el kernel
    for e in imagen:
        nuevo=e[-1]
        nuevo2=e[0]
        pixel=e[:]
        pixel=[nuevo2]*filas_a_agregar+[e]+[nuevo]*filas_a_agregar #le agrego las columnas al final del mismo valor que los bordes de la imagen
        lista.append(pixel)
    for i in range(filas_a_agregar):
        lista.append(lista[-1]) #agrego la primera y ultima fila (la cantidad de veces necesarias para que entre bien el kernel)
        lista.insert(0,lista[0])
    lista=np.array(lista) #HASTA ACA DIM=3
    
    matriz_final = [] 
    for i in range(tamaño_imagen[0]):
        fila_matriz_final = []
        rgb = []
        for j in range(tamaño_imagen[1]):
            valor = 0
            for fk in range(filak):
                for ck in range(colk):
                    if dimension ==3:
                     #ACA TENGO QUE LOGRAR DIFERENCIAR SI ME TIENE QUE DEVOLVER DIM 2 O DIM 3
                        for color in range(3):
                            valor += lista[i+fk][j+ck][color]*kernel[fk][ck] #sumatoria de los valores
                            rgb.append(valor)
                    else: valor += lista[i+fk][j+ck]*kernel[fk][ck]
            if dimension == 3:        
                fila_matriz_final.append(rgb)
            else: fila_matriz_final+=valor
        matriz_final+=[fila_matriz_final]
    matriz_final=np.array(matriz_final)
    return matriz_final
    return lista

def main():
    #imagen=('baboon.png') #con este kernel no funciona

    kernel_sobel_horizonal=np.array([[-1,-2,11],[0,0,0],[1,2,1],[-1,-2,1],[0,0,0],[1,2,1]])
    nueva_imagen=(('TP/TP2/baboon.png'))
    
    imagen_final = convolucion(nueva_imagen, kernel_sobel_horizonal)

    print(imagen_final)
    

if __name__=='__main__':
    main()
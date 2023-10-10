import numpy as np
from PIL import Image
#PROBLEMA A RESOLVER: al hacer la convolucion, lo nuevo que nos devuelve no coincide con las dimensiones de las imagenes

def convolucion(imagen,kernel):
    imagen = Image.open(imagen)
    filak,colk = kernel.shape
    tamaño_imagen = imagen.shape
    filas_a_agregar = round((filak - 1)/2)
    forma1 = (tamaño_imagen[0]+filas_a_agregar,tamaño_imagen[1]+filas_a_agregar)
    valor = 0
    array0 = np.zeros(forma1)
    imagen = np.array(imagen)
    for i in range(filak):
        for j in range(colk):
            for fk in range(filak):
                for ck in range(colk):
                    valor += imagen[i+fk][j+ck][ck]*kernel[fk][ck]
            #valores.append(valor)
            array0[i+1][j+1]= valor
            array0[i+2][j+2]= valor
    array0[1::] = []
    return array0


def main():
    #imagen=('baboon.png') #con este kernel no funciona

    kernel_sobel_horizonal=np.array([[-1,-2,11],[0,0,0],[1,2,1],[-1,-2,11],[0,0,0],[1,2,1]])

    k2 = kernel_sobel_horizonal[1:-1:]
    for elemento in range(len(k2)):
        k2[elemento]=k2[elemento][1:-1:]
   
    print(k2)
    #imagen_final=convolucion(imagen,kernel_sobel_horizonal)
    #print(imagen_final)
    
if __name__=='__main__':
    main()
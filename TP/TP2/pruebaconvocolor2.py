import numpy as np
from PIL import Image

def convolucion(imagen_path, kernel):
    ''' HACER DOCSTRINGS Y TYPE HINTS :((((( '''
    imagen = Image.open(imagen_path)
    imagen = np.array(imagen)
    
    # tamaño de la imagen y el tamaño del kernel
    alto_imagen, ancho_imagen = imagen.shape[:2]
    filak, colk = kernel.shape
    
    # array0 donde voy a agregar los valores al final (return)
    array0 = np.zeros((alto_imagen, ancho_imagen), dtype=np.int64)

    # padding imagen
    filas_a_agregar = (filak - 1) // 2
    columnas_a_agregar = (colk - 1) // 2 
    imagen_extendida = np.pad(imagen, ((filas_a_agregar, filas_a_agregar), (columnas_a_agregar, columnas_a_agregar),(0,0)), mode='edge') 
    
    # para la convolución
    for i in range(alto_imagen):
        for j in range(ancho_imagen):
            submatriz = imagen_extendida[i:i+filak, j:j+colk] #creo submatriz del tamaño del kernel 
            for elemento in range(len(submatriz)):
                if imagen.ndim == 3:   # Imagen rgb
                    for color in range(3):
                        array0[i, j] += np.sum(submatriz[elemento][color] * kernel[elemento])
                else:  # Imagen blanco y negro  
                    array0[i, j] += np.sum(submatriz[elemento] * kernel[elemento])
    
    return array0

# Ejemplo de uso:
kernel=np.array([[-1,-2,11],[0,0,0],[1,2,1]])
imagen=(('TP/TP2/baboon.png'))

resultado = convolucion(imagen, kernel)
print(resultado)

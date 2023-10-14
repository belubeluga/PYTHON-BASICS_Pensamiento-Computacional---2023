import numpy as np
from PIL import Image
from matplotlib import pyplot as plt


def convolucion(imagen_path, kernel):
    ''' HACER DOCSTRINGS Y TYPE HINTS :((((( '''
    imagen = Image.open(imagen_path)
    imagen = np.array(imagen)
    
    try:
        dimension = imagen.ndim #arreglar lo de abajos
    except:
        dimension = len(imagen.getbands())+1
    
    # tamaño de la imagen y el tamaño del kernel
    try:
        alto_imagen, ancho_imagen = imagen.shape[:2]
    except:
        alto_imagen, ancho_imagen = imagen.size
        
    #tamaños kernel
    filak, colk = kernel.shape
    filas_a_agregar = (filak - 1) // 2
    columnas_a_agregar = (colk - 1) // 2 

    # array0 donde voy a agregar los valores al final (return) y padding
    if imagen.ndim == 3:
        array0 = np.zeros((alto_imagen, ancho_imagen, imagen.shape[2]), dtype=np.int64)
        imagen_extendida = np.pad(imagen, ((filas_a_agregar, filas_a_agregar), (columnas_a_agregar, columnas_a_agregar), (0, 0)), mode='edge')

    else: 
        array0 = np.zeros((alto_imagen, ancho_imagen), dtype=np.int64)
        imagen_extendida = np.pad(imagen, ((filas_a_agregar, filas_a_agregar), (columnas_a_agregar, columnas_a_agregar)), mode='edge')


    # para la convolución
    for i in range(alto_imagen):
        for j in range(ancho_imagen):
            submatriz = imagen_extendida[i:i+filak, j:j+colk]
            if dimension == 3:
                for color in range(len(array0[i,j])):
                    if color < 3:
                        array0[i, j, color] = np.sum(submatriz[:, :, color] * kernel)
                    else: array0[i, j, color] = (submatriz[filas_a_agregar, columnas_a_agregar, color])
            else: array0[i, j] = np.sum(submatriz * kernel)

    return array0

def normalizar(imagen):
    if imagen.ndim == 2: # Blanco y negro
        minimo = np.min(imagen)
        maximo = np.max(imagen)
        imagen_normalizada = ((imagen - minimo) / (maximo - minimo)) * 255
    else:
        imagen_normalizada = np.array(imagen)
            #para rojo:
        for color in range(3):
            color_min = np.min(imagen_normalizada[:,:,color])
            color_max = np.max(imagen_normalizada[:,:,color])
            imagen_normalizada[:, :, color] = ((imagen_normalizada[:, :, color] - color_min) / (color_max - color_min)) * 255

    return imagen_normalizada #devuelve array normalizado



def main():
    kernel=np.array([[-1,-2,11],[0,0,0],[1,2,1]])
    imagen=(('TP/TP2/baboon.png'))
    kernel_identidad=np.array([[0,0,0],[0,1,0],[0,0,0]])
    kernel_negativo=np.array([[0,0,0],[0,-1,0],[0,0,0]])
    kernel_sobel_vertical=np.array([[-1,-2,-1],[0,0,0],[1,2,1]])
    kernel_sobel_horizonal=np.array([[-1,0,1],[-2,0,2],[-1,0,1]])
    kernel_sharpen=np.array([[-1,-1,-1],[-1,8,-1],[-1,-1,-1]])
    kernel_gaussian_5x5=np.array([[1,4,6,4,1],[4,16,24,16,4],[6,24,36,24,6],[4,16,24,16,4],[1,4,6,4,1]])
    kernel_unsharpen_5x5=np.array([[-1,-4,-6,-4,-1],[-4,-16,-24,-16,-4],[-6,-24,476,-24,-6],[-4,-16,-24,-16,-4],[-1,-4,-6,-4,-1]])
    kernel_box_blur_11x11= np.array([[1 for i in range(11)]for i in range(11)])
    kernel_lens_blur_11x11=np.array([[0,0,0,0,0,1,0,0,0,0,0],[0,0,0,1,1,1,1,1,0,0,0],[0,0,1,1,1,1,1,1,1,0,0],[0,1,1,1,1,1,1,1,1,1,0],[1,1,1,1,1,1,1,1,1,1,1],[0,1,1,1,1,1,1,1,1,1,0],[0,0,1,1,1,1,1,1,1,0,0],[0,0,0,1,1,1,1,1,0,0,0],[0,0,0,0,0,1,0,0,0,0,0]])
    kernel_motion_blur_11x11=np.array([[0,0,0,0,0,0,0,0,0,0,1],[0,0,0,0,0,0,0,0,0,1,0],[0,0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,1,0,0,0],[0,0,0,0,0,0,1,0,0,0,0],[0,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,1,0,0,0,0,0,0],[0,0,0,1,0,0,0,0,0,0,0],[0,0,1,0,0,0,0,0,0,0,0],[0,1,0,0,0,0,0,0,0,0,0],[1,0,0,0,0,0,0,0,0,0,0]])

    resultado = convolucion(imagen, kernel_gaussian_5x5)
 
    resultado = normalizar(resultado)

    plt.imshow(resultado, cmap='Greys')
    plt.show()
if __name__ == '__main__':
    main()
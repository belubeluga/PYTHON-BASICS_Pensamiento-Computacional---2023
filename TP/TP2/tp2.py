from PIL import Image, ImageDraw
import numpy as np
#---------------------------------------------------
#CHEQUEO COLOR O BLANCO Y NEGRO
#---------------------------------------------------
def chequeo_color(imagen:str)->bool:
    '''si es a color te devuelve True, si es Blanco y negro devuelve False'''
    if np.array(imagen).ndim == 2:
        return False
    else:
        return True #falta ver caso transparencia
#---------------------------------------------------
#UMBRALIZADO DE IMAGENES BLANCO Y NEGRO
#---------------------------------------------------
def umbralizar_bn(nombre_imagen):
    ''' '''
    imagen = Image.open(nombre_imagen)
    prueba = np.array(imagen)
    prueba2=[]
    for x in prueba:
        lista=[]
        for i in x:
            if int(i)>128:
                i=255
            elif int(i)<=128:
                i=0
            lista.append(i)
        prueba2.append(lista)
    prueba2= np.array(prueba2)
    return prueba2 #devuelve array

#----------------------------------------------------
#UMBRALIZADO DE IMAGENES A COLOR
#-----------------------------------------------------
def umbralizar_color(nombre_imagen:str): #devuelve array
    ''' '''
    imagen = Image.open(nombre_imagen)
    prueba = np.array(imagen)
    nuevos_pixeles= []
    umbral=128
    for x in prueba:
        lista=[]
        for i in x:
            red = i[0]
            green = i[1]
            blue= i[2]
            if red>umbral and green<umbral and blue<umbral:
                i=[255,0,0] #todo pixel rojo
            elif red> umbral and green>umbral and blue<umbral:
                i= [255,255,0] #todo pixel amarillo
            elif red<umbral and green>umbral and blue<umbral:
                i=[0,255,0] #todo el pixel verde
            elif red<umbral and green>umbral and blue>umbral:
                i=[0,255,255]#todo pixel cyan
            elif red<umbral and green<umbral and blue>umbral:
                i= [0,0,255] #todo pixel azul
            elif red>umbral and green<umbral and blue>umbral:
                i=[255,0,255] #todo pixel magenta
            elif red>umbral and green>umbral and blue>umbral:
                i=[255,255,255]#pixel blanco
            elif red<umbral and green<umbral and blue<umbral:
                i=[0,0,0] #pixel negro.
            lista.append(i)
        nuevos_pixeles.append(lista)
        nuevos_pixeles=np.array(nuevos_pixeles)
    return nuevos_pixeles #devuelve array

#-------------------------------------------------------
#KERNELS como arrays :)
#-------------------------------------------------------
kernel_identidad=np.array([[0,0,0],[0,1,0],[0,0,0]])
kernel_negativo=np.array([[0,0,0],[0,-1,0],[0,0,0]])
kernel_sobel_vertical=np.array([[-1,-2,-1],[0,0,0],[1,2,1]])
kernel_sobel_horizonal=np.array([[-1,0,1],[-2,0,2],[-1,0,1]])
kernel_sharpen=np.array([[-1,-1,-1],[-1,8,-1],[-1,-1,-1]])
kernel_gaussian_5x5=np.array([[1,4,6,4,1],[4,16,24,16,4],[6,24,36,24,6],[4,16,24,16,4],[1,4,6,4,1]])
kernel_unsharpen_5x5=np.array([[-1,-4,-6,-4,-1],[-4,-16,-24,-16,-4],[-6,-24,476,-24,-6],[-4,-16,-24,-16,-4],[-1,-4,-6,-4,-1]])
kernel_box_blur_11x11= np.array([[1 for i in range(12)]for i in range(12)])
kernel_lens_blur_11x11=np.array([[0,0,0,0,0,1,0,0,0,0,0],[0,0,0,1,1,1,1,1,0,0,0],[0,0,1,1,1,1,1,1,1,0,0],[0,1,1,1,1,1,1,1,1,1,0],[1,1,1,1,1,1,1,1,1,1,1],[0,1,1,1,1,1,1,1,1,1,0],[0,0,1,1,1,1,1,1,1,0,0],[0,0,0,1,1,1,1,1,0,0,0],[0,0,0,0,0,1,0,0,0,0,0]])
kernel_motion_blur_11x11=np.array([[0,0,0,0,0,0,0,0,0,0,1],[0,0,0,0,0,0,0,0,0,1,0],[0,0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,1,0,0,0],[0,0,0,0,0,0,1,0,0,0,0],[0,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,1,0,0,0,0,0,0],[0,0,0,1,0,0,0,0,0,0,0],[0,0,1,0,0,0,0,0,0,0,0],[0,1,0,0,0,0,0,0,0,0,0],[1,0,0,0,0,0,0,0,0,0,0]])
#-------------------------------------------------------
#KERNEL PERSONALIZADO
#-------------------------------------------------------
def kernel_personalizado(): #aclara que devuelve    
    tamanio_kernel= int(input('ingrese tamanio del kernel: '))
    while tamanio_kernel%2==0:
        print('Error: numero debe ser impar')
        tamanio_kernel= int(input('ingrese tamanio del kernel: '))
    kernel_personalizado=[]
    fila=1
    for i in range(tamanio_kernel):
        pixel_kernel=[]
        print(f'ingrese {tamanio_kernel} valores para la fila {fila} del kernel')
        for pixel in range(tamanio_kernel):
            a=float(input('ingrese valor: ')) #revisar el float
            pixel_kernel.append(a)
        fila+=1
        kernel_personalizado.append(pixel_kernel)
    kernel_personalizado=np.array(kernel_personalizado)
    return kernel_personalizado

#-------------------------------------------------------
#CONVOLUCION Y NORMALIZACION
#-------------------------------------------------------
def convolucion(imagen_path, kernel):
    ''' HACER DOCSTRINGS Y TYPE HINTS :((((( '''
    imagen = np.array(imagen_path)
    
    # tamaño de la imagen y el tamaño del kernel
    alto_imagen, ancho_imagen = imagen.shape[:2]
    filak, colk = kernel.shape
    
    # array0 donde voy a agregar los valores al final (return)
    if imagen.ndim == 3:
        array0 = np.zeros((alto_imagen, ancho_imagen, imagen.shape[2]), dtype=np.int64)
    else: array0 = np.zeros((alto_imagen, ancho_imagen), dtype=np.int64)
    # padding imagen
    filas_a_agregar = (filak - 1) // 2
    columnas_a_agregar = (colk - 1) // 2 
    imagen_extendida = np.pad(imagen, ((filas_a_agregar, filas_a_agregar), (columnas_a_agregar, columnas_a_agregar), (0, 0)), mode='edge')
    
    
    # para la convolución
    for i in range(alto_imagen):
        for j in range(ancho_imagen):
            submatriz = imagen_extendida[i:i+filak, j:j+colk]
            for color in range(3):
                array0[i, j, color] = np.sum(submatriz[:, :, color] * kernel)

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
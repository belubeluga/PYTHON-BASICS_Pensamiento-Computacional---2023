import numpy as np
from PIL import Image
import tp2 
from matplotlib import pyplot as plt

try:
    imagen=input('Ingrese nombre de la imagen:')
    imagen=Image.open(imagen)
except FileNotFoundError :
    print('Archivo no se encuentra.Ingrese un nombre de una imagen existente.')
else:
    if np.array(imagen).ndim == 2:
        color=0 #imagen en byn'imagen'
    else:
        color=1 #imagen a color

    dic = {1:'Umbralizar',2:'Identidad',3:'Negativo',4:'Sobel vertical',5:'Sobel horizontal',6:'Sharpen',7:'Gaussian',8:'Unsharpen',9:'Box blur',10:'Lens blur',11:'Motion blur',12:'Kernel personalizado'}
    print('OPERACIONES\n-----------')
    for key,value in dic.items():
        print(f'{key}.{value}')

    operacion= int(input('Ingrese el numero de la operacion:'))
    opciones=[key for key in dic.keys()]
    while operacion not in opciones:#chequear
        operacion=input('Ingrese una opcion valida:')
    salida= input('Ingrese el nombre del archivo de salida:') #verificar bien q poner al final del nombre
    while salida==' ':
        salida= input('Nombre del archivo de salida no puede estar vacio. Ingresar nuevamente:')
    if operacion == 1:
        umbral=int(input('Ingrese el umbral:')) #numero que se utilizara en la umbralizacion.
        if color==0:
            final= tp2.umbralizar_bn(imagen,umbral)
            final = Image.fromarray(final.astype('uint8'))
            final.save(salida)
        else:
            final=tp2.umbralizar_color(imagen,umbral)
            plt.imshow(final, cmap='jet')
            plt.axis('off')  #chequear si hay otra manera de guardarlo
            plt.savefig(salida, bbox_inches='tight', pad_inches=0, transparent=True)#lo mismo de arriba
        print('Operacion realizada con exito!')
    elif operacion==2:
        kernel=tp2.kernel_identidad

    elif operacion==3:
        kernel=tp2.kernel_negativo
    
    elif operacion==4:
        kernel=tp2.kernel_sobel_vertical
    
    elif operacion==5:
        kernel=tp2.kernel_sobel_horizonal
    
    elif operacion==6:
        kernel=tp2.kernel_sharpen
    
    elif operacion==7:
        kernel=tp2.kernel_gaussian_5x5
    
    elif operacion==8:
        kernel=tp2.kernel_unsharpen_5x5
    
    elif operacion==9:
        kernel=tp2.kernel_box_blur_11x11
    
    elif operacion==10:
        kernel=tp2.kernel_lens_blur_11x11
    
    elif operacion==11:
        kernel=tp2.kernel_motion_blur_11x11
    
    elif operacion==12:
        kernel=tp2.kernel_personalizado()
    
    imagen_final=tp2.convolucion(imagen,kernel)
    imagen_final =tp2.normalizar(imagen_final)
    plt.imshow(imagen_final, cmap='jet')
    plt.axis('off')  
    plt.savefig(salida, bbox_inches='tight', pad_inches=0, transparent=True)
    print('Operacion realizada con exito!')
#numpy as image
#tensores
from PIL import Image
import numpy as np 
import matplotlib.pyplot as plt

img = Image.open("TP/TP2/foto_prueba.png")
img_np = np.array(img)
#print(img_np)
img.show(title=None)

def solo_rojos(imagen:str):
    '''     '''
    img = imagen.copy()
    img_np = np.array(img)
    for i in range(img_np):
        for j in range(img_np):
            r = img_np[i][j][0]
            g = img_np[i][j][1]
            b = img_np[i][j][2]
            g = 0
            b = 0
    return img_np, plt.imshow(img_np)
   
        #if (r>g) and (r>b):
           # g = 0
            #b = 0
        #print([r,g,b])
        
        
ancho,alto=img.size
#print(f'Ancho: {ancho}')
#print(f'Alto: {alto}')
#tamaño = (200,200)
#img3 = img.resize(tamaño)
#img4 = img.copy()
#img4.thumbnail(tamaño)
#plt.imshow(img3)
#img4.show()

#print(img.format, img.size, img.mode)
#print(img_np)

#PIL_image = Image.fromarray(img_np.astype('uni8t'), 'RGB')
#print(PIL_image)
img.save("out.png")
#plt.imshow("foto_prueba.png")
#plt.show("foto_prueba.png")




#usar forula para normalizar despues de cada convolucion que hagamos!!!
#CANAL TRANSPARENCIA: RGB Alpha 255 todo transparente, 0 todo opaco (no modificar!!!)


#NDARRAYS
#A[:,0]
#A[0,:]

#A[:,0,:]
# [fila, columna, canales]

#[[[][]]]
#numpy as image
#tensores
from PIL import Image
import numpy as np 
import matplotlib.pyplot as plt

img = Image.open("TP/TP2/foto_prueba.png")
img_np = np.array(img)
print(img_np)
#img.show(title=None)
'''for i in range(480):
    for j in range(512):
        r = img_np[i][j][0]
        g = img_np[i][j][1]
        b = img_np[i][j][2]
ancho,alto=img.size
print(f'Ancho: {ancho}')
print(f'Alto: {alto}')'''
#tamaño = (200,200)
#img3 = img.resize(tamaño)
#img4 = img.copy()
#img4.thumbnail(tamaño)
#plt.imshow(img3)
#img4.show()

#print(img.format, img.size, img.mode)
#print(img_np)

#PIL_image = Image.fromarray(img_np.astype('uni8t'), 'RGB')
img.save("out.png")
#plt.imshow("foto_prueba.png")
#plt.show("foto_prueba.png")



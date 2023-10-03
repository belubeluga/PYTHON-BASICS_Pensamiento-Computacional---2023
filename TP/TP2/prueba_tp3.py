from PIL import Image
import numpy as np 
import matplotlib.pyplot as plt

#%matplotlib inline

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
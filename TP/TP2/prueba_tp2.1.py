from PIL import Image
import sys #ver que es
try: 
    imagen = Image.open('foto_prueba.png')
except:
    print("No se pudo cargar la imagen")
    sys.exit #?????
imagen.show()
#Conversion de JPG a PNG
#imagen.save("paisaje.png","png")
#img2 = imagen.rotate(45)
#img2.show()
ancho,alto = imagen.size

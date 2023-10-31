import pygame
from math import *
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLUT import *



def dibujar_ejes():
    glBegin(GL_LINES)
    
    # Eje X (rojo)
    glColor3f(1.0, 0.0, 0.0)
    glVertex3f(-2.0, 0.0, 0.0)
    glVertex3f(2.0, 0.0, 0.0)
    
    # Eje Y (verde)
    glColor3f(0.0, 1.0, 0.0)
    glVertex3f(0.0, -2.0, 0.0)
    glVertex3f(0.0, 2.0, 0.0)
    
    # Eje Z (azul)
    glColor3f(0.0, 0.0, 1.0)
    glVertex3f(0.0, 0.0, -2.0)
    glVertex3f(0.0, 0.0, 2.0)
    
    glEnd()

# Función para dibujar un cubo
def dibujar_cubo():
    glBegin(GL_QUADS)  # Inicia la definición de un conjunto de vértices para un cuadrilátero (cara del cubo).

    # Coordenadas de los vértices del cubo
    vertices_cara = [
        ((-1, -1, -1), (1, -1, -1), (1, 1, -1), (-1, 1, -1)),  # Cara frontal
        ((-1, -1, 1), (1, -1, 1), (1, 1, 1), (-1, 1, 1)),      # Cara posterior
        ((-1, -1, -1), (-1, 1, -1), (-1, 1, 1), (-1, -1, 1)),  # Cara izquierda
        ((1, -1, -1), (1, 1, -1), (1, 1, 1), (1, -1, 1)),      # Cara derecha
        ((-1, 1, -1), (1, 1, -1), (1, 1, 1), (-1, 1, 1)),      # Cara superior
        ((-1, -1, -1), (1, -1, -1), (1, -1, 1), (-1, -1, 1))   # Cara inferior
    ]

    # Lista de colores para cada cara del cubo
    color2 = [
        (1.0, 0.0, 1.0, 0.0),
        (1.0, 0.0, 1.0, 0.0),
        (1.0, 0.0, 1.0, 0.0),
        (1.0, 0.0, 1.0, 0.0),
        (1.0, 0.0, 1.0, 0.0),
        (1.0, 0.0, 1.0, 0.0)
              ]
    
    colores = [
        (1.0, 0.0, 0.0),  # Cara frontal (rojo)
        (0.0, 1.0, 0.0),  # Cara posterior (verde)
        (0.0, 0.0, 1.0),  # Cara izquierda (azul)
        (1.0, 1.0, 0.0),  # Cara derecha (amarillo)
        (1.0, 0.0, 1.0),  # Cara superior (magenta)
        (0.0, 1.0, 1.0)   # Cara inferior (cian)
    ]

    for i, color in enumerate(color2):
        glColor4fv(color)  # Establece el color actual para la cara.

        # Definir los vértices para una cara del cubo
        for vertex in range(4):
            glVertex3fv(vertices_cara[i][vertex])  # Especifica las coordenadas de cada vértice de la cara.

    glEnd()  # Finaliza la definición de la cara del cubo.


# Función principal
def main():
    pygame.init()  # Inicializa Pygame.

    ancho, alto = 800, 600  # Tamaño de la ventana.
    ventana = pygame.display.set_mode((ancho, alto), DOUBLEBUF | OPENGL)  # Crea una ventana con OpenGL.
    pygame.display.set_caption("Cubo con Colores Diferentes")  # Establece el título de la ventana.

    glMatrixMode(GL_PROJECTION)  # Establece la matriz de proyección.
    glLoadIdentity()  # Inicializa la matriz de proyección.
    glFrustum(-1, 1, -1, 1, 2, 50)  # Configura la proyección perspectiva (frustum).
    glMatrixMode(GL_MODELVIEW)  # Establece la matriz de modelo-vista.
    glTranslatef(0.0, 0.0, -5)  # Realiza una traslación en el espacio de modelo-vista.
    angle = 0
    angle2 = 0
    ejecutando = True
    while ejecutando:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                ejecutando = False
            elif evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_v:
                    ejecutando = False
                elif evento.key == pygame.K_LEFT:
                    angle -= 0.2  # Rotar hacia la izquierda
                elif evento.key == pygame.K_RIGHT:
                    angle += 0.2  # Rotar hacia la derecha
                elif evento.key == pygame.K_UP:
                    angle2 -= 0.2  # Rotar hacia la izquierda
                elif evento.key == pygame.K_DOWN:
                    angle2 += 0.2  # Rotar hacia la derecha

        glRotatef(angle, 0, 1, 0)  # Realiza una rotación en el espacio de modelo-vista.
        glRotatef(angle2, 0, 0, 0)
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glClearColor(1.0, 1.0, 1.0, 0.0)

        #glRotatef(1, 3, 1, 1)  # Realiza una rotación en el espacio de modelo-vista.
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)  # Limpia los buffers de color y profundidad.
        glClearColor(1.0, 1.0, 1.0, 1.0) 
        
        dibujar_cubo()  # Llama a la función para dibujar el cubo.
        dibujar_ejes()

        pygame.display.flip()  # Actualiza la ventana.
        pygame.time.wait(10)  # Espera un tiempo breve para controlar la velocidad de fotogramas.

    pygame.quit()  # Finaliza Pygame cuando se sale del bucle.

if __name__ == "__main__":
    main()  # Llama a la función principal para iniciar el programa.
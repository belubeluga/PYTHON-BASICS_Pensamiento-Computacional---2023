import pygame
from math import *
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLUT import *

# ...

angle = 0.0  # Ángulo de rotación inicial

def main():
    pygame.init()
    # ...

    ejecutando = True
    while ejecutando:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                ejecutando = False
            elif evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_v:
                    ejecutando = False
                elif evento.key == pygame.K_LEFT:
                    angle -= 5.0  # Rotar hacia la izquierda
                elif evento.key == pygame.K_RIGHT:
                    angle += 5.0  # Rotar hacia la derecha

        glRotatef(angle, 0, 1, 0)  # Realiza una rotación en el espacio de modelo-vista.

        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glClearColor(1.0, 1.0, 1.0, 1.0)

        dibujar_cubo()
        dibujar_ejes()
        dibujar_esfera(1.0, 50)

        pygame.display.flip()
        pygame.time.wait(10)

    pygame.quit()

if __name__ == "__main__":
    main()
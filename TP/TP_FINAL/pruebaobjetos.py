import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import numpy as np

# Inicializar Pygame
pygame.init()
display = (800, 600)
pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
gluPerspective(45, (display[0] / display[1]), 0.1, 50.0)
glTranslatef(0.0, 0.0, -5)

# Cargar el archivo .obj
vertices = []
faces = []

with open('TP/TP_FINAL/tinker.obj', 'r') as obj_file:
    for line in obj_file:
        if line.startswith('v '):
            vertices.append(list(map(float, line[2:].split())))
        elif line.startswith('f '):
            face = [int(vertex.split('/')[0]) - 1 for vertex in line[2:].split()]
            faces.append(face)

vertices = np.array(vertices)
faces = np.array(faces)

# Función para renderizar el modelo
def draw_obj():
    glRotatef(1, 3, 1, 1)  # Rotar el modelo (puedes ajustar los valores)
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    
    glBegin(GL_TRIANGLES)
    for face in faces:
        for vertex_id in face:
            glVertex3fv(vertices[vertex_id])
    glEnd()

    pygame.display.flip()

# Bucle principal
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    draw_obj()

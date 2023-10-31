import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

pygame.init()
display = (800, 600)
pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
pygame.display.set_caption('Obj Viewer')

gluPerspective(45, (display[0] / display[1]), 0.1, 50.0)
glTranslatef(0.0, 0.0, -5)

def load_obj(filename):
    vertices = []
    faces = []

    with open(filename, 'r') as file:
        for line in file:
            if line.startswith('v '):
                vertices.append(list(map(float, line[2:].split())))
            elif line.startswith('f '):
                faces.append([list(map(int, vertex.split('/'))) for vertex in line[2:].split()])

    return vertices, faces

vertices, faces = load_obj('TP/TP_FINAL/tinker.obj')

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    
    for face in faces:
        glBegin(GL_POLYGON)
        for vertex in face:
            glVertex3fv(vertices[vertex[0] - 1])
        glEnd()

    pygame.display.flip()
    pygame.time.wait(10)


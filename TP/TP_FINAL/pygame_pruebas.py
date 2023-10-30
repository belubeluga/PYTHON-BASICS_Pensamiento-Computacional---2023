import pygame
import sys
import pygame.locals

pygame.init()

# Predefined some colors
BLUE  = (0, 0, 255)
RED   = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

PANTALLA = pygame.display.set_mode((800,600))
PANTALLA.fill(WHITE)
pygame.display.set_caption("Juego prueba")
icon = pygame.image.load("TP/TP_FINAL/icon.JPG")
pygame.display.set_icon(icon)

#frames per minutes
FPS = pygame.time.Clock()
FPS.tick(60)

#colision entre 2 rectas --> (bool)
object1 = pygame.Rect((20, 50), (50, 100))
object2 = pygame.Rect((10, 10), (100, 100))
print(object1.colliderect(object2))

#Game loop begins
while True:
      for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
      PANTALLA.fill(BLACK)
      pygame.display.update()




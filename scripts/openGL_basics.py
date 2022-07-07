from OpenGL.GL import *
from OpenGL.GLU import *
import pygame

pygame.init()

vertexes = (
    (1, -1, -1),
    (1, 1, -1),
    (-1, 1, -1),
    (-1, -1, -1),
    (1, -1, 1),
    (1, 1, 1),
    (-1, -1, 1),
    (-1, 1, 1),
)

edges = (
    (0, 1),
    (0, 3),
    (0, 4),
    (2, 1),
    (2, 3),
    (2, 7),
    (6, 3),
    (6, 4),
    (6, 7),
    (5, 1),
    (5, 4),
    (5, 7),
)

def MakeCube():
    glBegin(GL_LINES)
    for edge in edges:
        for vert in edge:
            glVertex3fv(vertexes[vert])

    glEnd()

DISP_W, DISP_H = 800, 600
display = pygame.display.set_mode((DISP_W, DISP_H),
                                  pygame.DOUBLEBUF | pygame.OPENGL)
pygame.display.set_caption('Rotating cube')
clock = pygame.time.Clock()

gluPerspective(45, DISP_W / DISP_H, 0.1, 50.)

glTranslate(0., 0., -5)

glRotatef(0, 0, 0, 0)

while True:

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            pygame.quit()

    glRotatef(1, 3, 1, 1)
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    MakeCube()

    pygame.display.flip()
    clock.tick(60)
import pygame
from pygame.locals import *

from OpenGL.GL import *
from OpenGL.GLU import *

vertices = (
    (1, 1, 1), (1, -1, 1), (-1, -1, 1), (-1, 1, 1),
    (1, 1, -1), (1, -1, -1), (-1, -1, -1), (-1, 1, -1)
)  # задаем вертикали куба

edges = (
    (0, 1, 2, 3), #front
    (4, 5, 6, 7), #back
    (0, 1, 5, 4), #RSide
    (3, 2, 6, 7),#LSide
    (0, 3, 7, 4),
    (1, 2, 6, 5)
)

colors = (
    (1, 0, 1),
    (1, 1, 0),
    (0, 1, 1),
    (1, 0, 0),
    (0, 0, 1),
    (0, 1, 0),
    (1, 1, 1),
)


def sq():
    glBegin(GL_QUADS)
    x = 0
    for e in edges:
        x = x+1
        print(x)
        glColor3fv(colors[x])
        for vertex in e:
            glVertex3iv(vertices[vertex])
    glEnd()


def main():
    pygame.init()
    display = (500, 500)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL | RESIZABLE)

    gluPerspective(40, display[0] / display[1], 1, 10)
    glTranslatef(0.0, 0.0, -5)
    glRotate(45, 1, 1, 0)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        glRotate(1, 1, 2, 1)
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        sq()
        pygame.display.flip()
        pygame.time.wait(20)


main()

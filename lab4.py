import math
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

import lab4

ESCAPE = '\033'

p = 0

window = 0

def InitGL(Width, Height):
    glClearColor(0.0, 0.0, 0.0, 0.0)
    glClearDepth(1.0)
    glDepthFunc(GL_LESS)
    glEnable(GL_DEPTH_TEST)
    glShadeModel(GL_SMOOTH)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(45.0, float(Width) / float(Height), 0.1, 100.0)
    glMatrixMode(GL_MODELVIEW)

def keyPressed(*args):
    if args[0] == ESCAPE:
        sys.exit()

def renderScene():
    lab4.p += 0.01
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    gluLookAt(20, -20 / 2, 60 / 2, 7.5, 6.5, 0, 0, 1, 0)

    z = 0.0
    step_state = 0.1
    height = 13

    i = 0
    while i <= 15:
        y1 = math.sin(i + lab4.p) * 0.4
        y2 = math.sin(i + lab4.p + step_state) * 0.4

        glBegin(GL_TRIANGLES)
        glColor3f(0.8, 0.2, 0.0)
        glVertex3d(i, y1, z)
        glVertex3d(i, y1 + height, z)
        glVertex3d(i + step_state, y2 + height, z)
        glEnd()

        glBegin(GL_TRIANGLES)
        glColor3f(0.8, 0.2, 0.0)
        glVertex3d(i - 0.5, y1 - 0.5, z)
        glVertex3d(i + step_state, y2, z)
        glVertex3d(i + step_state, y2 + height, z)
        glEnd()

        i += step_state

    glutSwapBuffers()
    glutPostRedisplay()

def changeSize(width, height):
    if height == 0:
        h = 1

    ratio = width * 1.0 / height

    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glViewport(0, 0, width, height)
    gluPerspective(45.0, ratio, 0.1, 100.0)

    glMatrixMode(GL_MODELVIEW)

def main():
    global window

    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_DEPTH)
    glutInitWindowSize(900, 600)
    glutInitWindowPosition(200, 200)

    window = glutCreateWindow('OpenGL lab 4')

    glEnable(GL_DEPTH_TEST)

    glutDisplayFunc(renderScene)
    glutReshapeFunc(changeSize)

    InitGL(640, 480)
    glutMainLoop()


if __name__ == "__main__":
    main()
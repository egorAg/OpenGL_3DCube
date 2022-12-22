import math

from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

ESCAPE = '\033'
ANGLE = 5

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

def cos(alpha):
    return math.cos(math.pi / 180 * alpha)

def sin(alpha):
    return math.sin(math.pi / 180 * alpha)
def renderScene():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()

    gluLookAt(5, 1, 5, 0, 0, 0, 0, 1, 0)

    glRotatef(90, 0, 0, 1)

    i = 1
    while i >= -1:
        glBegin(GL_TRIANGLE_FAN)
        glColor3f(1.0, 0.1, 0.0)
        glVertex3f(0, i, 0)
        k = 0
        while k <= 360:
            glColor3f(0.5, 0.0, 0.5)
            glVertex3f(cos(k), i, sin(k))
            k+=ANGLE
        i -= 2
        glEnd()

    glBegin(GL_TRIANGLE_STRIP)
    j = 0
    while j <= 360:
        glColor3f(1.0, 0.1, 0.0)
        glVertex3f(cos(j), 1, sin(j))
        glColor3f(1.0, 1.0, 0.0)
        glVertex3f(cos(j), -1, sin(j))
        j+=ANGLE
    glEnd()
    glutSwapBuffers()
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

    window = glutCreateWindow('OpenGL lab 3')

    glEnable(GL_DEPTH_TEST)

    glutDisplayFunc(renderScene)
    glutReshapeFunc(changeSize)

    InitGL(640, 480)
    glutMainLoop()


if __name__ == "__main__":
    main()
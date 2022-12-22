from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

ESCAPE = '\033'

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
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()

    gluLookAt(4, 4, 4, 0, 0, 0, 0, 1, 0)

    glTranslatef(-1.0, 0.0, 1.0)
    glBegin(GL_TRIANGLES)
    glColor3f(0.3, 0.0, 0.6)
    glVertex3f(0.0, 1.0, 0.0)

    glColor3f(1.0, 0.25, 0.0)
    glVertex3f(-1.0, -1.0, 1.0)

    glColor3f(1.0, 0.5, 0.0)
    glVertex3f(1.0, -1.0, 1.0)

    glEnd()

    glBegin(GL_TRIANGLES)
    glColor3f(0.3, 0.0, 0.6)
    glVertex3f(0.0, 1.0, 0.0)

    glColor3f(1.0, 0.5, 0.0)
    glVertex3f(1.0, -1.0, 1.0)

    glColor3f(0.0, 0.0, 0.0)
    glVertex3f(0.0, -1.0, -1.0)
    glEnd()

    glBegin(GL_TRIANGLES)
    glColor3f(0.3, 0.0, 0.6)
    glVertex3f(0.0, 1.0, 0.0)

    glColor3f(0.0, 0.0, 0.0)
    glVertex3f(0.0, -1.0, -1.0)

    glColor3f(1.0, 0.25, 0.0)
    glVertex3f(-1.0, -1.0, 1.0)
    glEnd()

    glBegin(GL_TRIANGLES)
    glColor3f(1.0, 0.25, 0.0)
    glVertex3f(-1.0, -1.0, 1.0)

    glColor3f(1.0, 0.5, 0.0)
    glVertex3f(1.0, -1.0, 1.0)

    glColor3f(0.0, 0.0, 0.0)
    glVertex3f(0.0, -1.0, -1.0)
    glEnd()

    glTranslatef(2.0, 0.0, -2.0)
    glRotatef(-20, 0, 1, 0)
    glBegin(GL_QUADS)
    glVertex3f(-1.0, 1.0, 1.0)
    glColor3f(0, 1, 0)

    glVertex3f(-1.0, 1.0, -1.0)
    glColor3f(0, 1, 0)

    glVertex3f(-1.0, -1.0, -1.0)
    glColor3f(0, 1, 0)

    glVertex3f(-1.0, -1.0, 1.0)
    glColor3f(0, 1, 0)
    glEnd()

    glBegin(GL_QUADS)
    glVertex3f(1.0, 1.0, 1.0)
    glColor3f(1, 0, 0)

    glVertex3f(1.0, -1.0, 1.0)
    glColor3f(1, 0, 0)

    glVertex3f(1.0, -1.0, -1.0)
    glColor3f(1, 0, 0)

    glVertex3f(1.0, 1.0, -1.0)
    glColor3f(1, 0, 0)
    glEnd()

    glBegin(GL_QUADS)
    glVertex3f(1.0, -1.0, 1.0)
    glColor3f(0, 0, 1)

    glVertex3f(-1.0, -1.0, 1.0)
    glColor3f(0, 0, 1)

    glVertex3f(-1.0, -1.0, -1.0)
    glColor3f(0, 0, 1)

    glVertex3f(1.0, -1.0, -1.0)
    glColor3f(0, 0, 1)
    glEnd()

    glBegin(GL_POLYGON)
    glVertex3f(1.0, 1.0, 1.0)
    glColor3f(1, 0, 1)

    glVertex3f(1.0, 1.0, -1.0)
    glColor3f(1, 0, 1)

    glVertex3f(-1.0, 1.0, -1.0)
    glColor3f(1, 0, 1)

    glVertex3f(-1.0, 1.0, 1.0)
    glColor3f(1, 0, 1)
    glEnd()

    glBegin(GL_POLYGON)
    glVertex3f(1.0, 1.0, 1.0)
    glColor3f(1, 1, 0)

    glVertex3f(-1.0, 1.0, 1.0)
    glColor3f(1, 1, 0)

    glVertex3f(-1.0, -1.0, 1.0)
    glColor3f(1, 1, 0)

    glVertex3f(1.0, -1.0, 1.0)
    glColor3f(1, 1, 0)
    glEnd()

    glBegin(GL_POLYGON)
    glVertex3f(1.0, 1.0, -1.0)
    glColor3f(0, 1, 1)

    glVertex3f(1.0, -1.0, -1.0)
    glColor3f(0, 1, 1)

    glVertex3f(-1.0, -1.0, -1.0)
    glColor3f(0, 1, 1)

    glVertex3f(-1.0, 1.0, -1.0)
    glColor3f(0, 1, 1)
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

    window = glutCreateWindow('OpenGL lab 2')

    glEnable(GL_DEPTH_TEST)

    glutDisplayFunc(renderScene)
    glutReshapeFunc(changeSize)

    InitGL(640, 480)
    glutMainLoop()


if __name__ == "__main__":
    main()
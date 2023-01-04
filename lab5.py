import math
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

import lab5

ESCAPE = '\033'

window = 0

RADIUS = [3.38, 9.95, 11.0, 8.53, 21.0, 19.0, 8.0, 8.0, 5.0, 5.0, 8.0, 8, 0]
DISTANCE = [59.5, 116.62, 161.84, 238.00, 416.5, 714.0, 911.5, 1206.5, 20.0, 30.0, 45.0, 80.0]
R = [1, 0.6, 0.0, 0.6, 1, 1, 0.6, 0.2, 0.8, 0.9, 0.8, 0.6]
G = [0.6, 0.2, 0.6, 0.2, 0.6, 1, 1, 0.2, 0.8, 0.9, 1, 0.8]
B = [0.0, 0.0, 1, 0.0, 0.8, 0.6, 1, 1, 0.8, 0.4, 1, 1]
SPEED = [1, 1.37, 1.6, 2.0, 3.7, 4.8, 7.0, 8.9, 5.0, 3.5, 1, 0.5]
k = 0
p = 0
x = 0
y = 0
z = 0
ANGLE = 0.0

AMBIENT = [0.2, 0.2, 0.2, 1.0]
DIFFUSE = [0.8, 0.8, 0.8, 1.0]
SPECULAR = [1.0, 1.0, 1.0, 1.0]
POSITION = [0.0, 20.0, 100.0, 1.0]

def drawSatellites():
    glPushMatrix()
    glRotatef(lab5.ANGLE * lab5.SPEED[lab5.p], lab5.x, lab5.y, lab5.z)
    glTranslatef(lab5.DISTANCE[lab5.p], 0.0, 0.0)
    glColor3f(lab5.R[lab5.p], lab5.G[lab5.p], lab5.B[lab5.p])
    glutSolidSphere(lab5.RADIUS[lab5.p], 20, 10)
    glPopMatrix()

def drawRings():
    glRotatef(-25, -1.0, 1.0, 0.0)
    glBegin(GL_QUAD_STRIP)
    glColor3f(0.85, 0.85, 0.85)
    i = 0
    while i <= 2 * math.pi:
        glVertex3f(math.cos(i) * 35, 0, math.sin(i) * 35)
        glVertex3f(math.cos(i) * 65, 0, math.sin(i) * 65)
        i = i + 0.0028
    glEnd()

def drawPlanet():
    glEnable(GL_LIGHT0)
    glEnable(GL_NORMALIZE)
    glEnable(GL_COLOR_MATERIAL)
    glEnable(GL_LIGHTING)

    glLightfv(GL_LIGHT0, GL_AMBIENT, lab5.AMBIENT)
    glLightfv(GL_LIGHT0, GL_DIFFUSE, lab5.DIFFUSE)
    glLightfv(GL_LIGHT0, GL_SPECULAR, lab5.SPECULAR)
    glLightfv(GL_LIGHT0, GL_POSITION, lab5.POSITION)

    glColor3f(1.0, 1.0, 0.0)
    glTranslatef(0, 0.0, 0.0)
    glutSolidSphere(30, 100, 50)

    j = 0
    while j < 7:
        glPushMatrix()
        glRotatef(lab5.ANGLE / lab5.SPEED[lab5.k], 0.0, 1.0, 0.0)
        glColor3f(lab5.R[lab5.k], lab5.G[lab5.k], lab5.B[lab5.k])
        glTranslatef(lab5.DISTANCE[lab5.k] * 0.9, 0.0, 0.0)
        glutSolidSphere(lab5.RADIUS[lab5.k], 40, 20)

        if j == 2:
            lab5.p = lab5.k + 6
            lab5.x, lab5.z = 0, 0
            lab5.y = 1
            drawSatellites()

        if j == 4:
            lab5.p = lab5.k + 5
            lab5.x = 0
            lab5.y, lab5.z = 1, 1
            drawSatellites()
            lab5.p = lab5.k + 6
            lab5.x = 0
            lab5.y = 1
            lab5.z = -1
            drawSatellites()

        if j == 5:
            lab5.p = lab5.k + 6
            lab5.x = 0
            lab5.y = -1
            lab5.z = 1
            drawSatellites()
            drawRings()

        lab5.x, lab5.y, lab5.z = 0, 0, 0
        glPopMatrix()
        j = j+1

    lab5.ANGLE += 0.05

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
    gluLookAt(0.0, 100.0, 1000.0, 0.0, 0.0, 0.0, 0.2, 0.8, 0.0)

    drawPlanet()
    glutSwapBuffers()

def changeSize(width, height):
    if height == 0:
        height = 1

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
    glutInitWindowSize(1333, 1000)
    glutInitWindowPosition(100, 100)

    window = glutCreateWindow('OpenGL lab 5')

    glEnable(GL_DEPTH_TEST)

    glutDisplayFunc(drawPlanet)
    glutReshapeFunc(changeSize)
    glutIdleFunc(renderScene)

    InitGL(640, 480)
    glutMainLoop()

if __name__ == "__main__":
    main()
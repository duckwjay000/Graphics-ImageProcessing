import math
import sys

try:
    from OpenGL.GLUT import *
    from OpenGL.GL import *
    from OpenGL.GLU import *
    from OpenGL.GL import glOrtho
    from OpenGL.GLU import gluPerspective
    from OpenGL.GL import glRotated
    from OpenGL.GL import glTranslated
    from OpenGL.GL import glLoadIdentity
    from OpenGL.GL import glMatrixMode
    from OpenGL.GL import GL_MODELVIEW
    from OpenGL.GL import GL_PROJECTION
except:
    print("ERROR: PyOpenGL not installed properly. ")

DISPLAY_WIDTH = 500.0
DISPLAY_HEIGHT = 500.0
ortho = False
angle = 0.0
tranX = 0.0
tranY = 0.0
translateZ = -20.0


def init(): 
    glClearColor (0.0, 0.0, 0.0, 0.0)
    glShadeModel (GL_FLAT)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()

def drawHouse ():
    glLineWidth(2.5)
    glColor3f(1.0, 0.0, 0.0)
    #Floor
    glBegin(GL_LINES)
    glVertex3f(-5.0, 0.0, -5.0)
    glVertex3f(5, 0, -5)
    glVertex3f(5, 0, -5)
    glVertex3f(5, 0, 5)
    glVertex3f(5, 0, 5)
    glVertex3f(-5, 0, 5)
    glVertex3f(-5, 0, 5)
    glVertex3f(-5, 0, -5)
    #Ceiling
    glVertex3f(-5, 5, -5)
    glVertex3f(5, 5, -5)
    glVertex3f(5, 5, -5)
    glVertex3f(5, 5, 5)
    glVertex3f(5, 5, 5)
    glVertex3f(-5, 5, 5)
    glVertex3f(-5, 5, 5)
    glVertex3f(-5, 5, -5)
    #Walls
    glVertex3f(-5, 0, -5)
    glVertex3f(-5, 5, -5)
    glVertex3f(5, 0, -5)
    glVertex3f(5, 5, -5)
    glVertex3f(5, 0, 5)
    glVertex3f(5, 5, 5)
    glVertex3f(-5, 0, 5)
    glVertex3f(-5, 5, 5)
    #Door
    glVertex3f(-1, 0, 5)
    glVertex3f(-1, 3, 5)
    glVertex3f(-1, 3, 5)
    glVertex3f(1, 3, 5)
    glVertex3f(1, 3, 5)
    glVertex3f(1, 0, 5)
    #Roof
    glVertex3f(-5, 5, -5)
    glVertex3f(0, 8, -5)
    glVertex3f(0, 8, -5)
    glVertex3f(5, 5, -5)
    glVertex3f(-5, 5, 5)
    glVertex3f(0, 8, 5)
    glVertex3f(0, 8, 5)
    glVertex3f(5, 5, 5)
    glVertex3f(0, 8, 5)
    glVertex3f(0, 8, -5)
    glEnd()

def display():
    glClear (GL_COLOR_BUFFER_BIT)
    glColor3f (1.0, 1.0, 1.0)
    # viewing transformation 

    #Your Code Here
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    if (ortho):
        glOrtho(-2.0, 2.0, -2.0, 2.0, -1.5, 1.5)
    else:
        gluPerspective(45, 1.0, 1.0, 1000)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    glRotated(angle, 0, 1, 0)
    glTranslated(tranX, tranY, translateZ)
    # call to transformation functions with saved vals
    # call to proj or ortho based on saved val

    drawHouse()
    glFlush()

    

def keyboard(key, x, y):
    global translateZ
    global tranX
    global tranY
    global angle
    global ortho

    if key == b'\x1b':
        import sys
        sys.exit(0)
  
    if key == b'w':
#            translateZ += math.cos(angle)
#            tranX += math.sin(angle)
        translateZ += 1.0

    if key == b'a':
        tranX += 1.0

    if key == b's':
        translateZ -= 1.0
        
    if key == b'd':
        tranX -= 1.0

    if key == b'q':
        angle -= 1.0


    if key == b'e':
        angle += 1.0

    if key == b'r':
        tranY -= 1.0

    if key == b'f':
        tranY += 1.0

    if key == b'h':
        tranX = 0.0
        tranY = 0.0
        translateZ = -20.0
        angle = 0.0

    if key == b'o':
        ortho = True

    if key == b'p':
        ortho = False
        
  
    glutPostRedisplay()


glutInit(sys.argv)
glutInitDisplayMode (GLUT_SINGLE | GLUT_RGB)
glutInitWindowSize (int(DISPLAY_WIDTH), int(DISPLAY_HEIGHT))
glutInitWindowPosition (100, 100)
glutCreateWindow (b'OpenGL Lab')
init ()
glutDisplayFunc(display)
glutKeyboardFunc(keyboard)
glutMainLoop()

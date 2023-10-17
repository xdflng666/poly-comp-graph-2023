from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

angle = 0.0

def reshape(width, height):
    glViewport(0, 0, width, height)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(45, (width/height), 1, 1000)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    glTranslatef(0, 0, -500)

def main_routine():
    global angle

    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glPushMatrix()
    
    glColor3f(0.0, 1.0, 1.0)

    glRotatef(angle, 1.0, 0.0, 0.0) # cube rotation
    glutWireCube(200)

    angle += 1.0
    
    glPopMatrix()
    glutSwapBuffers()


def main():
    glutInit()
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGBA | GLUT_DEPTH)
    glutInitWindowSize(1280, 720)
    glutCreateWindow("OpenGL Lab 1")

    glEnable(GL_DEPTH_TEST)

    glutDisplayFunc(main_routine) # provide display func here
    glutReshapeFunc(reshape)
    glutIdleFunc(main_routine)

    glutMainLoop()

if __name__ == '__main__':
    main()

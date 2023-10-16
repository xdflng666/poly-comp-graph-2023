from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *


def reshape(width, height):
    glViewport(0, 0, width, height)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(45, (width/height), 1, 1000)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    glTranslatef(0, 0, -500)


def task1():
    # Очищаем буфер экрана
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    glPushMatrix()
    
    # Рисуем каркасный цилиндр
    glColor3f(1.0, 1.0, 1.0)
    glTranslatef(50, 40, 0)
    glutWireCylinder(50, 360, 20, 10)

    # Wire sphere
    glColor3f(1.0, 0.0, 0.0)
    # glScalef(1.5, 1.5, 1.5) # scaling sphere
    glutWireSphere(300, 20, 10)
    glPopMatrix()

    glutSwapBuffers()


def task2():
    # Очищаем буфер экрана
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    glPushMatrix()

    # Рисуем куб
    glColor3f(1.0, 0.0, 1.0)
    glTranslatef(-200, 0, 0)
    glRotatef(180, 1.0, 0.0, 0.0) # cube rotation
    glutWireCube(150)

    # Рисуем конус
    glColor3f(1.0, 1.0, 0.0)
    glTranslatef(300, 0, 0)
    # glRotatef(-90, 1.0, 0.0, 0.0) # cone rotation

    glutWireCone(100, 200, 20, 10)

    glPopMatrix()

    glutSwapBuffers()


def main():
    glutInit()
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGBA | GLUT_DEPTH)
    glutInitWindowSize(1280, 720)
    glutCreateWindow("OpenGL Lab 1")

    glEnable(GL_DEPTH_TEST)

    # glutDisplayFunc(task1)
    glutDisplayFunc(task2)
    glutReshapeFunc(reshape)

    glutMainLoop()

if __name__ == '__main__':
    main()

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


def draw_transparent_cube():
    glTranslatef(-200, 0, 0)
    # Прозрачный синий материал
    glMaterialfv(GL_FRONT, GL_DIFFUSE, [1.0, 0.0, 1.0, 0.6])
    glutSolidCube(100)


def draw_polished_sphere():
    glMaterialfv(GL_FRONT, GL_DIFFUSE, [0.5, 0.5, 0.5, 1.0])  # Серый материал
    # Зеркальный серый материал
    glMaterialfv(GL_FRONT, GL_SPECULAR, [0.5, 0.5, 0.5, 1.0])
    glMaterialf(GL_FRONT, GL_SHININESS, 128.0)  # Максимальная степень блеска
    glTranslatef(200, 0, 0)
    glutSolidSphere(60, 50, 30)


def draw_matte_cone():
    glMaterialfv(GL_FRONT, GL_DIFFUSE, [1.0, 0.2, 0.8, 1.0])  # Серый материал
    glTranslatef(200, -50, 0)
    glRotatef(-90, 1, 0, 0)
    glutSolidCone(50, 100, 20, 10)


def main_routine():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    glPushMatrix()

    draw_transparent_cube()
    draw_polished_sphere()
    draw_matte_cone()

    glPopMatrix()
    glutSwapBuffers()


# Глобальные переменные для управления источником света
light_position = [1.0, 1.0, 1.0, 0.0]  # Положение источника света
light_diffuse = [1.0, 1.0, 1.0, 1.0]  # Диффузный цвет света
light_specular = [1.0, 1.0, 1.0, 1.0]  # Зеркальный цвет света
light_ambient = [0.2, 0.2, 0.2, 1.0]


def main():
    glutInit()
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGBA | GLUT_DEPTH)
    glutInitWindowSize(1280, 720)
    glutCreateWindow("OpenGL Lab 2")

    glEnable(GL_DEPTH_TEST)
    glEnable(GL_LIGHTING)
    glEnable(GL_LIGHT0)


    # Установка параметров источника света
    glLightfv(GL_LIGHT0, GL_POSITION, light_position)
    glLightfv(GL_LIGHT0, GL_AMBIENT, light_ambient)
    glLightfv(GL_LIGHT0, GL_DIFFUSE, light_diffuse)
    glLightfv(GL_LIGHT0, GL_SPECULAR, light_specular)

    # # One more light test
    # glEnable(GL_LIGHT1)
    # # Установка параметров источника света
    # glLightfv(GL_LIGHT1, GL_POSITION, [0,0,1,0])
    # glLightfv(GL_LIGHT1, GL_AMBIENT, [1,0,0,0])
    # glLightfv(GL_LIGHT1, GL_DIFFUSE, light_diffuse)
    # glLightfv(GL_LIGHT1, GL_SPECULAR, light_specular)

    glutDisplayFunc(main_routine)  # provide display func here
    glutReshapeFunc(reshape)

    glutMainLoop()


if __name__ == '__main__':
    main()

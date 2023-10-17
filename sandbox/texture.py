from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
from PIL import Image

def load_texture(filename):
    img = Image.open(filename)
    img_data = img.tobytes("raw", "RGBX", 0, -1)
    width, height = img.size
    texture_id = glGenTextures(1)
    glBindTexture(GL_TEXTURE_2D, texture_id)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_REPEAT)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_REPEAT)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR)
    glTexImage2D(GL_TEXTURE_2D, 0, GL_RGBA, width, height, 0, GL_RGBA, GL_UNSIGNED_BYTE, img_data)
    return texture_id

# def draw_cone():
#     glEnable(GL_TEXTURE_2D)
#     glEnable(GL_TEXTURE_GEN_S)
#     glEnable(GL_TEXTURE_GEN_T)
#     glTexGeni(GL_S, GL_TEXTURE_GEN_MODE, GL_SPHERE_MAP)
#     glTexGeni(GL_T, GL_TEXTURE_GEN_MODE, GL_SPHERE_MAP)
#     glBindTexture(GL_TEXTURE_2D, texture_id)
#     glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
#     glLoadIdentity()
#     glTranslatef(0.0, 0.0, -5.0)
#     glRotatef(45, 1.0, 1.0, 1.0)
#     glutSolidCone(1.0, 2.0, 32, 32)
#     glDisable(GL_TEXTURE_GEN_S)
#     glDisable(GL_TEXTURE_GEN_T)
#     glDisable(GL_TEXTURE_2D)
#     glutSwapBuffers()

# glutInit()
# glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_DEPTH)
# glutInitWindowSize(640, 480)
# glutCreateWindow("Textured Cone")
# texture_id = load_texture("texture.png")
# glutDisplayFunc(draw_cone)

# glutMainLoop()

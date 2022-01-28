
from OpenGL import GL as gl
from OpenGL import GLU as glu
from OpenGL import GLUT as glut

from arm_gl import ArmAngles, ArmGL
from camera import Camera
import numpy as np

from keyboard_controler import KeyboardController

WIDTH = 800
HEIGHT = 600


def reshape(width: int,  height: int):
    global WIDTH, HEIGHT

    WIDTH = width
    HEIGHT = height
    print(f'width: {width} height: {height}')
    gl.glViewport(0, 0, width, height)
    gl.glMatrixMode(gl.GL_PROJECTION)
    gl.glLoadIdentity()
    glu.gluPerspective(70.0, width/height, 0.1, 30.0)
    gl.glMatrixMode(gl.GL_MODELVIEW)
    glut.glutPostRedisplay()


def opengl_init():
    gl.glClearColor(1.0, 1.0, 1.0, 1.0)
    gl.glEnable(gl.GL_DEPTH_TEST)

    """Habilitar a textura"""
    gl.glEnable(gl.GL_BLEND)
    gl.glBlendFunc(gl.GL_SRC_ALPHA, gl.GL_ONE_MINUS_SRC_ALPHA)

#   carregar_texturas();
    gl.glShadeModel(gl.GL_FLAT)
    gl.glEnable(gl.GL_TEXTURE_2D)


def window_init():
    glut.glutInitWindowPosition(0, 0)
    glut.glutInit()
    glut.glutInitDisplayMode(
        glut.GLUT_RGBA | glut.GLUT_DEPTH | glut.GLUT_DOUBLE | glut.GLUT_ALPHA)
    glut.glutInitWindowSize(WIDTH, HEIGHT)
    glut.glutCreateWindow("BRACO GARRA")
    glut.glutPositionWindow(400, 400)


def main():

    arm = ArmGL()
    camera = Camera()
    keyboard_controler = KeyboardController(arm, camera)
    window_init()

    opengl_init()
    """"Para criar o Braço preciso ter inicializado a janela GLUT e OpenGL"""
    arm.make_arm()

    def display():

        gl.glEnable(gl.GL_DEPTH_TEST)
        gl.glClear(gl.GL_COLOR_BUFFER_BIT | gl.GL_DEPTH_BUFFER_BIT)
        gl.glPushMatrix()

        camera.look_at()

        gl.glColor4f(0.52, 0.52, 0.78, 1.0)
        gl.glBegin(gl.GL_QUADS)
        gl.glVertex3f(-10, 0, 10)
        gl.glVertex3f(10, 0, 10)
        gl.glVertex3f(10, 0, -10)
        gl.glVertex3f(-10, 0, -10)
        gl.glEnd()

        gl.glTranslatef(-3.0, 0.5, 0.0)
        gl.glCallList(arm.arm_id)
        gl.glPopMatrix()

        arm.make_arm()

        glut.glutSwapBuffers()

    def normal_keys_handler(key: bytes, x: int, y: int):
        print('key', key)
        if keyboard_controler.key_press(key):
            glut.glutPostRedisplay()

    def special_keys_handler(key: int, x: int, y: int):
        if keyboard_controler.special_key_press(key):
            glut.glutPostRedisplay()

    glut.glutDisplayFunc(display)
    glut.glutReshapeFunc(reshape)
    glut.glutKeyboardFunc(normal_keys_handler)
    glut.glutSpecialFunc(special_keys_handler)

    glut.glutMainLoop()


if __name__ == '__main__':
    main()

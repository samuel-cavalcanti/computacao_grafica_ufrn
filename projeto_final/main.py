
from typing import Optional
from OpenGL import GL as gl
from OpenGL import GLU as glu
from OpenGL import GLUT as glut

from arm_gl import ArmGL
from camera import Camera
import numpy as np
import cv2
from keyboard_controler import KeyboardController

WIDTH = 800
HEIGHT = 600

FLOOR_TEXTURE_ID: Optional[int] = None
METAL_TEXTURE_ID: Optional[int] = None


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


def load_texture(image_path: str) -> int:
    image: np.ndarray = cv2.imread(image_path)  # segundo o OpenCV está em BGR

    texture = gl.glGenTextures(1)
    gl.glBindTexture(gl.GL_TEXTURE_2D, texture)

    gl.glTexImage2D(gl.GL_TEXTURE_2D,
                    0,
                    gl.GL_RGB,  # formato da saída
                    image.shape[0],
                    image.shape[1],
                    0,
                    gl.GL_BGR,  # formato da imagem
                    gl.GL_UNSIGNED_BYTE,
                    image)

    gl.glTexParameteri(gl.GL_TEXTURE_2D, gl.GL_TEXTURE_WRAP_S, gl.GL_REPEAT)
    gl.glTexParameteri(gl.GL_TEXTURE_2D, gl.GL_TEXTURE_WRAP_T, gl.GL_REPEAT)

    gl.glTexParameteri(
        gl.GL_TEXTURE_2D, gl.GL_TEXTURE_MIN_FILTER, gl.GL_NEAREST)
    gl.glTexParameteri(
        gl.GL_TEXTURE_2D, gl.GL_TEXTURE_MAG_FILTER, gl.GL_NEAREST)

    return texture


def load_textures():
    global FLOOR_TEXTURE_ID, METAL_TEXTURE_ID

    FLOOR_TEXTURE_ID = load_texture('piso_2.jpeg')

    METAL_TEXTURE_ID = load_texture('metal.jpeg')


def main():

   
    
    
    window_init()

    opengl_init()

    load_textures()
    camera = Camera()
    arm = ArmGL(texture_id=METAL_TEXTURE_ID)
    keyboard_controler = KeyboardController(arm, camera)
    """"Para criar o Braço preciso ter inicializado a janela GLUT e OpenGL"""
    arm.make_arm()

    def display():

        gl.glEnable(gl.GL_DEPTH_TEST)
        gl.glClear(gl.GL_COLOR_BUFFER_BIT | gl.GL_DEPTH_BUFFER_BIT)
        gl.glPushMatrix()

        camera.look_at()

        gl.glColor4f(1.0, 1.0, 1.0, 1.0)
        gl.glPolygonMode(gl.GL_FRONT_AND_BACK, gl.GL_FILL)
        gl.glBindTexture(gl.GL_TEXTURE_2D, FLOOR_TEXTURE_ID)
        gl.glBegin(gl.GL_QUADS)

        """
        (10,-10)--------------------------(-10,-10)             
            |                             |     
            |                             | 
            |                             |
        (10.10) ------------------------(-10,10) #(x,z)
        """

        gl.glTexCoord2fv([0.0, 0.0])
        gl.glVertex3f(10, 0, 10)

        gl.glTexCoord2fv([1.0, 0.0])  # (x,y)
        gl.glVertex3f(-10, 0, 10)

        gl.glTexCoord2fv([1.0, 1.0])
        gl.glVertex3f(-10, 0, -10)

        gl.glTexCoord2fv([0.0, 1.0])
        gl.glVertex3f(10, 0, -10)

        gl.glEnd()

        gl.glTranslatef(-3.0, 0.5, 0.0)
        gl.glCallList(arm.arm_id)
        gl.glPopMatrix()

        arm.make_arm()

        glut.glutSwapBuffers()
        glut.glutPostRedisplay()

    def normal_keys_handler(key: bytes, x: int, y: int):
        print('key', key)
        if keyboard_controler.key_press(key):
            glut.glutPostRedisplay()

    def special_keys_handler(key: int, x: int, y: int):
        if keyboard_controler.special_key_press(key):
            glut.glutPostRedisplay()

    """ conjunto de funções do gerenciador de janelas"""
    glut.glutDisplayFunc(display)
    glut.glutReshapeFunc(reshape)
    glut.glutKeyboardFunc(normal_keys_handler)
    glut.glutSpecialFunc(special_keys_handler)

    glut.glutMainLoop()


if __name__ == '__main__':
    main()

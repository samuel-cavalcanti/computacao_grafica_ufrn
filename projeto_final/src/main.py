

from pathlib import Path
from typing import Optional
from OpenGL import GL as gl
from OpenGL import GLU as glu
from OpenGL import GLUT as glut

from camera import Camera
import numpy as np
import cv2

from keyboard_controler import KeyboardController
from gl_models import arm_model, floor_model
from arm_angles import ArmAngles


WIDTH = 800
HEIGHT = 600

FLOOR_TEXTURE_ID: Optional[int] = None
METAL_TEXTURE_ID: Optional[int] = None
FLOOR_IMAGE = Path('images').joinpath('piso_2.jpeg')
METAL_IMAGE = Path('images').joinpath('metal.jpeg')


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


def load_texture(image_path: Path) -> int:
    """
        carrega uma textura por uma image em qualquer formato suportado pelo OpenCV. 
    """

    # segundo o OpenCV a imagem está em BGR
    image: np.ndarray = cv2.imread(str(image_path))

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

    """
        Basicamente glTexParameteri eu configuro os parâmetros da textura
        GL_REPEAT, implica que vou repetindo a mesma imagem infinitamente e
        GL_NEAREST, implica que a cor do pixel mais próxima é que vai ser escolhida
        é mais fácil de visualizar na referência:  https://learnopengl.com/Getting-started/Textures

    """
    gl.glTexParameteri(gl.GL_TEXTURE_2D, gl.GL_TEXTURE_WRAP_S, gl.GL_REPEAT)
    gl.glTexParameteri(gl.GL_TEXTURE_2D, gl.GL_TEXTURE_WRAP_T, gl.GL_REPEAT)

    gl.glTexParameteri(
        gl.GL_TEXTURE_2D, gl.GL_TEXTURE_MIN_FILTER, gl.GL_NEAREST)
    gl.glTexParameteri(
        gl.GL_TEXTURE_2D, gl.GL_TEXTURE_MAG_FILTER, gl.GL_NEAREST)

    return texture


def load_textures():
    global FLOOR_TEXTURE_ID, METAL_TEXTURE_ID

    FLOOR_TEXTURE_ID = load_texture(FLOOR_IMAGE)

    METAL_TEXTURE_ID = load_texture(METAL_IMAGE)


def main():

    window_init()

    opengl_init()

    load_textures()
    camera = Camera()

    # arm = ArmGL(texture_id=METAL_TEXTURE_ID, arm_model=arm_model.draw_arm)
    arm_angles = ArmAngles()
    keyboard_controler = KeyboardController(arm_angles, camera)
    """"Para criar o Braço preciso ter inicializado a janela GLUT e OpenGL"""

    def display():
        """
            Callback de visualização da  janela glut
            Basicamente  limbo a tela, posiciono a camera e desenho o braço e chão.
        """

        gl.glClear(gl.GL_COLOR_BUFFER_BIT | gl.GL_DEPTH_BUFFER_BIT)
        gl.glPushMatrix()

        camera.look_at()

        floor_model.draw_floor(FLOOR_TEXTURE_ID)

        gl.glTranslatef(-3.0, 0.5, 0.0)
        arm_model.draw_arm(arm_angles, METAL_TEXTURE_ID)
        # arm.show()

        gl.glPopMatrix()

        glut.glutSwapBuffers()
        glut.glutPostRedisplay()

    def normal_keys_handler(key: bytes, x: int, y: int):
        keyboard_controler.key_press(key)

    def special_keys_handler(key: int, x: int, y: int):
        keyboard_controler.special_key_press(key)

    """ conjunto de funções do gerenciador de janelas"""
    glut.glutDisplayFunc(display)
    glut.glutReshapeFunc(reshape)
    glut.glutKeyboardFunc(normal_keys_handler)
    glut.glutSpecialFunc(special_keys_handler)

    glut.glutMainLoop()


if __name__ == '__main__':
    main()

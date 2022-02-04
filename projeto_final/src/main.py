

from pathlib import Path
from OpenGL import GL as gl
from OpenGL import GLU as glu
from OpenGL import GLUT as glut

from camera import Camera
import numpy as np
import cv2

from keyboard_controler import KeyboardController
from gl_models import arm_model, floor_model
from arm_angles import ArmAngles


"""
Por padrão vamos iniciar
a janela em 800x600, mas
podemos redimensiona-la
durante a aplicação
"""
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600

"""
Para que o caminho até a image
seja agnóstico de sistema operacional
usamos a classe Path do python, mas
é bom lembrar que esse script deve ser
executado dentro do diretório projeto_final
"""
FLOOR_IMAGE_PATH = Path('images').joinpath('piso_2.jpeg')
METAL_IMAGE_PATH = Path('images').joinpath('metal.jpeg')


def reshape(width: int,  height: int):
    """Callback chamando no momento que a tela é redimensionada"""
    global WINDOW_WIDTH, WINDOW_HEIGHT

    WINDOW_WIDTH = width
    WINDOW_HEIGHT = height
    print(f'width: {width} height: {height}')

    """
        ViewPort é o local da área ser renderizada pelo OpenGL
        no caso estamos pegando a janela toda
    """
    gl.glViewport(0, 0, width, height)

    """
        Criando uma visão em perspectiva para dar uma idea de
        profundidade no nosso mundo 3D
    """
    gl.glMatrixMode(gl.GL_PROJECTION)
    gl.glLoadIdentity()
    glu.gluPerspective(70.0, width/height, 0.1, 30.0)
    gl.glMatrixMode(gl.GL_MODELVIEW)


def opengl_init():
    """
        É nessa função que coloquei a configuração inicial do OpenGL.
    """

    """
        Configurado a cor que será usada para limpar a tela como um escurinho
    """
    gl.glClearColor(0.07, 0.13, 0.17, 1.0)
    """ habilite a profundidade,  ou seja x,y,z"""
    gl.glEnable(gl.GL_DEPTH_TEST)

    """Configurações para habilitar a textura"""
    gl.glEnable(gl.GL_BLEND)
    gl.glBlendFunc(gl.GL_SRC_ALPHA, gl.GL_ONE_MINUS_SRC_ALPHA)

    gl.glShadeModel(gl.GL_FLAT)
    gl.glEnable(gl.GL_TEXTURE_2D)


def window_init():
    """
        Configurações iniciais do gestor de janelas GLUT
        basicamente coloco a janela para se posicionar na
        posição:
            x: 400
            y: 400
        coloco o nome da janela e digo que ela tem profundidade e renderiza em RGBA
    """
    glut.glutInit()
    glut.glutInitDisplayMode(
        glut.GLUT_RGBA | glut.GLUT_DEPTH | glut.GLUT_DOUBLE | glut.GLUT_ALPHA)
    glut.glutInitWindowSize(WINDOW_WIDTH, WINDOW_HEIGHT)
    glut.glutCreateWindow("Braco Robotico")
    glut.glutPositionWindow(400, 400)


def load_texture(image_path: Path) -> int:
    """
        carrega uma textura por uma image em qualquer formato suportado pelo OpenCV. 
    """

    # segundo o OpenCV a imagem está em BGR
    image: np.ndarray = cv2.imread(str(image_path))

    """crio um id de textura
      digo ao OpenGL para selecionar a textura
      carrego a textura no formado de imagem
      configuro os parâmetros da textura

       """
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


def main():

    window_init()

    opengl_init()

    camera = Camera()

    """instanciado os anglos do braço, por padrão é tudo 0 graus"""
    arm_angles = ArmAngles()
    keyboard_controler = KeyboardController(arm_angles, camera)

    """
        Carregando as texturas, no caso estamos utilizando o OpenCV para
        carrega-las e por conveniências ambas as texturas tem os mesmos parâmetros.
    """

    floor_texture_id = load_texture(FLOOR_IMAGE_PATH)

    arm_texture_id = load_texture(METAL_IMAGE_PATH)

    def display():
        """
            Callback de visualização da  janela glut
            Basicamente  limbo a tela, posiciono a camera e 
            desenho:
                o braço,
                o chão

            digo para o gesto GLUT, para trocar o buffer background para o front (glutSwapBuffers)
            mando ele chamadar a função display novamente. (glutPostRedisplay)
        """

        gl.glClear(gl.GL_COLOR_BUFFER_BIT | gl.GL_DEPTH_BUFFER_BIT)
        gl.glPushMatrix()

        camera.look_at()  # basicamente é a função gluLookAt com as posições e orientações da câmera

        floor_model.draw_floor(floor_texture_id)

        gl.glTranslatef(-3.0, 0.5, 0.0)
        arm_model.draw_arm(arm_angles, arm_texture_id)

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
    """
       normal_keys_handler, special_keys_handler
       são funções callbacks que são chamadas no momento que eu pressiono uma tecla.
    """
    glut.glutKeyboardFunc(normal_keys_handler)
    glut.glutSpecialFunc(special_keys_handler)

    glut.glutMainLoop()  # sequesta a aplicação até fechar a janela.


if __name__ == '__main__':
    main()

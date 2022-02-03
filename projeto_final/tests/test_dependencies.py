import unittest


class DependenciesTestCase(unittest.TestCase):
    """Cheking Dependencies"""

    def test_install_opengl_(self):

        try:
            from OpenGL import GL
            from OpenGL import GLUT
            from OpenGL import GLU
            opengl_works = True
        except ModuleNotFoundError:
            opengl_works = False
            pass

        self.__check_import(import_name='OpenGL', is_works=opengl_works)

    def test_install_numpy_(self):

        try:
            import numpy as np
            numpy_works = True
        except ModuleNotFoundError:
            numpy_works = False
            pass

        self.__check_import(import_name='numpy', is_works=numpy_works)

    def test_install_opencv(self):
        try:
            import cv2
            opencv_works = True
        except ModuleNotFoundError:
            opencv_works = False

        self.__check_import(import_name='OpenCV', is_works=opencv_works)

    def __check_import(self, import_name: str, is_works: bool) -> None:
        self.assertTrue(
            is_works, msg=f'{import_name} não instalado!! por favor execute pip install -r requirements.txt')

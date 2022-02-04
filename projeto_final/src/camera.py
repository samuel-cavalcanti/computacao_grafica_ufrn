from OpenGL import GLU as glu
from OpenGL import GL as gl
import numpy as np


class Camera:
    position = [6.0, 7.0, 0.0]
    look = [0.0, 3.0, 0.0]


    def update_position_by_polar_system(self, angle_xz_in_degrees: float, ray_xz: float = 6):
        """
            Atualizando a posição da câmera utilizando o sistema polar, podemo fazer como que
            a câmera gire em torno de um ponto.
            Experimentalmente  utilizando um raio igual 6 obtimentos uma boa visualização.
        """
        angle_in_rads = np.deg2rad(angle_xz_in_degrees)
        self.position[0] = ray_xz*np.cos(angle_in_rads)
        self.position[2] = ray_xz*np.sin(angle_in_rads)

    def look_at(self):

        glu.gluLookAt(self.position[0], self.position[1], self.position[2],
                      self.look[0], self.look[1], self.look[2],
                      0.0, 1.0, 0.0)

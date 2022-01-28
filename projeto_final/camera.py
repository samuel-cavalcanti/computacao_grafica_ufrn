from OpenGL import GLU as glu
from OpenGL import GL as gl
import numpy as np


class Camera:
    obs = [0.0, 7.0, 0.0]
    look = [0.0, 3.0, 0.0]
    tetaxz = 0
    raioxz = 6

    def look_at(self):
        # gl.glPushMatrix()
       
        # calcula a posicao do observador */
        # O movimento da camera corresponde a um movimento circular em torno do objeto */
        self.obs[0] = self.raioxz*np.cos(2*np.pi*self.tetaxz/360)
        self.obs[2] = self.raioxz*np.sin(2*np.pi*self.tetaxz/360)

        

        glu.gluLookAt(self.obs[0], self.obs[1], self.obs[2],
                      self.look[0], self.look[1], self.look[2],
                      0.0, 1.0, 0.0)
       

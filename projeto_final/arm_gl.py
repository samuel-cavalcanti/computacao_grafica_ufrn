from dataclasses import dataclass
from typing import Any
from OpenGL import GL as gl
# from OpenGL import GLU as glu
from OpenGL import GLUT as glut

import numpy as np


@dataclass
class ArmAngles:
    base_in_degrees: float
    shoulder_in_degrees: float
    elbow_in_degrees: float
    upper_claw_in_degrees: float
    bottom_claw_in_degrees: float


class ArmGL:
    texture_id: int
    arm_id: int
    arm_angles: ArmAngles

    def __init__(self, texture_id: Any) -> None:
        self.arm_angles = ArmAngles(0, 0, 0, 0, 0)
        self.texture_id = texture_id

    def make_arm(self):

        # inicia a composição do braco
        self.arm_id = gl.glGenLists(1)  # Retorna uma lista de exibição vazia
        # Inicia a criação do primeiro (e unico) elemento da display lit
        gl.glNewList(self.arm_id, gl.GL_COMPILE)

        # /* origem posicionada no ombro */

        gl.glRotatef(self.arm_angles.base_in_degrees, 0.0, 1.0, 0.0)
        gl.glRotatef(self.arm_angles.shoulder_in_degrees, 0.0, 0.0, 1.0)

        # /* origem posicionada no centro do braco */
        gl.glTranslatef(1.0, 0.0, 0.0)
        gl.glPushMatrix()

        gl.glScalef(2.0, 0.4, 1.0)
        gl.glColor3f(0.0, 1.0, 1.0)# cyan color
        self.draw_cube(1.0)

        gl.glPopMatrix()

        # /* origem posicionada no cotovelo */
        gl.glTranslatef(1.0, 0.0, 0.0)
        gl.glRotatef(self.arm_angles.elbow_in_degrees, 0.0, 0.0, 1.0)
        gl.glTranslatef(1.0, 0.0, 0.0)
        gl.glPushMatrix()
        gl.glScalef(2.0, 0.4, 1.0)
        gl.glColor3f(0.0, 1.0, 1.0)# cyan color
        self.draw_cube(1.0)
        gl.glPopMatrix()

        # /* origem posicionada no dedo1 */
        gl.glTranslatef(1.0, 0.0, 0.0)
        gl.glPushMatrix()
        gl.glTranslatef(0.0, -0.2, 0.0)
        gl.glRotatef(self.arm_angles.bottom_claw_in_degrees, 0.0, 0.0, 1.0)
        gl.glTranslatef(0.25, 0.0, 0.0)
        gl.glScalef(0.5, 0.1, 0.33)
        gl.glColor3f(0.0, 1.0, 0.0)
        self.draw_cube(1.0)
        gl.glPopMatrix()

    # /* origem posicionada no dedo2 */
        gl.glTranslatef(0.0, 0.2, 0.0)
        gl.glPushMatrix()
        gl.glTranslatef(0.0, 0.0, 0.0)
        gl.glRotatef(self.arm_angles.upper_claw_in_degrees, 0.0, 0.0, 1.0)
        gl.glTranslatef(0.25, 0.0, 0.0)
        gl.glScalef(0.5, 0.1, 0.33)
        gl.glColor3f(0.0, 1.0, 0.0)
        self.draw_cube(1.0)
        gl.glPopMatrix()

        # termina a composição do braco*/
        gl.glEndList()

    def draw_cube(self, size: float):
        n = [
            [-1.0, 0.0, 0.0],  # 0
            [0.0, 1.0, 0.0],  # 1
            [1.0, 0.0, 0.0],  # 2
            [0.0, -1.0, 0.0],  # 3
            [0.0, 0.0, 1.0],  # 4
            [0.0, 0.0, -1.0],  # 5
        ]

        faces = [
            [0, 1, 2, 3],  # 0
            [3, 2, 6, 7],  # 1
            [7, 6, 5, 4],  # 2
            [4, 5, 1, 0],  # 3
            [5, 6, 2, 1],
            [7, 4, 0, 3]
        ]

        n = np.array(n)

        faces = np.array(faces)

        v = np.zeros(shape=(8, 3))

        v[0][0] = v[1][0] = v[2][0] = v[3][0] = -size / 2
        v[4][0] = v[5][0] = v[6][0] = v[7][0] = size / 2
        v[0][1] = v[1][1] = v[4][1] = v[5][1] = -size / 2
        v[2][1] = v[3][1] = v[6][1] = v[7][1] = size / 2
        v[0][2] = v[3][2] = v[4][2] = v[7][2] = -size / 2
        v[1][2] = v[2][2] = v[5][2] = v[6][2] = size / 2

        gl.glPolygonMode(gl.GL_FRONT_AND_BACK, gl.GL_FILL)
        gl.glBindTexture(gl.GL_TEXTURE_2D, self.texture_id)

        for i in [5, 4, 3, 2, 1, 0]:
            gl.glBegin(gl.GL_QUADS)

            gl.glTexCoord2fv([0.0, 0.0])
            gl.glNormal3fv(n[i])  # 0

            gl.glTexCoord2fv([0.5, 0.0])
            gl.glVertex3fv(v[faces[i][0]])  # 1
#
            gl.glTexCoord2fv([1.0, 0.0])
            gl.glVertex3fv(v[faces[i][1]])  # 2

            gl.glTexCoord2fv([0.5, 0.0])
            gl.glVertex3fv(v[faces[i][2]])  # 4

            gl.glTexCoord2fv([1.0, 0.0])
            gl.glVertex3fv(v[faces[i][3]])  # 5

            gl.glEnd()

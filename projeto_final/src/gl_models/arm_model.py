from arm_angles import ArmAngles
from OpenGL import GL as gl
from . import cube_model


def draw_arm(angles: ArmAngles, texture_id: int):
    """Modelo do braço.
     Basicamente são as sequências de matrizes que são enviadas
     ao OpenGL para desenhar o braço com textura.
    """

    # seleciona a textura do braço
    gl.glBindTexture(gl.GL_TEXTURE_2D, texture_id)
    #  os angulos da base e do ombro rotacionam o mesmo cubo, mas em eixos diferentes
    gl.glRotatef(angles.base_in_degrees, 0.0, 1.0, 0.0)
    gl.glRotatef(angles.shoulder_in_degrees, 0.0, 0.0, 1.0)

    #  origem posicionada no centro do braco */
    gl.glTranslatef(1.0, 0.0, 0.0)
    gl.glPushMatrix()

    gl.glScalef(2.0, 0.4, 1.0)
    gl.glColor3f(0.0, 1.0, 1.0)  # cyan color
    cube_model.draw_cube(1.0, texture_id)

    gl.glPopMatrix()

    #  origem posicionada no cotovelo
    gl.glTranslatef(1.0, 0.0, 0.0)
    gl.glRotatef(angles.elbow_in_degrees, 0.0, 0.0, 1.0)
    gl.glTranslatef(1.0, 0.0, 0.0)
    gl.glPushMatrix()
    gl.glScalef(2.0, 0.4, 1.0)
    gl.glColor3f(0.0, 1.0, 1.0)  # cyan color
    cube_model.draw_cube(1.0, texture_id)
    gl.glPopMatrix()

    # o dedo de baixo garra
    gl.glTranslatef(1.0, 0.0, 0.0)
    gl.glPushMatrix()
    gl.glTranslatef(0.0, -0.2, 0.0)
    gl.glRotatef(angles.bottom_claw_in_degrees, 0.0, 0.0, 1.0)
    gl.glTranslatef(0.25, 0.0, 0.0)
    gl.glScalef(0.5, 0.1, 0.33)
    gl.glColor3f(0.0, 1.0, 0.0)
    cube_model.draw_cube(1.0, texture_id)
    gl.glPopMatrix()

    # o dedo de cima garra
    gl.glTranslatef(0.0, 0.2, 0.0)
    gl.glPushMatrix()
    gl.glTranslatef(0.0, 0.0, 0.0)
    gl.glRotatef(angles.upper_claw_in_degrees, 0.0, 0.0, 1.0)
    gl.glTranslatef(0.25, 0.0, 0.0)
    gl.glScalef(0.5, 0.1, 0.33)
    gl.glColor3f(0.0, 1.0, 0.0)
    cube_model.draw_cube(1.0, texture_id)
    gl.glPopMatrix()

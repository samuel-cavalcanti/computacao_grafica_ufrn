from calendar import c
from dataclasses import dataclass
from OpenGL import GL as gl
# from OpenGL import GLU as glu
from OpenGL import GLUT as glut


@dataclass
class ArmAngles:
    base_in_degrees:float
    shoulder_in_degrees: float
    elbow_in_degrees: float
    upper_claw_in_degrees: float
    bottom_claw_in_degrees: float


class ArmGL:

    arm_id: int
    arm_angles:ArmAngles

    def __init__(self) -> None:
        self.arm_angles = ArmAngles(0, 0, 0, 0,0)
      

    def make_arm(self):

        # inicia a composicao do braco
        self.arm_id = gl.glGenLists(1)  # Retorna uma lista de exibicao vazia
        # Inicia a criacao do primeiro (e unico) elemento da display lit
        gl.glNewList(self.arm_id, gl.GL_COMPILE)

        # /* origem posicionada no ombro */
        
        gl.glRotatef(self.arm_angles.base_in_degrees, 0.0, 1.0, 0.0)
        gl.glRotatef(self.arm_angles.shoulder_in_degrees, 0.0, 0.0, 1.0)
        

        # /* origem posicionada no centro do braco */
        gl.glTranslatef(1.0, 0.0, 0.0)
        gl.glPushMatrix()

        gl.glScalef(2.0, 0.4, 1.0)
        gl.glColor3f(0.0, 0.0, 128.0)
        glut.glutSolidCube(1.0)
        gl.glPopMatrix()

        # /* origem posicionada no cotovelo */
        gl.glTranslatef(1.0, 0.0, 0.0)
        gl.glRotatef(self.arm_angles.elbow_in_degrees, 0.0, 0.0, 1.0)
        gl.glTranslatef(1.0, 0.0, 0.0)
        gl.glPushMatrix()
        gl.glScalef(2.0, 0.4, 1.0)
        gl.glColor3f(0.0, 191.0, 255.0)
        glut.glutSolidCube(1.0)
        gl.glPopMatrix()

        # /* origem posicionada no dedo1 */
        gl.glTranslatef(1.0, 0.0, 0.0)
        gl.glPushMatrix()
        gl.glTranslatef(0.0, -0.2, 0.0)
        gl.glRotatef(self.arm_angles.bottom_claw_in_degrees, 0.0, 0.0, 1.0)
        gl.glTranslatef(0.25, 0.0, 0.0)
        gl.glScalef(0.5, 0.1, 0.33)
        gl.glColor3f(0.0, 35.0, 0.0)
        glut.glutSolidCube(1.0)
        gl.glPopMatrix()

    # /* origem posicionada no dedo2 */
        gl.glTranslatef(0.0, 0.2, 0.0)
        gl.glPushMatrix()
        gl.glTranslatef(0.0, 0.0, 0.0)
        gl.glRotatef(self.arm_angles.upper_claw_in_degrees, 0.0, 0.0, 1.0)
        gl.glTranslatef(0.25, 0.0, 0.0)
        gl.glScalef(0.5, 0.1, 0.33)
        gl.glColor3f(0.0, 35.0, 0.0)
        glut.glutSolidCube(1.0)
        gl.glPopMatrix()

        # termina a composicao do braco*/
        gl.glEndList()


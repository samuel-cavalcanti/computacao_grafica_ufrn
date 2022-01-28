from arm_gl import ArmGL
from camera import Camera
from OpenGL import GLUT as glut

class KeyboardController:
    __arm: ArmGL
    __cam:Camera

    def __init__(self, arm: ArmGL,cam:Camera) -> None:
        self.__arm = arm
        self.__cam =cam

    def key_press(self, key: bytes) -> bool:
        arm = self.__arm

        match key.decode():
            case 'A':
                angle = arm.arm_angles.shoulder_in_degrees
                arm.arm_angles.shoulder_in_degrees = 180 if angle >= 180 else angle + 5
                return True
            case 'a':
                angle = arm.arm_angles.shoulder_in_degrees
                arm.arm_angles.shoulder_in_degrees = 0 if angle <= 0 else angle - 5
                return True

            case 'S':
                angle = arm.arm_angles.elbow_in_degrees
                arm.arm_angles.elbow_in_degrees = 135 if angle >= 135 else angle + 5
                return True

            case 's':
                angle = arm.arm_angles.elbow_in_degrees
                arm.arm_angles.elbow_in_degrees = 0 if angle <= 0 else angle - 5
                return True

            case 'B':
                angle = arm.arm_angles.base_in_degrees
                arm.arm_angles.base_in_degrees = 360 if angle >= 360 else angle + 5
                return True

            case 'b':
                angle = arm.arm_angles.base_in_degrees
                arm.arm_angles.base_in_degrees = 0 if angle <= 0 else angle - 5
                return True

            case 'c':
                angle = arm.arm_angles.upper_claw_in_degrees
                arm.arm_angles.upper_claw_in_degrees = -45/2 if angle <= -45/2 else angle - 5
                arm.arm_angles.bottom_claw_in_degrees = -arm.arm_angles.upper_claw_in_degrees
                return True
            case 'C':
                angle = arm.arm_angles.upper_claw_in_degrees
                arm.arm_angles.upper_claw_in_degrees = 0 if angle >= 0 else angle + 5
                arm.arm_angles.bottom_claw_in_degrees = -arm.arm_angles.upper_claw_in_degrees
                return True

        return False

    def special_key_press(self,key:int)->bool:
        camera = self.__cam
        match key:
            case glut.GLUT_KEY_UP:
                camera.obs[1] += +1
                return True

            case glut.GLUT_KEY_DOWN:
                camera.obs[1] -= 1
                return True

            case glut.GLUT_KEY_LEFT:
                camera.tetaxz += 2
                return True

            case glut.GLUT_KEY_RIGHT:
                camera.tetaxz -= 2
                return True
        pass



import unittest

from src.arm_angles import ArmAngles


class ArmAnglesTestCase(unittest.TestCase):

    @staticmethod
    def __gerate_angles_to_test(max_angle: float, min_angle: float) -> tuple[list[float], list[float]]:
        input_angles = [min_angle,
                        max_angle,
                        max_angle - 5,
                        min_angle - 5,
                        max_angle + 5,
                        ]

        expected_angles = [min_angle,
                           max_angle,
                           max_angle - 5,
                           max_angle - 5,
                           max_angle - 5,
                           ]

        return input_angles, expected_angles

    def test_base_angle_limits(self):
        """Testando limites dos os anglos da base"""

        arm_angles = ArmAngles()

        input_angles, expected_angles = self.__gerate_angles_to_test(
            min_angle=0, max_angle=360.0)

        for input_angle, expected_angle in zip(input_angles, expected_angles):
            arm_angles.base_in_degrees = input_angle
            self.__assertAngle(arm_angles.base_in_degrees, expected_angle)

    def __assertAngle(self, result: float, expected: float):
        self.assertEqual(
            result, expected, msg=f"Base angle should be {expected}, base angle : {result}")

    def test_shoulder_angle_limits(self):
        """Testando limites dos os anglos do ombro"""
        arm_angles = ArmAngles()

        input_angles, expected_angles = self.__gerate_angles_to_test(
            min_angle=0, max_angle=180)

        for input_angle, expected_angle in zip(input_angles, expected_angles):
            arm_angles.shoulder_in_degrees = input_angle
            self.__assertAngle(arm_angles.shoulder_in_degrees, expected_angle)

    def test_elbow_angle_limits(self):
        """Testando limites dos os anglos do cotovelo"""

        arm_angles = ArmAngles()

        input_angles, expected_angles = self.__gerate_angles_to_test(
            min_angle=0, max_angle=135)

        for input_angle, expected_angle in zip(input_angles, expected_angles):
            arm_angles.elbow_in_degrees = input_angle
            self.__assertAngle(arm_angles.elbow_in_degrees, expected_angle)

    def test_claw_angle_limits(self):
        """Testando limites dos os anglos da garra"""
        arm_angles = ArmAngles()

        input_angles, expected_angles = self.__gerate_angles_to_test(
            min_angle=0, max_angle=17)

        for input_angle, expected_angle in zip(input_angles, expected_angles):
            arm_angles.set_angle_claw(input_angle)
            self.__assertAngle(arm_angles.bottom_claw_in_degrees, expected_angle)
            self.__assertAngle(arm_angles.upper_claw_in_degrees, -expected_angle)

    

"""

    def base_in_degrees(self) -> float:
        return self.__base_in_degrees

    @property
    def shoulder_in_degrees(self) -> float:
        return self.__shoulder_in_degrees

    @property
    def elbow_in_degrees(self) -> float:
        return self.__elbow_in_degrees

"""

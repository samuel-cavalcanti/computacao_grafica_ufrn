import numpy as np


def degree_to_rads(angle_in_degree: float) -> float:
    return np.pi/180 * angle_in_degree


def rads_to_degree(rads: float) -> float:
    return 180/np.pi*rads


def rotate_x(angle_in_degree: float) -> np.ndarray:

    angle_in_radians = degree_to_rads(angle_in_degree)

    return np.array([
        [1, 0, 0],
        [0, np.cos(angle_in_radians), -np.sin(angle_in_radians)],
        [0, np.sin(angle_in_radians), np.cos(angle_in_radians)],
    ])


def rotate_y(angle_in_degree: float) -> np.ndarray:

    angle_in_radians = degree_to_rads(angle_in_degree)

    return np.array([
        [np.cos(angle_in_radians), 0, np.sin(angle_in_radians)],
        [0, 1, 0],
        [-np.sin(angle_in_radians), 0, np.cos(angle_in_radians)],
    ])


def rotate_z(angle_in_degree: float) -> np.ndarray:

    angle_in_radians = degree_to_rads(angle_in_degree)

    return np.array([
        [np.cos(angle_in_radians), -np.sin(angle_in_radians), 0],
        [np.sin(angle_in_radians), np.cos(angle_in_radians), 0],
        [0, 0, 1],
    ])


def question_9():
    p1 = np.array([2, 1, 1])

    x_matrix = rotate_x(60)
    y_matrix = rotate_y(45)
    z_matrix = rotate_z(30)

    print(f"x: \n{x_matrix}", end='\n\n')

    print(f"y: \n{y_matrix}", end='\n\n')

    print(f"z: \n{z_matrix}", end='\n\n')

    result_matrix = np.dot(z_matrix, np.dot(y_matrix, x_matrix))

    print(f"result_matrix: \n{result_matrix}", end='\n\n')

    p2 = np.dot(result_matrix, p1)
    print(f"p2: {p2}")

    p2 = np.dot(z_matrix, np.dot(y_matrix, np.dot(x_matrix, p1)))

    print(f"p2: {p2}")

    p_0 = np.array([3, -4, 5])

    print(f"p2 + (+3, -4, +5): {p2 + p_0}")


def main():

    test_rotation()
    # question_9()

    # theta_in_rads = np.arccos(-1/2)

    # print(rads_to_degree(theta_in_rads))


def test_rotation():

    x = rotate_x(180)
    y = rotate_y(0)
    z = rotate_z(0)

    result = np.dot(np.dot(x,y),z)

    print(result)



if __name__ == '__main__':
    main()

import cv2
import numpy as np

from typing import Tuple

'''
https://docs.opencv.org/3.4/d2/d2c/tutorial_sobel_derivatives.html
'''


def sobel(image: np.ndarray, gradient: Tuple[int, int]):

    grad = cv2.Sobel(image, cv2.CV_16S, dx=gradient[0], dy=gradient[1], ksize=3,
                     scale=1, delta=0, borderType=cv2.BORDER_DEFAULT)

    return grad


def main():

    image = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0],
        [0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0],
        [0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0],
        [0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0],
        [0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0],
        [0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0],
        [0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0],
        [0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

    image = 255 * np.array(image, dtype=np.uint8)

    sobel_x = sobel(image, (1, 0))

    sobel_y = sobel(image, (0, 1))

    abs_sobel_x = cv2.convertScaleAbs(sobel_x)
    abs_sobel_y = cv2.convertScaleAbs(sobel_y)

    print('sobel X', end='\n\n')
    print(sobel_x)

    print('sobel Y', end='\n\n')
    print(sobel_y)

    cv2.imshow('image', image)

    cv2.imshow(' Magnitude Sobel X', abs_sobel_x)
    cv2.imshow('Magnitude Sobel Y', abs_sobel_y)

    cv2.imshow('Magnitude Sobel X + Y', abs_sobel_x + abs_sobel_y)
    cv2.waitKey(0)


if __name__ == '__main__':
    main()

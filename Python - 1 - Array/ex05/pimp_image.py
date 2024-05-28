import matplotlib.pyplot as plt
import numpy as np
from load_image import ft_load
import cv2


def ft_invert(array):
    '''Inverts the color of the image received.'''

    matrix = np.array(array)

    matrix[:, :, 0] = 255 - matrix[:, :, 0]
    matrix[:, :, 1] = 255 - matrix[:, :, 1]
    matrix[:, :, 2] = 255 - matrix[:, :, 2]

    plt.imshow(matrix)

    plt.show()


def ft_red(array):
    '''Removes the green and blue colors from the image received.'''

    matrix = np.array(array)

    matrix[:, :, 1:] = 0

    plt.imshow(matrix)
    plt.show()


def ft_green(array):
    '''Removes the red and blue colors from the image received.'''

    matrix = np.array(array)

    matrix[:, :, 0] = 0
    matrix[:, :, 2] = 0

    plt.imshow(matrix)
    plt.show()


def ft_blue(array):
    '''Removes the red and green colors from the image received.'''

    matrix = np.array(array)

    matrix[:, :, :2] = 0

    plt.imshow(matrix)
    plt.show()


def ft_grey(array):
    ''''''

    matrix = np.array(array)

    gray = cv2.cvtColor(matrix, cv2.COLOR_BGR2GRAY)

    plt.imshow(gray)
    plt.show()


def main():
    '''Main'''

    array = ft_load("landscape.jpg")

    # ft_invert(array)
    # ft_red(array)
    # ft_green(array)
    # ft_blue(array)
    ft_grey(array)


if __name__ == "__main__":
    main()
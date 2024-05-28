import matplotlib.image as mpimg
import matplotlib.pyplot as plt
from PIL import Image
import numpy as np
from load_image import ft_load


def ft_invert(array):
    '''Inverts the color of the image received.'''

    matrix = np.array(array)

    matrix[:, :, 0] = 0
    plt.imshow(matrix, cmap="gray")

    plt.title("Animal")
    plt.show()


# def ft_red(array) -> array:

# def ft_green(array) -> array:

# def ft_blue(array) -> array:

# def ft_grey(array) -> array:


def main():
    '''Main'''

    array = ft_load("landscape.jpg")
    ft_invert(array)

    # ft_red(array)
    # ft_green(array)
    # ft_blue(array)
    # ft_grey(array)

if __name__ == "__main__":
    main()
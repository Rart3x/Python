import matplotlib.image as mpimg
import numpy as np
from zoom import display


def ft_load(path: str) -> []:
    '''Load image'''

    try:
        img = mpimg.imread(path)
    except IOError:
        print(f"Error: opening image path '{path}'")
        exit()

    image_arr = np.array(img)
    height, width, mode = image_arr.shape

    print("The shape of image is :", f"({width}, {height}, {mode})")

    return img


def main():
    '''Main'''

    print(ft_load("animal.jpeg"))
    display("animal.jpeg")


if __name__ == "__main__":
    main()

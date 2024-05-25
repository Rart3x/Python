import numpy as np
import matplotlib.image as mpimg


def ft_load(path: str) -> []:
    '''Load image'''

    arr = []

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

    print(ft_load("landscape.jpg"))


if __name__ == "__main__":
    main()

import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from PIL import Image
import numpy as np


def get_image_as_arr(path: str):
    '''Return arr that contain all image [RGB]'''

    arr = []

    try:
        img = Image.open(path)
    except IOError:
        print(f"Error: opening image path '{path}'")
        exit()

    image_arr = np.array(img)
    height, width, mode = image_arr.shape

    for y in range(height):
        row = []
        for x in range(width):
            r, g, b = img.getpixel((x, y))
            row.append([r, g, b])
        arr.append(row)

    return arr, height, width


def display(path: str) -> None:
    '''Display image'''

    img = mpimg.imread(path)
    img2 = img[:, :, 1]

    plt.imshow(img2, cmap="gray")

    plt.ylim(100, 500)
    plt.xlim(850, 450)

    plt.title("Animal")
    plt.show()


def display_rotated(path: str) -> None:
    '''Rotation function'''

    arr, height, width = get_image_as_arr(path)

    display(path)


def main():
    '''Main'''


if __name__ == "__main__":
    main()

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


def zoom(arr: np.array) -> np.array:
    '''Zoom function'''

    new_arr = []

    for y in range(500, 100):
        row = []
        for x in range(850, 450):
            row.append(arr[y][x])
        new_arr.append(row)

    return np.array(new_arr)


def display_zoomed(path: str) -> None:
    '''Display image'''

    img = mpimg.imread(path)
    img = zoom(img)
    img2 = img[:, :, 1]

    print("\nNew shape after slicing: ", img2.shape)
    print(img2)

    plt.imshow(img2, cmap="gray")

    plt.title("Animal")
    plt.show()


def display(path: str) -> None:
    '''Zoom function'''

    arr, height, width = get_image_as_arr(path)
    display_zoomed(path)


def main():
    '''Main'''


if __name__ == "__main__":
    main()

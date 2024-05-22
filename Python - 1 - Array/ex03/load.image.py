from PIL import Image
import numpy as np

from zoom import display_zoomed


def ft_load(path: str) -> []:
    '''Load image'''

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

    print("The shape of image is :", f"({width}, {height}, {mode})")

    return arr


def main():
    '''Main'''

    print(ft_load("animal.jpeg"))
    display_zoomed("animal.jpeg")


if __name__ == "__main__":
    main()

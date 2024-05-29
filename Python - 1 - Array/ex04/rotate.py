import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
import cv2
from load_image import ft_load


def rotate_l(arr: np.array) -> np.array:
    '''
    Manually rotates an image 90 degrees to the left.
    '''

    matrix = np.array(arr)
    height, width, mode = matrix.shape

    new_arr = np.empty((width, height, mode), dtype=np.uint8)

    for i, r in enumerate(matrix):
        new_arr[:, i] = matrix[i]

    return new_arr


def zoom(arr: np.array) -> np.array:
    '''Zoom function'''

    new_arr = []

    for y in range(100, 500):
        row = []
        for x in range(450, 850):
            row.append(arr[y][x])
        new_arr.append(row)

    return np.array(new_arr)


def display(path: str) -> None:
    '''Display image'''

    try:
        img = mpimg.imread(path)
    except IOError:
        print(f"Error: opening image path '{path}'")
        exit()

    img_resized = zoom(img)

    height, width, mode = img_resized.shape

    img_resized = rotate_l(img_resized)
    gray_img = cv2.cvtColor(img_resized, cv2.COLOR_BGR2GRAY)

    print(
        f"\nNew shape after Transpose: "
        f"{width}, {height}, {mode} or "
        f"{gray_img.shape}"
    )
    print(gray_img)

    plt.imshow(gray_img, cmap="gray")

    plt.title("Animal")
    plt.show()


def main():
    '''Main'''

    print(ft_load("animal.jpeg"))
    display("animal.jpeg")


if __name__ == "__main__":
    main()

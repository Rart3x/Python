import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np


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

    img = mpimg.imread(path)
    img = zoom(img)

    height, width, mode = img.shape

    img2 = img[:, :, 1]

    print(f"\nNew shape after slicing: {width, height, mode} or {img2.shape}")
    print(img2)

    plt.imshow(img2, cmap="gray")

    plt.title("Animal")
    # plt.show()


def main():
    '''Main'''


if __name__ == "__main__":
    main()

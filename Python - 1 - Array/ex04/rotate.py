import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
import cv2


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
    img_resized = zoom(img)

    height, width, mode = img_resized.shape

    gray_img = cv2.cvtColor(img_resized, cv2.COLOR_BGR2GRAY)

    print(f"\nNew shape after conversion: {width, height, mode} or {gray_img.shape}")
    print(gray_img)

    plt.imshow(gray_img, cmap="gray")

    plt.title("Animal")
    plt.show()


def main():
    '''Main'''


if __name__ == "__main__":
    main()

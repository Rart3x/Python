import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
import cv2


def rotate_l(arr: np.array) -> np.array:
    """
    Manually rotates an image 90 degrees to the left.

    Parameters:
    - arr: A 2D numpy array representing the image.

    Returns:
    - The left-rotated image as a 2D numpy array.
    """
    # Initialize an empty array with the same shape
    # as the input array to store the inverted rows
    inverted_rows = np.zeros_like(arr)

    # Iterate over each row of the input array
    for y in range(arr.shape[0]):
        # Iterate over each element within the current row
        for x in range(arr.shape[1]):
            # Assign the value of the element at the mirrored
            # position in the last row to the current position
            inverted_rows[y, :] = arr[arr.shape[0]-1-y, :]

    # Initialize another empty array with the same shape
    # as the inverted rows to store the transposed image
    transposed = np.zeros_like(inverted_rows)

    # Iterate over each row of the inverted rows array
    for y in range(inverted_rows.shape[0]):
        # Iterate over each element within the current row
        for x in range(inverted_rows.shape[1]):
            # Assign the value of the element at
            # the corresponding position in the transposed array
            transposed[x, y] = inverted_rows[y, x]

    # Initialize yet another empty array with the same shape
    # as the transposed array to store the final rotated image
    rotated = np.zeros_like(transposed)

    # Iterate over each row of the transposed array
    for y in range(transposed.shape[0]):
        # Iterate over each element within the current row
        for x in range(transposed.shape[1]):
            # Assign the value of the element at the reversed position
            # in the current row to the final rotated image
            rotated[y, :] = transposed[y, ::-1]

    # Return the final rotated image
    return rotated


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

    img_resized = rotate_l(img_resized)

    gray_img = cv2.cvtColor(img_resized, cv2.COLOR_BGR2GRAY)

    print(
        f"\nNew shape after conversion: "
        f"{width}, {height}, {mode} or "
        f"{gray_img.shape}"
    )
    print(gray_img)

    plt.imshow(gray_img, cmap="gray")

    plt.title("Animal")
    plt.show()


def main():
    '''Main'''


if __name__ == "__main__":
    main()

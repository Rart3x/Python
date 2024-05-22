import matplotlib.pyplot as plt
import matplotlib.image as mpimg


def display(path: str) -> None:
    '''Display image'''

    img = mpimg.imread(path)
    plt.imshow(img)
    plt.title("Animal")
    plt.show()


def display_zoomed(path: str) -> None:
    '''Zoom function'''

    display(path)


def main():
    '''Main'''


if __name__ == "__main__":
    main()

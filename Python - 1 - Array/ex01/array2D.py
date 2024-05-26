import numpy as np


def slice_me(family: list, start: int, end: int) -> list:
    '''Print array shape and truncate from start to index'''

    try:
        assert (
            start >= 0
            and start < len(family)
            and end < len(family)
        ), "start and end must be valid indexes"
    except AssertionError:
        print("AssertionError: start and end must be valid indexes")
        exit()

    try:
        assert isinstance(family, list), "family must be a list"
    except AssertionError:
        print("AssertionError: family must be a list")
        exit()

    a = np.array(family)
    print(f"My shape is {a.shape}")

    x = slice(start, end)
    a = np.array(family[x])

    print(f"My new shape is {a.shape}")

    return a


def main():
    '''Main'''

    family = [
        [1.80, 78.4],
        [2.15, 102.7],
        [2.10, 98.5],
        [1.88, 75.2]
    ]

    print(slice_me(family, 0, 2))
    print(slice_me(family, 1, -2))


if __name__ == "__main__":
    main()

import numpy as np


def slice_me(family: list, start: int, end: int) -> list:
    '''Print array shape and truncate from start to index'''

    try:
        assert (
            start >= 0
            and start < len(family)
            and end < len(family)
            and start < end
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


if __name__ == "__main__":
    main()

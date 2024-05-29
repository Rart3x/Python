def give_bmi(
    height: list[int | float],
    weight: list[int | float]
) -> list[int | float]:

    '''Calculate BMI'''

    try:
        assert len(height) == len(weight), "List must have the same size"
    except AssertionError:
        print("AssertionError: List must have the same size")
        exit()

    for h, w in zip(height, weight):
        try:
            assert (isinstance(h, float) or isinstance(h, int)), (
                "All elements must be floats or int"
            )
        except AssertionError:
            print("AssertionError: All elements must be floats or int")
            exit()
        try:
            assert (isinstance(w, float) or isinstance(w, int)), (
                "All elements must be floats or int"
            )
        except AssertionError:
            print("AssertionError: All elements must be floats or int")
            exit()

    arr = []

    for i in range(len(height)):
        arr.append(weight[i] / (height[i] ** 2))

    return arr


def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    '''True if an element is above limit value, otherwise False'''

    for b in bmi:
        try:
            assert isinstance(b, float) or isinstance(b, int), (
                "All elements in height must be floats or int"
            )
        except AssertionError:
            print("AssertionError: All elements must be floats or int")
            exit()

    arr = []

    for i in range(len(bmi)):
        if bmi[i] > limit:
            arr.append(True)
        else:
            arr.append(False)

    return arr


def main():
    '''Main'''


if __name__ == "__main__":
    main()

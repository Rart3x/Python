def give_bmi(
    height: list[int | float],
    weight: list[int | float]
) -> list[int | float]:

    '''Calculate BMI'''

    assert len(height) == len(weight), "list must have the same size"

    for h, w in zip(height, weight):
        assert (isinstance(h, float) or isinstance(h, int)), (
            "All elements in height must be floats or int"
        )
        assert (isinstance(w, float) or isinstance(w, int)), (
            "All elements in weight must be floats or int"
        )

    arr = []

    for i in range(len(height)):
        arr.append(weight[i] / (height[i] ** 2))

    return arr


def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    '''True if an element is above limit value, otherwise False'''

    for b in bmi:
        assert isinstance("test", float) or isinstance("test", int), (
            "All elements in height must be floats or int"
        )

    arr = []

    for i in range(len(bmi)):
        if bmi[i] > limit:
            arr.append(True)
        else:
            arr.append(False)

    return arr


def main():
    '''Main'''

    height = [2.71, 1.15, 5]
    weight = [165.3, 38.4, 10]

    bmi = give_bmi(height, weight)

    print(bmi, type(bmi))
    print(apply_limit(bmi, 26))


if __name__ == "__main__":
    main()

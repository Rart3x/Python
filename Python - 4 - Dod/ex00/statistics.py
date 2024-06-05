def mean(vec: []) -> None:
    '''Mean method'''

    if len(vec) == 0:
        return print("ERROR")

    total = 0

    for i in vec:
        total += i
    print("mean :", total / len(vec))


def median(vec: []) -> None:
    '''Median method'''

    if len(vec) == 0:
        return print("ERROR")

    vec.sort()

    if len(vec) % 2 == 0:
        median = (vec[len(vec) // 2 - 1] + vec[len(vec) // 2]) / 2
    else:
        median = vec[len(vec) // 2]

    print("median :", median)


def quartile(vec: list) -> None:
    '''Quartile method'''

    if len(vec) == 0:
        return print("ERROR")

    vec.sort()
    n = len(vec)

    q1_i = n // 4
    q1 = vec[q1_i] if n % 4 != 0 else (vec[q1_i - 1] + vec[q1_i]) / 2

    q3_i = n // 4 * 3
    q3 = vec[q3_i] if n % 4 != 0 else (vec[q3_i - 1] + vec[q3_i]) / 2

    new_vec = []

    new_vec.append(float(q1))
    new_vec.append(float(q3))

    print("quartile :", new_vec)


def std(vec: list) -> None:
    '''Std method'''

    if len(vec) == 0:
        return print("ERROR")

    mean = sum(vec) / len(vec)
    variance = sum((x - mean) ** 2 for x in vec) / len(vec)

    print("std :", variance ** 0.5)


def var(vec: list) -> None:
    '''Var method'''

    if len(vec) == 0:
        return print("ERROR")

    mean = sum(vec) / len(vec)
    print("var :", sum((x - mean) ** 2 for x in vec) / len(vec))


def ft_statistics(*args: any, **kwargs: any) -> None:
    '''Ft_statistics method'''

    vec = []
    tmp = []

    for arg in args:
        vec.append(arg)

    for arg in kwargs:
        tmp.append(arg)

    for arg in tmp:
        if kwargs[arg] == "mean":
            mean(vec)
        if kwargs[arg] == "median":
            median(vec)
        if kwargs[arg] == "quartile":
            quartile(vec)
        if kwargs[arg] == "std":
            std(vec)
        if kwargs[arg] == "var":
            var(vec)

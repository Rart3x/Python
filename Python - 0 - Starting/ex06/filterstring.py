from sys import argv

def isstr(arg: any) -> bool:
    '''Isalpha() including spaces'''

    for i in arg:
        if i != ' ':
            if not i.isalpha():
                return False
    return True


def check_args(argv: list) -> tuple:
    '''Check args conformity'''

    string = None
    integer = None

    assert len(argv) == 3, "The arguments are bad"

    for i in argv:
        if i.isdigit():
            integer = int(i)
        elif isstr(i):
            string = i

    assert string is not None and integer is not None, "The arguments are bad"

    return (string, integer)


def output(argv: list, tup: tuple) -> None:
    '''Output'''

    arr = tup[0].split(' ')
    final_arr = [i for i in arr if len(i) > tup[1]]

    print(final_arr)


def main():
    '''Main'''

    tup = check_args(argv)
    output(argv, tup)


if __name__ == "__main__":
    main()

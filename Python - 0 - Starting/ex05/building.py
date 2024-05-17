import sys


def check_args(argv):
    '''Check input confirmity'''

    if (len(argv) < 2):
        return (input("What is the text to count\n"))
    assert len(argv) == 2, "Please provide a simple string"

    return None


def count_carac(str):
    '''Count each type of caracters'''

    upper = 0
    lower = 0
    punctuation = 0
    digit = 0
    space = 0
    total = 0

    arr = [upper, lower, punctuation, digit, space, total]

    for c in str:
        match c:
            case _ if c.isupper():
                arr[0] += 1
            case _ if c.islower():
                arr[1] += 1
            case _ if c.isdigit():
                arr[3] += 1
            case _ if c.isspace():
                arr[4] += 1
            case _:
                arr[2] += 1
        arr[5] += 1
    return arr


def print_nb_carac(arr) -> []:
    '''Print the final prompt with number of each type of caracters'''

    print("The text contains", arr[5], "characteres:")
    print(arr[0], "upper letters")
    print(arr[1], "lower letters")
    print(arr[2], "punctuation marks")
    print(arr[4], "spaces")
    print(arr[3], "digits")


def main():
    '''Main'''

    arg = check_args(sys.argv)
    if arg is None:
        print_nb_carac(count_carac(sys.argv[1]))
    else:
        print_nb_carac(count_carac(arg))


if __name__ == "__main__":
    main()

import sys


def check_args(argv):
    '''Check the arguments'''

    str_bool = 0
    int_bool = 0

    assert len(argv) == 3, "the arguments are bad"

    if argv[1].isdigit() or argv[2].isdigit():
        int_bool = 1

    if argv[1].isalpha() or argv[2].isalpha():
        str_bool = 1

    print("str_bool: ", str_bool)
    print("int_bool: ", int_bool)
    
    assert str_bool == 1 and int_bool == 1, "the arguments are bad"


def main():
    '''Main'''

    check_args(sys.argv)


if __name__ == "__main__":
    main()

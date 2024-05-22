from sys import sys


def isstr(arg: any) -> bool:
    '''Isalpha() including spaces'''

    for i in arg:
        if i != ' ':
            if not i.isalpha() and not i.isdigit():
                return False
    return True


def check_args(argv: list) -> tuple:
    '''Check args conformity'''

    try:
        assert len(argv) == 2, "The arguments are bad"
    except AssertionError:
        print("AssertionError: The arguments are bad")

    str_bool = isstr(argv[1])

    try:
        assert str_bool is True, "The arguments are bad"
    except AssertionError:
        print("AssertionError: The arguments are bad")


def fill_dict() -> dict:
    '''Fill the Morse code dictionary'''

    morse_code = {
        'A': '.-',       'B': '-...',     'C': '-.-.',     'D': '-..',
        'E': '.',        'F': '..-.',     'G': '--.',      'H': '....',
        'I': '..',       'J': '.---',     'K': '-.-',      'L': '.-..',
        'M': '--',       'N': '-.',       'O': '---',      'P': '.--.',
        'Q': '--.-',     'R': '.-.',      'S': '...',      'T': '-',
        'U': '..-',      'V': '...-',     'W': '.--',      'X': '-..-',
        'Y': '-.--',     'Z': '--..',     ' ': '/',
        '0': '-----',    '1': '.----',    '2': '..---',    '3': '...--',
        '4': '....-',    '5': '.....',    '6': '-....',    '7': '--...',
        '8': '---..',    '9': '----.'
    }

    return morse_code


def convert_to_morse_code(text: str) -> str:
    '''Convert text to morse code'''

    morse_code = fill_dict()
    morse_text = ""

    for char in text:
        morse_text += morse_code[char.upper()]

    return morse_text


def main():
    '''Main'''

    check_args(sys.argv)
    print(convert_to_morse_code(sys.argv[1]))


if __name__ == "__main__":
    main()

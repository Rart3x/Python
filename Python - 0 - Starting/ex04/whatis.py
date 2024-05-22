from sys import argv


if (len(argv) == 1):
    exit(1)

try:
    assert len(argv) < 3, "more than one argument is provided"
except AssertionError:
    print("AssertionError: more than one argument is provided")
    exit()

try:
    value = int(argv[1])
except ValueError:
    value = "error"

try:
    assert value != "error", "argument is not an integer"
except AssertionError:
    print("AssertionError: argument is not an integer")
    exit()

if (int)(argv[1]) >= 0:
    print("I'm Even.")
else:
    print("I'm Odd.")

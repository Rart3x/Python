import sys

if (len(sys.argv) == 1):
    exit(1)

assert len(sys.argv) < 3, "more than one argument is provided"

try:
    value = int(sys.argv[1])
except ValueError:
    value = "error"

assert value != "error", "argument is not an integer"

if (int)(sys.argv[1]) >= 0:
    print("I'm Even.")
else:
    print("I'm Odd.")
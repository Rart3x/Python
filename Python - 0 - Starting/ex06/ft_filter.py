def ft_filter(function, iterable):
    '''filter(function or None, iterable) --> filter object

Return an iterator yielding those items of iterable for which function(item)
is true. If function is None, return the items that are true.'''

    arr = []
    for i in iterable:
        if function(i) is True:
            arr.append(i)
    return iter(arr)


def test(c):
    return c.isdigit()


def main():
    arr = [' ', '\n', '1', ' ', 'x', '2']

    print(ft_filter.__doc__)
    print(filter.__doc__)

    print((list)(ft_filter(test, arr)))
    print((list)(filter(test, arr)))


if __name__ == "__main__":
    main()

def square(x: int | float) -> int | float:
    '''Square method'''

    return x * x


def pow(x: int | float) -> int | float:
    '''Pow method'''

    return x ** x


def outer(x: int | float, function) -> object:
    '''Outter method'''

    def inner() -> float:
        '''Inner method'''

        nonlocal x
        result = function(x)
        x = result

        return result
    return inner

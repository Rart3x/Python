def callLimit(limit: int):
    '''Call limit function'''

    count = 0

    def callLimiter(function):
        '''Call limiter function'''

        def limit_function(*args: any, **kwds: any):
            '''Limit function'''

            nonlocal count

            if count != limit:
                count += 1
                return function(*args, **kwds)
            else:
                print("Error:", function, "call to many times")
        return limit_function
    return callLimiter

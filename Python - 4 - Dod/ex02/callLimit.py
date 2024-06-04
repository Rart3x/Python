def callLimit(limit: int):
    count = 0
    def callLimiter(function):
        def limit_function(*args: any, **kwds: any):
            nonlocal count

            if count != limit:
                count += 1
                return function(*args, **kwds)
            else:
                print("Error:", function, "call to many times")
        return limit_function
    return callLimiter

@callLimit(3)
def f():
    print ("f()")

@callLimit(1)
def g():
    print ("g()")

for i in range(3):
    f()
    g()
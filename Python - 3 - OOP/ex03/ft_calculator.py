class calculator:
    '''Calculator class'''

    def __init__(self, vec):
        '''Calculator Constructor'''

        for i in range(len(vec)):
            if (isinstance(vec[i], float) or isinstance(vec[i], int)):
                continue
            else:
                print("Error: Vector values must be float or integer")
                exit()

        self.vec = vec

    def __add__(self, object) -> None:
        '''Calculator Overload for +'''

        if (isinstance(object, float) or isinstance(object, int)):
            for i in range(len(self.vec)):
                self.vec[i] += object
            print(self.vec)
        else:
            print("Error: arguments must be float or integer")

    def __mul__(self, object) -> None:
        '''Calculator Overload for *'''

        if (isinstance(object, float) or isinstance(object, int)):
            for i in range(len(self.vec)):
                self.vec[i] *= object
            print(self.vec)
        else:
            print("Error: arguments must be float or integer")

    def __sub__(self, object) -> None:
        '''Calculator Overload for -'''

        if (isinstance(object, float) or isinstance(object, int)):
            for i in range(len(self.vec)):
                self.vec[i] -= object
            print(self.vec)
        else:
            print("Error: arguments must be float or integer")

    def __truediv__(self, object) -> None:
        '''Calculator Overload for /'''

        if (isinstance(object, float) or isinstance(object, int)):
            for i in range(len(self.vec)):
                self.vec[i] /= object
            print(self.vec)
        else:
            print("Error: arguments must be float or integer")

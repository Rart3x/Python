from abc import ABC, abstractmethod


class Character(ABC):
    '''Abstract Character Class'''

    @abstractmethod
    def __init__(self, first_name, is_alive=True):
        '''Character Constructor'''

        self.first_name = first_name
        self.is_alive = is_alive

    def __str__(self):
        '''Character __str__ method'''

        return f"Vector: ({self.eyes}, {self.hairs})"

    def __repr__(self):
        '''Character __repr__ method'''

        return self.__str__()

    def die(self):
        '''Character die method'''

        pass


class Stark(Character):
    '''Stark Class'''

    def __init__(self, first_name, is_alive=True):
        '''Stark Constructor'''

        self.first_name = first_name
        self.is_alive = is_alive

    def die(self):
        '''Stark die method'''

        self.is_alive = False

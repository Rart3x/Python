from abc import ABC, abstractmethod


class Character(ABC):
    '''Abstract Character Class'''

    @abstractmethod
    def __init__(self, first_name, is_alive=True):
        '''Character Constructor'''

        self.first_name = first_name
        self.is_alive = is_alive

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

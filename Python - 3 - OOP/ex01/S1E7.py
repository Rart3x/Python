from S1E9 import Character


class Baratheon(ABC):
    '''Baratheon Character Class'''

    def __init__(self, first_name, is_alive=True):
        '''Baratheon Constructor'''

        self.first_name = first_name
        self.is_alive = is_alive

    def die(self):
        pass


class Lannister(Character):
    '''Lannister Class'''

    def __init__(self, first_name, is_alive=True):
        '''Lannister Constructor'''

        self.first_name = first_name
        self.is_alive = is_alive

    def die(self):
        '''Lannister die function'''

        self.is_alive = not self.is_alive

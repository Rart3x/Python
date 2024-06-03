from S1E9 import Character


class Baratheon(Character):
    '''Baratheon Character Class'''

    def __init__(self, first_name, is_alive=True):
        '''Baratheon Constructor'''

        super().__init__(first_name, is_alive)
        self.family_name = "Baratheon"
        self.eyes = "brown"
        self.hairs = "dark"

    def __str__(self):
        '''Character __str__ method'''

        return f"Vector: ('{self.family_name}', '{self.eyes}', '{self.hairs}')"

    def __repr__(self):
        '''Character __repr__ method'''

        return self.__str__()

    def die(self):
        '''Baratheon die method'''

        self.is_alive = False


class Lannister(Character):
    '''Lannister Class'''

    def __init__(self, first_name, is_alive=True):
        '''Lannister Constructor'''

        super().__init__(first_name, is_alive)
        self.family_name = "Lannister"
        self.eyes = "blue"
        self.hairs = "light"

    def __str__(self):
        '''Character __str__ method'''

        return f"Vector: ('{self.family_name}', '{self.eyes}', '{self.hairs}')"

    def __repr__(self):
        '''Character __repr__ method'''

        return self.__str__()

    def die(self):
        '''Lannister die method'''

        self.is_alive = False

    @classmethod
    def create_lannister(cls, first_name, is_alive=True):
        '''Lannister create_lannister method'''

        new_instance = cls(first_name)
        new_instance.is_alive = is_alive
        return new_instance

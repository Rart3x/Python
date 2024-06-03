from S1E7 import Baratheon, Lannister


class King(Baratheon, Lannister):

    def __init__(self, first_name, is_alive=True):
        '''King Constructor'''

        super().__init__(first_name, is_alive)
        self.family_name = "Baratheon"
        self.eyes = "brown"
        self.hairs = "dark"

    def __str__(self):
        '''King __str__ method'''

        return f"Vector: ('{self.family_name}', '{self.eyes}', '{self.hairs}')"

    def __repr__(self):
        '''King __repr__ method'''

        return self.__str__()

    def die(self):
        '''King die method'''

        self.is_alive = False

    def get_eyes(self):
        return self.eyes

    def get_hairs(self):
        return self.hairs

    def set_eyes(self, eye):
        self.eyes = eye

    def set_hairs(self, hair):
        self.hairs = hair

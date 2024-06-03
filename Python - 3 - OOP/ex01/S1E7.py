from S1E9 import Character


class Baratheon(Character):
    '''Baratheon Character Class'''

    def __init__(self, first_name, is_alive=True):
        '''Baratheon Constructor'''

        super().__init__(first_name, is_alive)
        self.family_name = "Baratheon"
        self.eyes = "brown"
        self.hairs = "dark"


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


    def die(self):
        '''Lannister die method'''
        
        self.is_alive = False


    @classmethod
    def create_lannister(cls, first_name, is_alive=True):
        '''Lannister create_lannister method'''

        new_instance = cls(first_name)
        new_instance.is_alive = is_alive
        return new_instance


Robert = Baratheon("Robert")
print(Robert.__dict__)
print(Robert.__str__)
print(Robert.__repr__)
print(Robert.is_alive)
Robert.die()
print(Robert.is_alive)
print(Robert.__doc__)
print("---")
Cersei = Lannister("Cersei")
print(Cersei.__dict__)
print(Cersei.__str__)
print(Cersei.is_alive)
print("---")
Jaine = Lannister.create_lannister("Jaine", True)
print(f"Name : {Jaine.first_name, type(Jaine).__name__}, Alive : {Jaine.is_alive}")
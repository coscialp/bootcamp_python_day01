class GotCharacter:

    first_name: str
    is_alive: bool

    def __init__(self, name: str, is_alive: bool = True):
        self.first_name = name
        self.is_alive = is_alive


class Stark(GotCharacter):
    """A class representing the Stark family. Or when bad things happen to good people."""
    def __init__(self, first_name: str = None, is_alive: bool = True):
        super().__init__(first_name, is_alive)
        self.family_name = 'Stark'
        self.house_word = 'Winter is coming'

    def print_house_words(self):
        print(self.house_word)

    def die(self):
        self.is_alive = False

'''
oop_encapsulation_with_properties.py

Use properties to encapsulate attributes, don't use setter and getter functions

'''


class BaseballPlayer:
    def __init__(self, new_name="Unknown", new_position="Utility"):
        self.name = new_name  # this is actually calling @name.setter function!
        self.position = new_position  # same here but with @position.setter

    # these functions are decorated to be used as setters and getters
    # instead of accessing the attributes, the functions are called
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, new_name):
        if new_name == '':
            new_name = 'Unknown'
        self.__name = new_name

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, new_position):
        positions = ('Pitcher', 'Catcher', 'First Basemen', 'Second Basemen',
                     'Third Basemen', 'Shortstop', 'Left Fielder',
                     'Center Fielder', 'Right Fielder', 'Designated Hitter',
                     'Utility', 'Coach')
        if new_position not in positions:
            raise ValueError(f"{new_position} is not a valid baseball position"
                             )
        self.__position = new_position


if __name__ == "__main__":
    year = 1984
    tony = BaseballPlayer("Tony Perez", "Pitcher")
    print(f"On the year {year} {tony.name} was a {tony.position}")
    year = 2019
    tony.position = 'Coach'
    print(f"On the year {year} {tony.name} was a {tony.position}")

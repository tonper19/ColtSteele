"""
oop_inheritance_super.py
use of OOP inherintance and super
"""


class Club:
    def __init__(self, name, address):
        self.name = name
        self.address = address

    def __repr__(self):
        return f"Club class with the following attributes: name={self.name}, address={self.address}"

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, new_name):
        if new_name == "":
            new_name = "Unknowm Club"
        self.__name = new_name

    @property
    def address(self):
        return self.__address

    @address.setter
    def address(self, new_address):
        if new_address == "":
            new_address = "Unknowm Address"
        self.__address = new_address


class Team(Club):
    def __init__(self, name, address, sport):
        super().__init__(name, address)
        self.sport = sport
        self.team_member_number = 0

    def __repr__(self):
        return f"Team class {self.sport} belongs to " + super().__repr__()

    @property
    def sport(self):
        return self.__sport

    @sport.setter
    def sport(self, new_sport):
        if new_sport == "":
            new_sport = "Unknowm Sport"
        self.__sport = new_sport

    @property
    def team_member_number(self):
        return self.__team_member_number

    @team_member_number.setter
    def team_member_number(self, team_member_number):
        self.__team_member_number = team_member_number


if __name__ == "__main__":
    rsh = Team("Brussels Kangaroos", "Avenue Albert Dumont 40", "softball")
    print(rsh)
    rsh.team_member_number = 1
    rsh.team_member_number = 2
    print(rsh.team_member_number)

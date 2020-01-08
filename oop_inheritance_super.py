"""
oop_inheritance_super.py
use of OOP inherintance and super
"""


class Club:
    _club_members = 0  # class variable

    def __init__(self, name, address):
        self.name = name
        self.address = address

    def __repr__(self):
        return f"Club class with the following attributes: name={self.name}, address={self.address}"

    @classmethod
    def active_club_members(cls):
        return cls._club_members

    @classmethod
    def increase_club_members(cls):
        cls._club_members += 1

    @classmethod
    def decrease_club_members(cls):
        cls._club_members -= 1

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


class KangaroosTeam(Club):
    def __init__(self, sport):
        super().__init__("Brussels Kangaroos", "Avenue Albert Dumont 40")
        self.sport = sport
        self.__active_team_member_number = 0

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
    def active_team_member_number(self):
        return self.__active_team_member_number

    def increase_team_member(self):
        self.__active_team_member_number += 1
        Club.increase_club_members()


if __name__ == "__main__":
    rsh = KangaroosTeam("softball men")
    sd1 = KangaroosTeam("softball ladies")

    print(rsh)
    rsh.increase_team_member()
    print(f"Current {rsh.sport} team members: {rsh.active_team_member_number}")
    rsh.increase_team_member()
    print(f"Current {rsh.sport} team members: {rsh.active_team_member_number}")

    for i in range(1, 16):
        sd1.increase_team_member()

    print(f"Current {sd1.sport} team members: {sd1.active_team_member_number}")

    print(f"Current {sd1.name} club memebers: {Club.active_club_members()}")

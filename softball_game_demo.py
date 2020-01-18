"""
Python pickle and jsonpickle demo object serialization

Serialize an object, save it to a file and use it later on the state
that it was pickled.

AUTHOR
    Tony Perez

DATE
    17/01/2020

    # refactor1 to generate a two teams game and play inning by inning
    # refactor2 keep the score
    # refactor3 allow to make changes to the lineup with the bench
    # refactor4 allow mercy rule
    # refactor5 display the score once is available

    # TODO: ramdomly generate a rain delay game if it is before the
    # 5th inning, then save the game using pickling and then load it
    # back and continue

"""
import pickle
import jsonpickle
from csv import DictReader
from random import choice


class Player():
    """
    A class used to represent a baseball player

    Attributes
    ----------
    name : str
        name of the player
    position : str
        field position of the player
    plays : list 
        plays the player has made during a game

    Methods
    -------
    make_a_play(new_play)
        append a player's new play to a list

    get_plays()
        return a list of the players plays during a game
    """

    def __init__(self, name, position):
        """
        initialize the player's name, position and create an
        empty list of plays
        """
        self.name = name
        self.position = position
        self.plays = []

    def __repr__(self):
        return f"Player class: name={self.name}, position={self.position}"

    # getters and setters the Python way
    @property
    def name(self):
        """
        return the player's name @property
        """
        return self.__name

    @name.setter
    def name(self, new_name):
        """
        set the player's name property
        """
        if new_name == "":
            new_name = "Unknowm Player"
        self.__name = new_name

    @property
    def position(self):
        """
        return the player's fielding position abbreaviation @property
        """
        return self.__position

    @position.setter
    def position(self, new_position):
        """
        set the player's name property, if blank set to Utility player
        """
        if new_position == "":
            new_position = "Utility"
        self.__position = new_position

    def make_a_play(self, new_play):
        """
        create a new game play for the player
        """
        self.plays.append(new_play)

    def get_plays(self):
        """
        return the list of plays of the player in a game
        """
        return self.plays


class Team():
    """
    A class used to represent a baseball team

    Attributes
    ----------
    name : str
        name of the team
    players : list
        list of players in the lineup
    bench : list
        list of the players sitting on the bench
    at_bat : int
        current player at bat (1 - 9)
    inning : int
        current inning
    outs : int
        current number of outs
    safe : tuple
        abbreviations that represent a non-out play
    out : tuple
        abbreviations that represent an out play
    plays : tuple
        all possible plays

    Methods
    -------
    lineup(Player)
        create a new lineup position for player, if the
        lineup is completed with 9 players, add the player
        to the bench
    game()
        generate a 9 inning game
    scoring_sheet()
        display the generated game scoring sheets

    """
    safe = ("H", "2H", "3H", "HR", "BB", "HBP")
    out = ("K", "1-3", "2-3", "U3", "4-3",
           "5-3", "6-3", "IF", "F7", "F8", "F9"
           )

    def __init__(self, name):
        self.name = name
        self.players = []
        self.bench = []
        self.at_bat = 1
        self.inning = 1
        self.outs = 0
        self.plays = self.safe + self.out

    def __repr__(self):
        return f"Team class: name={self.name}"

    # getters and setters the Python way
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, new_name):
        if new_name == "":
            new_name = "Unknowm Club"
        self.__name = new_name

    def lineup(self, new_player):
        if isinstance(new_player, Player):
            if len(self.players) < 9:
                self.players.append(new_player)
            else:
                self.bench.append(new_player)

    def game(self):
        # refactor1 to generate a two teams game and play inning by inning
        # refactor2 keep the score
        # refactor3 allow to make changes to the lineup with the bench
        # refactor4 allow mercy rule
        if len(self.players) == 9:
            while self.inning < 10:
                if self.at_bat > 9:
                    self.at_bat = 1
                play = choice(self.plays)
                idx = self.at_bat - 1
                self.players[idx].make_a_play(play)
                if play in self.out:
                    self.outs += 1
                    if self.outs == 3:
                        self.outs = 0
                        self.inning += 1
                self.at_bat += 1

    def scoring_sheet(self):
        # refactor1 display the score once is available
        idx = 0
        while idx < len(self.players):
            print(f"{idx + 1}. {self.players[idx].name}")
            player_plays = self.players[idx].get_plays()
            for play in player_plays:
                print(f" {play}", end="")
            print("")
            idx += 1

    # TODO: ramdomly generate a rain delay game if it is before the
    # 5th inning, then save the game using pickling and then load it
    # back and continue


def main():
    brussels_kangaroos = Team("Brussels Kangaroos Men Softball")

    # get the players and buid a lineup and bench
    with open("players.csv") as file:
        csv_reader = DictReader(file)
        for row in csv_reader:
            player = Player(row["name"], row["position"])
            brussels_kangaroos.lineup(player)

    brussels_kangaroos.game()
    brussels_kangaroos.scoring_sheet()


if __name__ == "__main__":
    main()

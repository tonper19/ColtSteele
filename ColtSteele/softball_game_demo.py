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
from csv import DictReader
from random import choice
# import pickle
# import jsonpickle


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
    hit : tuple
        abbreviations that represent a non-out play
    out : tuple
        abbreviations that represent an out play
    plays : tuple
        all possible plays
    score : list
        score for each inning

    Methods
    -------
    name(self)
        return name of the Team
    lineup(self, new_player)
        create a new lineup position for player, if the
        lineup is completed with 9 players, add the player
        to the bench
    game(self)
        generate a 9 inning game
    scoring_sheet(self)
        display the generated game scoring sheets

    """
    hit = {"H": 1, "2H": 2, "3H": 3, "HR": 4}
    safe = {"BB": 1, "IBB": 1, "HBP": 1}
    out = ("KS", "Kl", "1-3", "2-3", "U3", "4-3",
           "5-3", "6-3", "F1", "F2", "F3", "F4",
           "F5", "F6", "F7", "F8", "F9", "FO"
           )

    def __init__(self, name):
        self.name = name
        self.players = []
        self.bench = []
        self.at_bat = 1
        self.inning = 1
        self.outs = 0
        self.plays = list(self.hit.keys()) + \
            list(self.safe.keys()) + \
            list(self.out)
        self.score = []
        self.bases = []

    def __repr__(self):
        return f"Team class: name={self.name}"

    # getters and setters the Python way
    @property
    def name(self):
        """
        Getter of name
        """
        return self.__name

    @name.setter
    def name(self, new_name):
        if new_name == "":
            new_name = "Unknowm Club"
        self.__name = new_name

    def lineup(self, new_player):
        """
        Add a new player to the lineup. If the lineup is
        filled with the 9 batters, add the player to the
        bench
        """
        if isinstance(new_player, Player):
            if len(self.players) < 9:
                self.players.append(new_player)
            else:
                self.bench.append(new_player)

    def game(self):
        """
        generate a team's half game
        to be refactored to have two teams cometing with each other
        """
        # refactor: keep the score

        # refactor1 to generate a two teams game and play inning by inning
        # refactor3 allow to make changes to the lineup with the bench
        # refactor4 allow mercy rule

        def clear_score():
            self.score = [0] * 10  # index 0 is left untouched

        def empty_bases():
            # players on base 0: HP, 1: 1B, 2: 2B, 3: 3B
            # if bases length > 4, players have been pushed by a play
            self.bases = empty_base * 4

        def play_bases(player):
            self.bases[0] = player  # player is at bat on home plate
            play = choice(self.plays)  # and makes a random play
            player.make_a_play(play)  # persist the play within the player

            if play in self.out:
                self.outs += 1
                if self.outs == 3:
                    self.outs = 0
                    self.inning += 1
                    empty_bases()
            else:
                # get how many the player advances by concatenating
                # the hits and safe plays and getting the value
                how_many_bases = {**self.hit, **self.safe}[play]
                self.bases = (empty_base * how_many_bases) + [player] + \
                    self.bases[1:]
                bases_pushed = self.bases[4:]  # any length > 4 is a play push
                # sum of pushed bases with players on them
                runs_scored = sum([1 for player in bases_pushed
                                   if isinstance(player, Player)])
                self.score[self.inning] += runs_scored
                self.bases = self.bases[:4]

        # the game starts here!
        empty_base = [None]
        clear_score()
        empty_bases()

        if len(self.players) == 9:  # enough players?
            while self.inning < 10:  # games are 9 inning max
                if self.at_bat > 9:  # rotate the lineup
                    self.at_bat = 1

                idx = self.at_bat - 1
                play_bases(self.players[idx])

                self.at_bat += 1

    def scoring_sheet(self):
        """
        Return the score of the Team in the game
        """
        return self.score

    def box_score(self):
        """
        game's box score for one of the teams
        """
        print(f"{self.name}")
        print("\nBox Score")
        print("---------")

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
    """
    generate a baseball game
    """
    brussels_kangaroos = Team("Brussels Kangaroos")
    # ----------------------
    # to refactor all these:
    # ----------------------

    # get the players and build a lineup and bench
    with open("players.csv") as file:
        csv_reader = DictReader(file)
        for player_row in csv_reader:
            player = Player(player_row["name"], player_row["position"])
            brussels_kangaroos.lineup(player)

    brussels_kangaroos.game()
    bru_score = brussels_kangaroos.scoring_sheet()

    scoring_display = " " * 8
    for inning in range(1, len(bru_score)):
        scoring_display += "  |  " + str(inning)
        if inning == 9:
            scoring_display += "  |  \n"
    scoring_display += "-" * 72
    scoring_display += "\n"
    scoring_display += brussels_kangaroos.name[:8]
    idx = 0
    while idx < len(bru_score):
        if idx > 0:
            scoring_display += "  |  " + str(bru_score[idx])
            if idx == 9:
                scoring_display += f"  |  {sum(bru_score)}\n"
        idx += 1

    #
    hoboken_pioneers = Team("Hoboken Pioneers")

    # get the players and build a lineup and bench
    with open("players_hoboken.csv") as file:
        csv_reader = DictReader(file)
        for player_row in csv_reader:
            player = Player(player_row["name"], player_row["position"])
            hoboken_pioneers.lineup(player)

    hoboken_pioneers.game()
    hob_score = hoboken_pioneers.scoring_sheet()

    scoring_display += "-" * 72
    scoring_display += "\n"
    idx = 0
    scoring_display += hoboken_pioneers.name[:8]
    while idx < len(hob_score):
        if idx > 0:
            scoring_display += "  |  " + str(hob_score[idx])
            if idx == 9:
                scoring_display += f"  |  {sum(hob_score)}\n"
        idx += 1
    print(scoring_display)
    brussels_kangaroos.box_score()
    hoboken_pioneers.box_score()

if __name__ == "__main__":
    main()

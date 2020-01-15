"""
File I/O comma separated values reader in Python.

AUTHOR
    Colt Steele
    and some chipotage and testing by Tony Perez
"""
from csv import reader
from csv import writer
from csv import DictReader


def csv_read_line_by_line():
    with open("players.csv") as f:
        csv_reader = reader(f)
        next(csv_reader)  # ignore headers
        for player in csv_reader:
            print(f"{player[0]} plays {player[1]} and bats {player[2]}")


def csv_all_at_once():
    with open("players.csv") as f:
        csv_reader = reader(f)
        print(csv_reader)  # this is an iterator, can be converted to a list
        data = list(csv_reader)
        print(data)


def csv_read_dict_line_by_line():
    with open("players.csv") as f:
        csv_reader = DictReader(f)
        for row in csv_reader:
            # each row is an OrderedDict
            print(row)


def new_file_in_uppercase():
    with open("players.csv") as f:
        csv_reader = reader(f)
        with open("players_uppercase.csv", "w") as fu:
            csv_writer = writer(fu)
            for player in csv_reader:
                csv_writer.writerow([string.upper() for string in player])


if __name__ == "__main__":
    csv_read_line_by_line()
    csv_all_at_once()
    csv_read_dict_line_by_line()
    new_file_in_uppercase()

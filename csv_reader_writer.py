"""
File I/O comma separated values reading and writing in Python.
using a csv file with the names of some of the 
2019 Belgium Champions Brussels Kangaroos Men Softball Reserve Team 

AUTHOR
    Colt Steele
    and some chipotage and testing by Tony Perez
"""
from csv import reader
from csv import writer
from csv import DictReader


def csv_read_line_by_line():
    """
    read a csv file with players, ignore the header and display
    the player name, its position and his/her batting average in
    separate lines
    """
    with open("players.csv") as f:
        csv_reader = reader(f)
        next(csv_reader)  # ignore headers
        for player in csv_reader:
            print(f"{player[0]} plays {player[1]} and bats {player[2]}")


def csv_all_at_once():
    """
    demo on reading a csv file, displaying the iterator and then
    converting into a list and displaying it
    """
    with open("players.csv") as f:
        csv_reader = reader(f)
        print(csv_reader)  # this is an iterator, can be converted to a list
        data = list(csv_reader)
        print(data)


def csv_read_dict_line_by_line():
    """
    demo on reading a csv file as an OrderedDict iterator
    the header become the dictionay key.
    Display each row, as a OrderedDict
    """
    with open("players.csv") as f:
        csv_reader = DictReader(f)
        for row in csv_reader:
            # each row is an OrderedDict
            print(row)


def csv_read_dict_line_by_line_with_key():
    """
    another example on how to read a csv file into an OrderedDict
    this time reading each row and displaying some of its values using
    the key as an index
    """
    with open("players.csv") as f:
        csv_reader = DictReader(f)
        for row in csv_reader:
            # each row is an OrderedDict
            print(f"{row['name']} is {row['age']} year old")


def new_file_in_uppercase():
    """
    read a csv file and create a new file (write) with all its
    alphabetic characters in uppercase
    by embedding the write inside of the read we maintain the
    read iterator open thus can be iterated in a loop
    """
    with open("players.csv") as f:
        csv_reader = reader(f)
        with open("players_uppercase.csv", "w") as fu:
            csv_writer = writer(fu)
            for player in csv_reader:
                csv_writer.writerow([string.upper() for string in player])
    print("*** New file: players_uppercase.csv")


if __name__ == "__main__":
    csv_read_line_by_line()
    csv_all_at_once()
    csv_read_dict_line_by_line()
    csv_read_dict_line_by_line_with_key()
    new_file_in_uppercase()

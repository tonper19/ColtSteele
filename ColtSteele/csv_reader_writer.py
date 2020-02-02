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
from csv import DictWriter
from decorator_enforce_argument_type import enforce


def csv_read_line_by_line():
    """
    Read a csv file with players, ignore the header and display
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
    Demo on reading a csv file, displaying the iterator and then
    converting into a list and displaying it
    """
    with open("players.csv") as f:
        csv_reader = reader(f)
        print(csv_reader)  # this is an iterator, can be converted to a list
        data = list(csv_reader)
        print(data)


def csv_read_dict_line_by_line():
    """
    Demo on reading a csv file as an OrderedDict iterator
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
    Another example on how to read a csv file into an OrderedDict
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
    Read a csv file and create a new file (write) with all its
    alphabetic characters in uppercase.
    By nesting  the write inside of the read we maintain the
    read iterator open thus can be iterated in a loop
    """
    with open("players.csv") as f:
        csv_reader = reader(f)
        with open("players_uppercase.csv", "w") as fu:
            csv_writer = writer(fu)
            for player in csv_reader:
                csv_writer.writerow([string.upper() for string in player])
    print("*** New file: players_uppercase.csv")


@enforce(int)
def years_to_days(age):
    """
    Function converting the age in years to days
    it's 'decorated' by a 'decorator' residing in
    decorator_enforce_argument_type.py (imported)
    The decorator will try convert the age argument 
    to an integer datatype, if it is not, and execute
    this function.
    """
    return age * 365


def players_age_in_days():
    """
    This function will read the players.csv file
    and convert the players age in years to days.
    Use of DictWriter instead of writer.
    Instead of nesting the read of the file and the
    write of the new file, as in the function
    decorator_enforce_argument_type, the players file
    is open, read and the iterator is stored in a 
    list. Since the next 'with open' statement is not
    nested, the players.csv file gets closed and the
    iterator csv_reader is no longer available. 
    The list has data and can be iterated to create
    the new file.
    """
    with open("players.csv") as original_file:
        csv_reader = DictReader(original_file)
        players = list(csv_reader)  # csv_reader no longer has data after this

    # using DictWriter!
    with open("players_age_in_days.csv", "w") as new_file:
        headers = ("name", "position", "batting average", "age in days")
        csv_writer = DictWriter(new_file, fieldnames=headers)
        csv_writer.writeheader()
        # using the list instead of csv_reader
        for player in players:
            # print(player)
            csv_writer.writerow({
                "name": player["name"],
                "position": player["position"],
                "batting average": player["batting average"],
                # the header name must be the same as in new file headers
                "age in days": years_to_days(player["age"])  # decorated funct.
            })
    print("*** New file: players_age_in_days.csv")


if __name__ == "__main__":
    csv_read_line_by_line()
    csv_all_at_once()
    csv_read_dict_line_by_line()
    csv_read_dict_line_by_line_with_key()
    new_file_in_uppercase()
    players_age_in_days()

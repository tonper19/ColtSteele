"""
Python date and time examples 2

Time calculation across timezones. Based on the course 
Working with dates and times in Python
by Georgy Pashkov

AUTHOR
    Georgy Pashkov
    modifications by Tony Perez

DATE
    25/01/2020

"""
import csv
import textwrap
from datetime import datetime, timedelta

class Airport:
    """
    Airport as represented in airport.csv
    """
    prop_names = ("id", "name", "city", "country", "iata", "icao", "lat"
                  , "long", "alt", "utc_offset", "dst_rule", "tz", "type"
                  , "source")
    
    def __init__(self, csv_entry):
        assert len(csv_entry) == len(Airport.prop_names)
        self.__dict__.update(dict(zip(Airport.prop_names, csv_entry)))

    def __str__(self):
        return f"{iata} ({name})"

def load_airports(csv_file):
    """
    Load airport into a dictionary where keys are IATA codes
    """
    airports = {}
    with open(csv_file, newline="") as data_file:
        for entry in csv.reader(data_file):
            a = Airport(csv_entry=entry)
            airports[a.iata] = a
    return airports

def main():
    """
    main function execution
    """


if __name__ == "__main__":
    main()

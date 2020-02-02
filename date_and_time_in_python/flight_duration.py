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
import pytz
from tzlocal import get_localzone

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
        return "{0.iata} ({0.name})".format(self)

def load_airports(csv_file):
    """
    Load airport into a dictionary where keys are IATA codes
    """
    airports = {}
    with open(csv_file, newline="") as data_file:
        for entry in csv.reader(data_file):
            this_airport = Airport(csv_entry=entry)
            airports[this_airport.iata] = this_airport
    return airports

class Flight:
    """
    Flight class
    """
    def __init__(self, flight_id, origin, destination, departure, arrival):
        self.id = flight_id
        self.origin = origin
        self.destination = destination
        self.departure = self.localize_flight_datetime(departure, origin.tz)
        self.arrival = self.localize_flight_datetime(arrival, destination.tz)

    @staticmethod
    def localize_flight_datetime(date_time, tz_name):
        """
        Set a datetime with the timezone
        Always test for invalid and ambigous time
        """
        time_zone = pytz.timezone(tz_name)
        try:
            return time_zone.localize(date_time, is_dst=None)
        except pytz.exceptions.AmbiguousTimeError:
            print("Error")
            return time_zone.localize(date_time, is_dst=True)
        except pytz.exceptions.InvalidTimeError:
            print("*** The time is invalid")
            return time_zone.localize(datetime(1970, 1, 1, 0, 0, 0), is_dst=None)

    @property
    def duration(self):
        """
        Return the duration of a flight
        """
        return self.arrival - self.departure

    @property
    def check_in(self):
        """
        Returns the time to checkin
        departure.tzinfo.normalize used to correct the timezone offset
        in case of DST change and the substraction (-3 hours) falls
        in the previous DST time
        Whenever adding or substracting an offset from a timestamp,
        we should always call normalize on the result
        """
        return self.departure.tzinfo.normalize(self.departure
                                               - timedelta(hours=3))

    def time_to_departure(self):
        """
        Returns the time to departure
        """
        return self.departure - get_localzone().localize(datetime.now())

    def __str__(self):
        return textwrap.dedent\
            ("""\
            Flight {0.id}:
                from        : {0.origin} {0.departure.tzinfo}
                to          : {0.destination}  {0.arrival.tzinfo}
                departure   : {0.departure}
                arrival     : {0.arrival}
                duration    : {0.duration}

                time to departure  : {ttd}
                check-in           : {0.check_in}
            """.format(self, ttd=self.time_to_departure())
            )

def main():
    """
    main function execution
    """
    airports = load_airports("airport.csv")
    # for a in airports:
    #     print(airports[a])

    flights = [
        Flight(flight_id="DL583"
               , origin=airports["DTW"]
               , destination=airports["PVG"]
               , departure=datetime(2020, 1, 25, 15, 51, 0)
               , arrival=datetime(2020, 1, 26, 18, 37, 0)
              )
        , Flight(flight_id="NH112"
                 , origin=airports["HND"]
                 , destination=airports["ORD"]
                 , departure=datetime(2020, 1, 26, 10, 47, 0)
                 , arrival=datetime(2020, 1, 26, 6, 50, 0)
                )
        # next two flights depart when the DST change occurs
        # the first one before, the second after
        , Flight(flight_id="DL81"
                 , origin=airports["BRU"]
                 , destination=airports["ATL"]
                 , departure=datetime(2020, 3, 29, 1, 10, 0)
                 , arrival=datetime(2020, 3, 29, 7, 50, 0)
                )
        # Invalid time. this flight departs on date time that does not exists
        # in Paris:
        # the DST changed from 02:00 to 03:00 from CET to CEST (Summer Time)
        , Flight(flight_id="AF22"
                 , origin=airports["CDG"]
                 , destination=airports["JFK"]
                 , departure=datetime(2020, 3, 29, 2, 10, 0)
                 , arrival=datetime(2020, 3, 29, 6, 50, 0)
                )
        # Ambigous departure time: change from Summer to Winter, 2:00 is
        # repeated twice
        , Flight(flight_id="DL82"
                 , origin=airports["BRU"]
                 , destination=airports["ATL"]
                 , departure=datetime(2018, 10, 28, 2, 10, 0)
                 , arrival=datetime(2018, 10, 28, 6, 50, 0)
                )
    ]

    for flight in flights:
        print(flight)

if __name__ == "__main__":
    main()

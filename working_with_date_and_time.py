"""
Python date and time examples

examples using the course Working with dates and times in Python
by Georgy Pashkov

AUTHOR
    Tony Perez

DATE
    25/01/2020

"""

import time
import datetime
import pytz

def get_current_time():
    """
    example on using time
    """
    print("get_current_time")
    current_time = time.time()
    print(f"Current time (raw): {current_time}")
    print(f"Current time (formatted): {time.ctime(current_time)}")

def work_with_datetime():
    """
    examples on using datetime
    """
    print("work_with_datetime")
    print(f"datetime.date.today(): {datetime.date.today()}")
    print(f"datetime.datetime.now(): {datetime.datetime.now()}")
    print(f"datetime.datetime.now().date(): {datetime.datetime.now().date()}")
    print(f"datetime.datetime.now().time(): {datetime.datetime.now().time()}")

def work_with_timezones():
    """
    example on using datetimes with timezones
    """
    brussels = pytz.timezone("Europe/Brussels")
    athens = pytz.timezone("Europe/Athens")

    print("*** NEVER pass tzinfo to datetime contructor")
    print("*** USE timezone.localize instead")

    naive = datetime.datetime(2019, 7, 27, 13, 45, 0)
    print(f"naive or date unaware of timezone: {naive}")
    aware_bru = brussels.localize(naive)
    print(f"brussels timezone: {aware_bru}")
    aware_ath = aware_bru.astimezone(athens)
    print(f"athens timezone: {aware_ath}")
    print(f"Are the two timezone aware dates equal => {aware_ath == aware_bru}")

if __name__ == "__main__":
    get_current_time()
    work_with_datetime()
    work_with_timezones()

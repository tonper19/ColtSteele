"""how to transpose a table in Python,
called pivoting a table in Excel."""
from pprint import pprint as pp

print("*** Almiryda hourly temperatures from 28/07/2019 to 31/07/2019")
sun = [20, 20, 19, 19, 19, 20, 20, 22, 23, 24, 27, 30, 33, 35, 38, 41, 40, 38, 35, 30, 28, 25, 23, 22]
mon = [21, 19, 18, 18, 19, 20, 21, 22, 24, 25, 26, 28, 30, 31, 35, 36, 35, 33, 31, 29, 27, 23, 24, 23]
tue = [22, 21, 19, 18, 18, 21, 22, 23, 25, 27, 28, 30, 31, 33, 34, 35, 33, 32, 29, 27, 25, 24, 23, 21]
wed = [20, 19, 18, 17, 17, 17, 18, 22, 24, 25, 27, 29, 32, 34, 35, 37, 37, 35, 33, 30, 29, 28, 26, 24]

# four different list zipped: each
print("*** Zipping four different lists:")
for hour in zip(sun, mon, tue, wed):
    print(hour)

print("*** Single data structure in the form of list of lists")
daily = [sun, mon, tue, wed]
pp(daily, width=120)

print("*** Zipping a single data structure in the form of list of lists\n"
      "using extended call syntax, apply any iterable series to function\n"
      "call arguments using the asterik prefix (*args)")
for hour in zip(*daily):
    print(hour)

print("*** Produce a single data structure passing the result of zip\n"
      "to the list constructor. We have transformed a structure containing\n"
      "lists of daily temperatures\n"
      "into a structure containing series of hourly temperatures.\n"
      "Effectively converting columns into rows and rows into columns.")
transposed = list(zip(*daily))
pp(transposed)
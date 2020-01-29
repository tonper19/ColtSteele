"""Python working with iterables

From the course: Python Fundamentals. Chapter: Iterables
 
"""
from math import factorial, sqrt
from pprint import pprint as pp
import os
import glob

def is_prime(x):
    """Returns true if the argument is a prime number
    """
    if x < 2:
        return False
    for i in range(2, int(sqrt(x)) + 1):
        if x % i == 0:
            return False
    return True


def comprehension():
    """Working with comprehension examples
    """
    words = ("Why sometimes I have believed as many as six impossible things "
             "before breakfast").split()
    print("*** List comprehension: ")
    print(f"List: {words}")
    print(f"Length of each word in the list: {[len(word) for word in words]}")
    print("=" * 132)
    print("*** Set comprehension: ")
    f = {len(str(factorial(x))) for x in range(20)}
    print(f"Unique lengths of the first 20 factorials: {f}")
    print("=" * 132)
    print("*** Dictionary comprehension: ")
    country_to_capital = {"Greece": "Athens",
                          "Spain": "Madrid",
                          "Cuba": "La Habana",
                          "United States of America": "Washington"
                         }
    capital_to_country = {capital: country 
                          for country, capital in
                          country_to_capital.items()
                         }
    pp(capital_to_country)
    python_modules_sizes = {os.path.realpath(p): os.stat(p).st_size
                            for p in glob.glob("*.py")
                           }
    pp(python_modules_sizes)
    print("=" * 132)
    print("*** List comprehension with filtering clause: ")
    prime_numbers = [x for x in range(101) if is_prime(x)]
    print(f"The first prime numbers smaller than 100 are {prime_numbers}")


def main():
    comprehension()

if __name__ == "__main__":
    main()
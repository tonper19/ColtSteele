"""
decorator example to use as function speed test
Because @wraps is used, the metadata is preserved.

AUTHOR
    Colt Steele
    and some chipotage and testing by Tony Perez
"""
from functools import wraps
from time import time


def speed_test(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        start_time = time()
        result = fn(*args, **kwargs)
        end_time = time()
        print(f"Executing {fn.__name__}")
        print(f"Elapsed time: {end_time - start_time}")
        return result
    return wrapper


@speed_test
def sum_nums_gen():
    return sum(x for x in range(90000000))


@speed_test
def sum_nums_list():
    return sum([x for x in range(90000000)])


if __name__ == "__main__":
    sum_nums_gen()
    sum_nums_list()


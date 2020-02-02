"""
decorator example to ensure that the first argument
has certain value.
Because @wraps is used, the metadata is preserved.

AUTHOR
    Colt Steele
    and some chipotage and testing by Tony Perez
"""
from functools import wraps


def ensure_first_arg_is(value):
    def inner(fn):
        @wraps(fn)
        def wrapper(*args, **kwargs):
            if args and args[0] != value:
                print(f"First arg must be {value}")
                raise ValueError
            return fn(*args, **kwargs)
        return wrapper
    return inner


@ensure_first_arg_is("Taco Bell")
def fast_food(*restaurants):
    print(f"There are {len(restaurants)} restaurants, they are:")
    for restaurant in restaurants:
        print(restaurant)


@ensure_first_arg_is(42)
def the_answer(answer):
    print(f"The answer to life, the universe and everything is {answer}")


if __name__ == "__main__":
    try:
        fast_food("Burger King", "Taco Bell", "Pizza Hut")
    except ValueError as err:
        print("That's not my favorite fast food joint")
    print("-" * 50)
    fast_food("Taco Bell", "Pizza Hut", "Los 100 Montaditos")
    print("-" * 50)
    try:
        the_answer(19)
    except ValueError as err:
        print("That's not the answer")
    print("-" * 50)
    the_answer(42)

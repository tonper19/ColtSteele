"""
decorator example to ensure than certain argument types are
not used.
Because @wraps is used, the metadata is preserved.

AUTHOR
    Colt Steele
    and some chipotage and testing by Tony Perez
"""

from functools import wraps


def ensure_no_kwargs(fn):
    """
    decorator function
    execute the decorated function greet in the wrapper
    function but raise a ValueError if kwargs are provided.
    """
    @wraps(fn)  # preserve the metadata
    def wrapper(*args, **kwargs):
        if kwargs:
            raise ValueError
        return fn(*args, **kwargs)
    return wrapper


@ensure_no_kwargs
def greet(name):
    """
    decorated function
    when executed, it will call its decorator: @ensure_no_kwargs
    """
    print(f"hi there {name}")


if __name__ == "__main__":
    # no kwargs here
    greet("Tony")

    try:
        # kwarg here, it will produce an error
        greet(name="Tony")
    except ValueError as ve:
        print("There was a ValueError calling greet")

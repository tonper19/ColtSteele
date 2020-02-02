"""
decorator example and usage of wraps to preserve the wrapped function
metadata.
Because @wraps is used, the metadata is preserved.

AUTHOR
    Colt Steele
    and some chipotage and testing by Tony Perez
"""

from functools import wraps


def log_function_data(function):
    """
    returns the wrapped function
    """
    @wraps(function)
    def wrapper(*args, **kwargs):
        """
        wrapper function documentation
        """
        print(f"you are about to call {function.__name__}")
        print(f"Its documentation is {function.__doc__}")
        return function(*args, **kwargs)
    return wrapper


@log_function_data
def add(x, y):
    """
    returns the sum of two numbers
    """
    return x + y


if __name__ == "__main__":
    print(add(18, 1))
    print("Because @wraps is used, the metadata is preserved:")
    print(f"Calling the documentation of add outside of the decorated function: {add.__doc__}")
    print("Otherwise the log_function_data documentation displays")

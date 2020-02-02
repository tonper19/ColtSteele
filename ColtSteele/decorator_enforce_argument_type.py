"""
decorator example to enforce argument types to
a decorated function.
Because @wraps is used, the metadata is preserved.

AUTHOR
    Colt Steele
    and some chipotage and testing by Tony Perez
"""
from functools import wraps


def enforce(*types):
    """
    decorator function enforcing, and converting, argument data types
    """
    def decorator(fn):
        def new_function(*args, **kwargs):
            # convert args into something mutable, list in this case
            newargs = []
            for original_argument, type_to_convert in zip(args, types):
                newargs.append(type_to_convert(original_argument))
            return fn(*newargs, **kwargs)
        return new_function
    return decorator


@enforce(str, int)
def repeat_msg(msg, times):
    """
    function expecting a string and then an integer as their
    parameters, the decorator will try to enforce, and if they
    are not, the decorator will try to convert them
    If successful, print the string (msg) n times (integer)
    """
    for i in range(times):
        print(msg)


if __name__ == "__main__":
    repeat_msg(42, "4")  # expect str and an int, the decorator will cast them

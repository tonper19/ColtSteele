"""Escape unicode characters through a decorator."""
import functools  # preserve decorated functions metadata

def escape_unicode(f):
    @functools.wraps(f)
    def wrap(*args, **kwargs):
        x = f(*args, **kwargs)
        return ascii(x)
    return wrap

@escape_unicode
def northern_city():
    """A city in northern Norway."""
    return "Tromsø"

if __name__ == "__main__":
    city = northern_city()
    print(city)

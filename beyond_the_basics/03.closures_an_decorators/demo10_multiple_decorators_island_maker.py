"""Multiple decorators usage demo."""
import functools  # preserve decorated functions metadata

def make_look_like_norwegian(f):
    @functools.wraps(f)
    def wrap(*args, **kwargs):
        x = f(*args, **kwargs)
        return x.replace("a", "å").replace("o", "ø").replace("e", "æ")
    return wrap

class Trace:
    def __init__(self):
        self.enabled = True

    def __call__(self, function):
        def wrap(*args, **kwargs):
            if self.enabled:
                print(f"** Tracer information - calling {function}")
            return function(*args, **kwargs)
        return wrap

    @property
    def enabled(self):
        return self._enabled
    
    @enabled.setter
    def enabled(self, is_enabled):
        self._enabled = is_enabled

if __name__ == "__main__":
    tracer = Trace()

    @tracer
    @make_look_like_norwegian
    def norwegian_island_maker(name):
        return name + "oy"
    
    island = norwegian_island_maker("Isla de Tenerife")
    print(f"The new Norwegian island is: {island}")

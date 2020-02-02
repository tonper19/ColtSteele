"""Using a class as a decorator demo.
Count the number of times a function is called.
"""

class CallCount:
    def __init__(self, function):
        self.f = function
        self.count = 0
    
    def __call__(self, *args, **kwargs):
        self.count = 1
        return self.f(*args, **kwargs)

    @property
    def count(self):
        return self._count

    @count.setter
    def count(self, value):
        try:
            self._count += value
        except AttributeError:
            self._count = 0

@CallCount
def hello(name):
    print(f"Hello {name}")


if __name__ == "__main__":
    hello("Ana")
    hello("Annabelle")
    hello("Miguel")
    hello("Tony")
    print(f"The function hello has been called {hello.count} times.")

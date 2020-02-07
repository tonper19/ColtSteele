class Point2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __str__(self):
        """Produces a readable, human-friendly representations of
        an object.
        If __str__ is not overriden, it uses the return from __repr__.
        Intended for clients.
        """
        return f"({self.x}, {self.y})"
    
    def __repr__(self):
        """Produces an unambiguous string representation of an object.
        The result of repr() should generally contain more information
        than the result of str().
        Intended for developers.
        As a rule, you should always write a repr() for your classes."""
        return f"Point2D(x={self.x}, y={self.y})"

    def __format__(self, f):
        return f"[Formatted point: {self.x}, {self.y}, {f}]"

def main():
    p = Point2D(19, 42)
    print(f"The str(p) returns {str(p)}")
    print(f"The repr(p) returns {repr(p)}")

    # repr() is used when showing elements of a collection
    lst = [Point2D(i, i * 2) for i in range(3)]
    print(f"The str of a list uses repr: {str(lst)}")
    print(f"The repr of a list: {repr(lst)}")
    dct = {i: Point2D(i, i * 2) for i in range(3)}
    print(f"The str of a dictionary uses repr: {str(dct)}")
    print(f"The repr of a dictionary: {repr(dct)}")

    # using format in print
    print(f"This is a point: {Point2D(19, 64)}")



if __name__ == "__main__":
    main()
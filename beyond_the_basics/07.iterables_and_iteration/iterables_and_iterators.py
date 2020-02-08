import itertools

class Trace:
    # Trace class taken from lesson 3
    def __init__(self):
        self.enabled = True

    def __call__(self, function):
        def wrap(*args, **kwargs):
            if self.enabled:
                print(f"** Tracer information - calling {function}")
            return function(*args, **kwargs)
        return wrap        

class ComprehensionDemo:
    """Comprehension demo class.

    Python comprehension:
        Short-hand syntax for creating collections and iterable objects.    
    """

    def multi_input_comprehension(self, r, f):
        """Multi input list comprehension demo.

        More than one for loop and if statement combination.
        Spread the comprehension across multiple lines to keep it
        readable.
        
        Arguments:
            r {int} -- range
            f {int} -- from
        
        Returns:
            list -- list comprehension
        """
        values = [x / (x - y)
                  for x in range(r)
                  if x > f
                  for y in range(r)
                  if x - y != 0]
        return values

    def nested_comprehension(self, r, mult):
        nested_list = [[y * mult for y in range(x)] for x in range(r)]
        return nested_list

class MapDemo:
    """Map demo class.

    Python map function: 
        Apply a function to every element in a sequence, producing
        a new sequence. 
        map() is lazy, it only produces values as
        they're needed. The map object returned by map() is itself
        an iterator object and only by iterating over can you start
        to produce output.
        map() can accept any number of input sequences. The number
        of input sequences must match the number of function arguments.
    """
    def map_demo(self, string):
        """Produce a new sequence using map.
        
        Arguments:
            string {str} -- string of characters
        
        Returns:
            map iterator -- sequence of ascii codes for each character
                in string.
        """
        result_iterator = map(Trace()(ord), string)
        return result_iterator
    
    def map_multiple_input_seq_demo(self):
        def combine(seq_order, size, color, thing):
            return f"{seq_order}. {size} {color} {thing}"
        print("*** Map multiple input sequence demo")
        sizes = ["litte", "medium", "big"]
        colors = ["red", "blue", "red"]
        things = ["corvette", "jeans", "machine"]

        combi = map(combine, itertools.count(start=1), sizes, colors, things)
        for i in combi:
            print(i)

def main():
    cdemo = ComprehensionDemo()
    v = cdemo.multi_input_comprehension(r=12, f=6)
    print(f"List: {v}")
    nested = cdemo.nested_comprehension(r=5, mult=5)
    print(f"Nested list: {nested}")

    mdemo = MapDemo()
    iterator = mdemo.map_demo("Tenerife, isla de la eterna primavera")
    print(f"Lazily producing values as needed: {next(iterator)}")
    print(f"Lazily producing values as needed: {next(iterator)}")
    print(f"Lazily producing values as needed: {next(iterator)}")

    mdemo.map_multiple_input_seq_demo()
    
if __name__ == "__main__":
    main()
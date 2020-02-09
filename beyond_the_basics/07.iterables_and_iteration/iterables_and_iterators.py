import itertools
from functools import reduce
import operator

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

    Python map() function: 
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

class FilterDemo:
    """Filter demo class

    Python filter() function:
        Apply a function to each element in a sequence, constructing a
        new sequence with elements for which the function returns True.
        Like map(), filter() produce its elements lazily. Unlike map(), 
        filter() only accepts a single input sequence and the function
        it takes only accepts a single argument.
    """
    def is_odd(self, value):
        return value % 2 != 0
    
    def filter_demo(self):
        print("*** Filter demo: get odd numbers only")
        iterator = filter(self.is_odd, [-3, -2, -1, 0, 1, 2, 3])
        return list(iterator)
    
class ReduceDemo:
    """Reduce demo class

    Python functools.reduce() function:
        Repeatedly apply a function to the elements of a sequence,
        reducing them to a single value.
    """
    def multiply_with_progress(self, x, y):
        print(f"multiply {x} {y}")
        return x * y

    def reduce_demo(self):
        print("*** Reduce demo: sum the year of birth of all of us")
        sum_of_years = reduce(operator.add, [1964, 1970, 2002, 2004])
        return sum_of_years

    def reduce_with_progress_demo(self):
        print("*** Reduce demo: multiple elements of sequence and show progress")
        m = reduce(self.multiply_with_progress, range(1, 10), 1)
        return m

class MapReduce:
    def count_words(self, doc):
        normalized_doc = ''.join(c.lower() if c.isalpha() else ' ' for c in doc)
        frequencies = {}
        for word in normalized_doc.split():
            frequencies[word] = frequencies.get(word, 0) + 1
        return frequencies
    
    def combine_counts(self, d1, d2):
        d = d1.copy()
        for word, count in d2.items():
            d[word] = d.get(word, 0) + count
        return d


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
    
    fdemo = FilterDemo()
    lst = fdemo.filter_demo()
    print(lst)

    rdemo = ReduceDemo()
    s = rdemo.reduce_demo()
    print(s)
    s = rdemo.reduce_with_progress_demo()
    print(s)

    mr = MapReduce()

    documents = [
        "It was the best of times, it was the worst of times, it was the"
        " age of wisdom, it was the age of foolishness, it was the epoch"
        " of belief, it was the epoch of incredulity, it was the season"
        " of Light, it was the season of Darkness, it was the spring of"
        " hope, it was the winter of despair, we had everything before us,"
        " we had nothing before us, we were all going direct to Heaven,"
        " we were all going direct the other way—in short, the period was"
        " so far like the present period, that some of its noisiest"
        " authorities insisted on its being received, for good or for evil,"
        " in the superlative degree of comparison only.",
        "I went to the woods because I wished to live deliberately, to"
        " front only the essential facts of life, and see if I could not"
        " learn what it had to teach, and not, when I came to die, discover"
        " that I had not lived.",
        "Friends, Romans, countrymen, lend me your ears. I come to bury "
        "Caesar, not to praise him. The evil that men do lives after them;"
        "The good is oft interrèd with their bones. So let it be with Caesar",
        "I do not like green eggs and ham. I do not like them, Sam-I-Am."
    ]

    counts = map(mr.count_words, documents)
    total_counts = reduce(mr.combine_counts, counts)
    print(total_counts)


if __name__ == "__main__":
    main()
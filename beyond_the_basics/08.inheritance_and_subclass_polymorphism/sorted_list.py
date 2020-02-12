class SimpleList:
    def __init__(self, items):
        self._items = list(items)

    def add(self, item):
        self._items.append(item)
    
    def __getitem__(self, index):
        return self._items[index]
    
    def sort(self):
        self._items.sort()
    
    def __len__(self):
        return len(self._items)
    
    def __repr__(self):
        return "SimpleList({!r})".format(self._items)

class SortedList(SimpleList):
    def __init__(self, items=()):
        print(f"{type(items)}")
        super().__init__(items)
        self.sort()
    
    def add(self, item):
        super().add(item)
        self.sort()
    
    def __repr__(self):
        return "SortedList({!r})".format(self._items)

class IntList(SimpleList):
    def __init__(self, items=()):
        for x in items:
            self._validate(x)
        super().__init__(items)

    @staticmethod
    def _validate(x):
        if not isinstance(x, int):
            raise TypeError("IntList only supports integer values.")
    
    def add(self, item):
        self._validate(item)
        super().add(item)

    def __repr__(self):
        return "IntList({!r})".format(list(self))

class SortedIntList(IntList, SortedList): 
    def __repr__(self):
        return "SortedIntList({!r})".format(list(self))


def main():
    sl = SimpleList([3, 1, 2])
    r = sl.__repr__()
    print(r)

    srt = SortedList([5, 1, 3])
    print(f"{srt.__repr__()}")

    il = IntList([3, 1, 2, 8])
    il.add(19)
    try:
        il.add("abc")
    except TypeError:
        print("There was a TypeError")

    # multiple inheritance
    sil = SortedIntList([23, 42, 19])
    print(f"{sil.__repr__()}")
    sil.add(-17)
    print(f"{sil.__repr__()}")


if __name__ == "__main__":
    main()
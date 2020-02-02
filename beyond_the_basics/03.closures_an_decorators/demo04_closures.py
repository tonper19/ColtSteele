"""Closure example"""
def enclosing():
    x = "this variable is enclosed"
    y = "and so is this"
    z = "but this one is not"
    def local_function():
        print(x, y)  # because the first two vars are used here
    return local_function

if __name__ == "__main__":
    lf = enclosing()
    print(lf.__closure__)
    lf()

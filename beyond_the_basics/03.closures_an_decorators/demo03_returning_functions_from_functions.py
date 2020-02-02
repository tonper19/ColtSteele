"""Returning a function from a function."""
def enclosing():
    def local_function():
        print("I am a local function")
    return local_function

if __name__ == "__main__":
    lf = enclosing()
    lf()
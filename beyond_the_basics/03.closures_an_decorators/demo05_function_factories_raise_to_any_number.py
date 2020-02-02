""" """
def raise_to(exponent):
    def raise_to_exponent(x):
        return pow(x, exponent)
    return raise_to_exponent

if __name__ == "__main__":
    # the parameter exponent will be a closure with the value of 2
    square = raise_to(2)
    # and here is the proof:
    print(square.__closure__)
    # and now, when square is invoked, it will raise a number to the power of 2
    print(f"The square of 5 is: {square(5)}")
    print(f"The square of 19 is: {square(19)}")

    # and we can create functions the same way:
    cube = raise_to(3)
    print(f"The cube of 5 is: {cube(5)}")
    print(f"The cube of 19 is: {cube(19)}")

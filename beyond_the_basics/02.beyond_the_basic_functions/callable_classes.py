def sequence_class(immutable):
    """returns a callable class with a conditional expression."""
    return tuple if immutable else list
    # the conditional expression is the same as below:
    # if immutable:
    #     cls = tuple
    # else:
    #     cls = list
    # return cls

if __name__ == "__main__":
    seq = sequence_class(immutable=True)
    this_is_a_tuple = seq("Almiryda")
    print(this_is_a_tuple)
    
    seq = sequence_class(immutable=False)
    this_is_a_list = seq("Kalyves")
    print(this_is_a_list)

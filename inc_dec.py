'''
inc_dec.py
used for unit test purposes
'''


def increment(x):
    return x + 1


def decrement(x):
    return x - 1


def main():
    variable = increment(1000)
    variable = decrement(variable)
    print(f'variable = {variable}')


if __name__ == '__main__':
    main()

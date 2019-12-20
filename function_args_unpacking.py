
''' function_args_unpacking.py
the function expects *args (a tuple), instead of sending several arguments
we can send a collection (list, tuple, set) instead, when calling the function add an *
to the list/tuple/set name, this will do an unpacking of all the elements and
treat each item as a single argument
'''

def players(*args):
    for player in args:
        print(player)

# using a list
softball_team = ['Raul', 'Christophe', 'Diego', 'Bill']
print('-----------------')
print('Softball Men:')
print('-----------------')
players(*softball_team)

# using a set
print('-----------------')
print('Baseball:')
print('-----------------')
baseball_team = {'Miguel', 'Carlos', 'Peter', 'Elio'}
players(*baseball_team)

# using a tuple
print('-----------------')
print('Softball Women:')
print('-----------------')
softballw_team = ('Lara', 'Idjy', 'Sybill', 'Sofie')
players(*softballw_team)

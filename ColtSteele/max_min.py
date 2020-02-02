'''
max and min iterable functions
return the maximum or minimum item of an iterable
'''

numbers = [7, 1, 3, 99, 5, 8, 6, 2]
max_number = max(numbers)
# return the biggest number on a list
print(f'The biggest number is {max_number} in the list {numbers}')

# min, strings and tuples
family = ('Miguel', 'Tony', 'Ana', 'Annabelle')
first_name = min(family)
print(f'The first name is {first_name} on the tuple: {family}')

# use max to get the name with most letters
# 1: family           - pass an iterable to the max function (tuple in this case)
# 2: key=             - single argument function
# 3: lambda           - we are using an anonymous function instead of a named one
# 4: family_name      - each of the items of the iterable
# 5: len(family_name) - calculate the length of each item
#                    1      2    3        4              5
#                  ------  --- ------ -----------  ----------------
longest_name = max(family, key=lambda family_name: len(family_name))
print(f'The longest name in the family is {longest_name}')

# the above could also be accomplished by using just key=len
# shortest name verison:
shortest_name = min(family, key=len)
print(f'The shortest name in the family is {shortest_name}')

# list and dictionaries:
team = [
    {'name': 'Raul', 'position':'shortstop', 'avg':560},
    {'name': 'Diego', 'position':'third base', 'avg':575},
    {'name': 'Juan Carlos', 'position':'pitcher', 'avg':670},
    {'name': 'Nori', 'position':'centerfielder', 'avg':445},
    {'name': 'Victor', 'position':'catcher', 'avg':410},
]
# returns the dictionary with the highest average:
mvp = max(team, key=lambda player: player['avg'])

print('*** The Brussels Kangaroos Softball team 2019 Most Valuable Player award goes to:')
print(f'{mvp["name"]}! with a batting average of: {mvp["avg"]}')

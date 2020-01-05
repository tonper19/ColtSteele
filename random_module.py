import random

teams = ['Kangaroos', 'Bears', 'Pioneers', 'Spartans', 'Afterburners', 'Titans', 'Squirrels']

print('-' * 80)
print('suffle a list:')
random.shuffle(teams)
print(teams)

print('-' * 80)
print('random selection from a list:')
print(random.choice(teams))

print('-' * 80)
print('random integer selection from 1 to 100:')
print(random.randint(1, 100))

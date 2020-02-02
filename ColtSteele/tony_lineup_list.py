
kangaroos_lineup = ['Nathan', 'Cedric', 'Peter', 'Juan', 'Guillaume', 'Juan Carlos', 'Ryouga', 'Miguel', 'Gabriel']

for player in kangaroos_lineup:
    print(player)

print('The Kangaroos lineup:')

idx = 0
while idx < len(kangaroos_lineup):
    print(f'{idx + 1}. {kangaroos_lineup[idx]}')
    idx += 1


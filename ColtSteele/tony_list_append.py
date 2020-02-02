
players = []

player_name = ''

while player_name != 'quit':
    player_name = input('Enter a player name ')

    if player_name != 'quit':
        players.append(player_name)

print(players)



from random import randint

player_wins = 0 
computer_wins = 0
winning_score = 3
player = ''

# for time in range(2):
while player != 'quit':
    print(f'Player score: {player_wins} computer score: {computer_wins}')
    print('...Rock...') 
    print('...Paper...')
    print('...Scissors...')

    player = input('(Enter your choice): ').lower()

    if player == 'quit' or input == 'q':
        break

    rand_num = randint(0,2)
    if rand_num == 0:
        computer = 'rock'
    elif rand_num == 1:
        computer = 'paper'
    else:
        computer = 'scissors'

    print(f'Computer plays {computer} so the result is')    

    if player == computer:
        print("it's a tie!")
    elif player == 'rock':
        if computer == 'scissors':
            print('You win!')
            player_wins += 1
        elif computer == 'paper':
            print('the computer wins!')
            computer_wins += 1
    elif player == 'paper':
        if computer == 'rock':
            print('You wins!')
            player_wins += 1
        elif computer == 'scissors':
            print('the computer wins')
            computer_wins += 1
    elif player == 'scissors':
        if computer == 'paper':
            print('You wins!')
            player_wins += 1
        elif computer == 'rock':
            print('the computer wins')
            computer_wins += 1
    else:
        print('something went wrong')

print('Thank you for playing Miguels game')
print(f'FINAL SCORES... Player score: {player_wins} computer score: {computer_wins}')

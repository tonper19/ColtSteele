import pyfiglet
from termcolor import colored

msg = input('Please enter a text: ')
color = input('Please enter a color: ')

valid_colors = ('red', 'green', 'yellow', 'blue', 'magenta', 'cyan', 'white')

if color not in valid_colors:
    msg = f'The color {color} is not valid, using green instead...'
    color = 'green'

ascii_art = pyfiglet.figlet_format(msg)
colored_ascii = colored(ascii_art, color=color)
print(colored_ascii)

from pyfiglet import figlet_format
from termcolor import colored

valid_colors = ('red', 'green', 'yellow', 'blue', 'magenta', 'cyan', 'white')


def print_art(msg, color):
    if color not in valid_colors:
        msg = f'The color {color} is not valid, using green instead...'
        color = 'green'

    ascii_art = figlet_format(msg)
    colored_ascii = colored(ascii_art, color=color)
    print(colored_ascii)


if __name__ == "__main__":
    msg = input('Please enter a text: ')
    color = input('Please enter a color: ')
    print_art(msg, color)

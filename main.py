#!/usr/bin/env python

import getch
import time
import argparse
from colorama import Fore
import string
import random

parser = argparse.ArgumentParser(description=' This program pretend measure your typing accuracy!')
parser.add_argument('--mv', '--max_value',
                    help='As the first argument' + Fore.RED + ' maxValue' + Fore.BLACK + ', please insert an integer number.\n',
                    action="store", default=10, type=int)
parser.add_argument('--utm',
                    help='As second argument, please insert:' + Fore.RED + ' utm' + Fore.BLACK + ' to play (maxValue) seconds, if else you play (maxValue) atemps',
                    action="store", type=bool)

tempo_do = parser.parse_args()

# print(tempo_do.__dict__["one"])


def gameOn(letters, number_typed_letters):
    letter = random.choice(letters)

    print("Type letter " + Fore.LIGHTBLUE_EX + str(letter) + Fore.RESET)
    char = getch.getch()
    number_typed_letters += 1
    if char == letter:
        print("You typed letter " + Fore.GREEN + str(char) + Fore.RESET)
    else:
        print("You typed letter " + Fore.RED + str(char) + Fore.RESET)
    return char



def printAllCharsUpTo(stop_char):
    """
    Pythonic version!
    :param stop_char:
    :return:
    """
    # para instalar o getch
    # pip install https://pypi.python.org/packages/source/g/getch/getch-1.0-python2.tar.gz#md5=586ea0f1f16aa094ff6a30736ba03c50
    inputs = []

    while True:
        start_time = time.time()
        char = getch.getch()  # also displayed on the screen
        final_time = time.time()
        print("Time elapsed is " + str(final_time - start_time) + "seconds")
        print("You have entered  " + char)
        if char == 'X':
            break
        else:
            inputs.append(char)

    print('Here is the list of all your inputs: ' + str(inputs))

    # Ex 5a Processing of list of inputs
    total_numerics = 0
    for input in inputs:
        if input.isdigit():
            total_numerics += 1
    print('Total numeric inputs is ' + str(total_numerics))


def main():
    number_typed_letters = 0
    print("Welcome to the " + Fore.RED + "PARI " + Fore.LIGHTBLUE_EX + "Ultimate Speed Typing Test." + Fore.RESET)
    print("Please, when you're ready, press any key.")
    char = getch.getch()

    print("The game will start in " + Fore.LIGHTBLUE_EX + "3" + Fore.RESET)
    time.sleep(1)

    print("The game will start in " + Fore.LIGHTBLUE_EX + "2" + Fore.RESET)
    time.sleep(1)

    print("The game will start in " + Fore.LIGHTBLUE_EX + "1" + Fore.RESET)
    time.sleep(1)

    letters = string.ascii_letters[0:26]
    init_time = time.time()

    # ARGUMENTOS


    max_value = 10
    utm = True

    if not utm:
        while number_typed_letters < max_value:
            char = gameOn(letters, number_typed_letters)
    else:
        while time.time()-init_time < max_value:
            char = gameOn(letters, number_typed_letters)

        if time.time() - init_time <= max_value:
            print("Current test duration is " + str(time.time() - init_time))
        else:
            print("\n" + Fore.RED + "WARNING: " + Fore.RESET + "Current test duration (" + str(time.time() - init_time) + ") exceeded the maximum of " + str(max_value) + ":")
            print("The last typed letter (" + str(char) + ") will not count")

    print(Fore.LIGHTBLUE_EX + "Test finished!" + Fore.RESET)

    # # not displayed in the screen
    # print('You have entered  ' + char)
    # printAllCharsUpTo(char)


if __name__ == '__main__':
    main()

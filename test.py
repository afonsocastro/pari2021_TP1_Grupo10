#!/usr/bin/env python

import getch
import time
import argparse
from colorama import  Fore

parser = argparse.ArgumentParser(description='Inserir numero de letras ou segundos para jogar')
parser.add_argument('--witharg2', action="store", default=10, dest="witharg2", type=int)
# parser.add_argument('--witharg3', action="store", default=10, dest="witharg3", type = int, descreption=)


tempo_do = parser.parse_args()

# print(tempo_do.__dict__["one"])


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
    print("Welcome to the " + Fore.RED + "PARI " + Fore.BLUE + "Ultimate Speed Typing Test." + Fore.RESET)
    print("Please, when you're ready, press any key.")
    char = getch.getch()
    # not displayed in the screen
    print('You have entered  ' + char)
    printAllCharsUpTo(char)


if __name__ == '__main__':
    main()

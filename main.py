#!/usr/bin/env python



import getch
import time
import argparse
from colorama import Fore
import string
import random
from collections import namedtuple
import pprint
Input = namedtuple("Input", ['requested', 'received', 'duration'])

parser = argparse.ArgumentParser(description=' This program aims to measure your typing accuracy!', epilog="And now you can pass to action!")
parser.add_argument('max_value', metavar='MaxValue',nargs='?',
                    help='As the first argument' + Fore.RED + ' MaxValue' + Fore.BLACK + ', please insert an integer number. By default is 10!\n',
                    action="store", default=10, type=int)
parser.add_argument('utm',metavar='UserTimeMode',nargs='?',
                    help='As second argument, please insert:' + Fore.RED + ' utm' + Fore.BLACK + ' to play (MaxValue) seconds, if else, you play (MaxValue) atemps',
                    action="store", type=str,default=False)


tempo_do = parser.parse_args()
#print (tempo_do.utm)

if tempo_do.utm=='utm':
    game_mode=True #play number by time
else:
    game_mode = False #play by number of attemps
#print (game_mode)

# print(tempo_do.__dict__["one"])
TupList = []
dictionary = {"accuracy": "", "number of hits": "", "number of types": "", "test duration": "",
              "test start": "", "test end": "", "type average time": "", "type hit average time": "",
              "type miss average time": "", "Every type data": ""}


def gameOn(letters, number_typed_letters):
    letter = random.choice(letters)
    print("Type letter " + Fore.LIGHTBLUE_EX + str(letter) + Fore.RESET)
    init_time = time.time()
    char = getch.getch()
    type_time = time.time()
    elapsed_time = type_time - init_time
    number_typed_letters += 1
    if char == letter:
        print("You typed letter " + Fore.GREEN + str(char) + Fore.RESET)
    else:
        print("You typed letter " + Fore.RED + str(char) + Fore.RESET)

    triple = Input(letter, str(char), str(elapsed_time))
    TupList.append(triple)
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


def main():
    number_typed_letters = 0
    hitkeys = 0
    misses = 0
    print("Welcome to the " + Fore.RED + "PARI " + Fore.LIGHTBLUE_EX + "Ultimate Speed Typing Test." + Fore.RESET)
    if not game_mode:
        print("You will play for "+Fore.RED + "{}".format(tempo_do.max_value) + Fore.RESET+" atemps".format(tempo_do.max_value))
    else:
        print("You will play for "+Fore.RED + "{}".format(tempo_do.max_value) + Fore.RESET+" seconds")
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


    max_value = 5
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
            print("\n" + Fore.RED + "WARNING: " + Fore.RESET + "Current test duration (" +
                  str(time.time() - init_time) + ") exceeded the maximum of " + str(max_value) + ":")
            print("The last typed letter (" + str(char) + ") will not count")
    print(Fore.LIGHTBLUE_EX + "Test finished!" + Fore.RESET)
    pprint.pprint(dictionary)
    print('\n'.join(map(str, TupList)))


    # # not displayed in the screen
    # print('You have entered  ' + char)
    # printAllCharsUpTo(char)


if __name__ == '__main__':
    main()

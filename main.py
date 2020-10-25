#!/usr/bin/env python

import sys
import getch
import time
import argparse
from colorama import Fore
import string
import random
from collections import namedtuple
import pprint
import datetime

from pyfiglet import Figlet


Input = namedtuple("Input", ['requested', 'received', 'duration'])


# global vars
number_typed_letters = 0
hits = 0
misses = 0
total_time = 0

# help context and input args
parser = argparse.ArgumentParser(description=' This program aims to measure your typing accuracy.', epilog="And now you are ready to play!")


parser.add_argument('-mv', '--max_value', help="Please insert an integer number. " + Fore.LIGHTBLUE_EX + ' MaxValue' + Fore.RESET + ' is the max of seconds (if' + Fore.LIGHTBLUE_EX + ' utm' + Fore.RESET + ' is set true) or the max of attempts (if' + Fore.LIGHTBLUE_EX + ' utm' + Fore.RESET + ' is set false). By default, ' + Fore.LIGHTBLUE_EX + ' MaxValue' + Fore.RESET + ' is 10.\n', action="store", default=10, type=int)

parser.add_argument('-utm', '--utm', help='Please select:' + Fore.LIGHTBLUE_EX + ' utm' + Fore.RESET
                                          + ' to play (' + Fore.LIGHTBLUE_EX + 'MaxValue' + Fore.RESET + ') seconds. Otherwise, you will play (' + Fore.LIGHTBLUE_EX + 'MaxValue' + Fore.RESET + ') attempts', action="store_true", default=False)


tempo_do = parser.parse_args()

# ARGUMENTS
max_value = tempo_do.max_value
utm = tempo_do.utm


TupList = []
Timehitlist = []
Timemisslist = []
TimetotalList = []
dictionary = {"accuracy": "", "number of hits": "", "number of types": "", "test duration": "",
              "test start": "", "test end": "", "type average time": "", "type hit average time": "",
              "type miss average time": "", "types": ""}


def delete_last_line():
    """
    Deletes the last line in the terminal
    """

    #cursor up one line
    sys.stdout.write('\x1b[1A')

    #delete last line
    sys.stdout.write('\x1b[2K')


def game_count_down(n):
    """
    Show the seconds (in a pretty way) to start the game
    :param n: number of seconds that remains to start the test
    """

    f = Figlet(font='small')
    print (Fore.LIGHTBLUE_EX)
    print f.renderText(str(n))
    print (Fore.RESET)
    time.sleep(1)
    delete_last_line()
    delete_last_line()
    delete_last_line()
    delete_last_line()
    delete_last_line()
    delete_last_line()
    delete_last_line()
    delete_last_line()


def game_on(letters):
    """
    Pick a random letter and ask the user to type that same letter.
    Wait for the user answer and then save the correct or the wrong answers number. Besides this, it also saves the time that took the user to type the requested letter.
    :param letters: string with all the possible letter for the program to ask
    :return char: character that the user has pressed
    """

    letter = random.choice(letters)
    print("Type letter " + Fore.LIGHTBLUE_EX + str(letter) + Fore.RESET)
    init_time = time.time()
    char = getch.getch()
    global number_typed_letters
    number_typed_letters += 1
    # print(number_typed_letters)
    type_time = time.time()
    elapsed_time = type_time - init_time
    TimetotalList.append(elapsed_time)
    SummedTimes = sum(TimetotalList)
    if char == letter:
        if SummedTimes <= max_value:
            print("You typed letter " + Fore.GREEN + str(char) + Fore.RESET)
            global hits
            hits += 1
            Timehitlist.append(elapsed_time)
        else:
            print("You typed letter " + Fore.LIGHTYELLOW_EX + str(char) + Fore.RESET + " (Time exceeded!)")

    elif char != " ":
        if SummedTimes <= max_value:
            print("You typed letter " + Fore.RED + str(char) + Fore.RESET)
            global misses
            misses += 1
            Timemisslist.append(elapsed_time)
        else:
            print("You typed letter " + Fore.LIGHTYELLOW_EX + str(char) + Fore.RESET + " (Time exceeded!)")

    triple = Input(letter, str(char), str(elapsed_time))
    TupList.append(triple)
    return char


def main():

    print("Welcome to the " + Fore.RED + "PARI " + Fore.LIGHTBLUE_EX + "Ultimate Speed Typing Test." + Fore.RESET)
    if not utm:
        print("You will play for "+Fore.RED + "{}".format(tempo_do.max_value) + Fore.RESET +
              " attempts".format(tempo_do.max_value))
    else:
        print("You will play for " + Fore.RED + "{}".format(tempo_do.max_value) + Fore.RESET+" seconds")
    print("You can quit the test, at any time, by pressing the spacebar key.")
    print("Please, when you're ready, press any key.")
    char = getch.getch()

    print("The game will start in:")
    game_count_down(3)
    game_count_down(2)
    game_count_down(1)
    # print(Fore.LIGHTBLUE_EX+'GOOD LUCK'+Fore.RESET)

    letters = string.ascii_letters[0:26]
    init_time = time.time()
    init_date = datetime.datetime.now()

    if not utm:
        while number_typed_letters < max_value:
            char = game_on(letters)
            global total_time
            total_time = time.time() - init_time
            if char == " ":
                print("\n Uh oh! You've cancelled the " + Fore.LIGHTBLUE_EX + "Ultimate Speed Typing Test " + Fore.RESET + ".")
                quit()

    else:
        while time.time()-init_time < max_value:
            char = game_on(letters)
            if char == " ":
                print("\nUh oh! You've cancelled the " + Fore.LIGHTBLUE_EX + "Ultimate Speed Typing Test " + Fore.RESET + ".")
                quit()
        if time.time() - init_time <= max_value:
            total_time = float(time.time() - init_time)
            print("Current test duration is " + str(total_time))

        else:
            total_time = time.time() - init_time
            print("\n" + Fore.RED + "WARNING: " + Fore.RESET + "Current test duration (" +
                  str('{:0.2f}'.format(total_time)) + " sec) exceeded the maximum of " + str(max_value) + "sec:")
            print("The last typed letter (" + str(char) + ") will not count")

    final_date = datetime.datetime.now()
    print(Fore.LIGHTBLUE_EX + "Test finished!" + Fore.RESET)
    TimeHit = sum(Timehitlist)
    Timemiss = sum(Timemisslist)
    dictionary["accuracy"] = str('{:0.2f}'.format(float(hits)/(float(hits) + float(misses)) * 100)) + " %"
    dictionary["number of hits"] = hits
    dictionary["number of types"] = hits + misses
    dictionary["test duration"] = '{:0.2f}'.format(total_time) + " seconds"
    dictionary["test start"] ='{:%Y-%m-%d %H:%M.%S}'.format((init_date))
    dictionary["test end"] = '{:%Y-%m-%d %H:%M.%S}'.format((final_date))
    dictionary["type average time"] = '{:0.2f}'.format((TimeHit + Timemiss)/(hits + misses)) + " seconds"

    dictionary["type hit average time"] = '{:0.2f}'.format(TimeHit / hits) + " seconds" if hits != 0 else str(0) + " seconds"

    dictionary["type miss average time"] = '{:0.2f}'.format(Timemiss / misses) + " seconds" if misses != 0 else str(0) + " seconds"

    dictionary["types"] = map(str, TupList)
    pprint.pprint(dictionary)
    print("\n" + Fore.LIGHTBLUE_EX +"          GAME OVER             " +Fore.RESET)


if __name__ == '__main__':
    main()



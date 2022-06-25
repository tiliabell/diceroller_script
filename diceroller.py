#!/usr/bin/env python
from random import randint
from time import sleep


welcome_msg = """
    *************************************
    ** Welcome to Tilia's Dice Roller. **
    *************************************
"""

info_msg = """
Type a number followed by the letter \"d\" followed by another number to 
roll some dice. The first number is the quantity of dice. The second 
number is the type of die aka the number of sides on each die.

Optionally add a 3rd number as a modifier. i.e. 1d20 +3

Type \"r\" to repeat the previous roll.
Type \"help\" to repeat this prompt. \n
Type \"q\" to exit.
"""

NOT_VALID = "\nThat's not a valid roll. Please try again.\n"

prev_roll = None


def err(error_msg):
    print(error_msg)


def sanitize(input_string):
    """Takes a str as input, removes weird chars, and outputs the 
    string in lower case

    """

    input_string = input_string.lower()
    sanitized_string = ""
    for i in input_string:
        if i.isalnum() or i == "+":
            sanitized_string += i
    return sanitized_string


def parse_dicestring(dicestring):
    num = ""
    die = ""
    mod_str = "0"
    if "+" in dicestring:
        roll_str, mod_str = dicestring.split("+")
    else:
        roll_str = dicestring
    num_str, die_str = roll_str.split("d")
    try:
        num = int(num_str)
        die = int(die_str)
        mod = int(mod_str)
    except:
        err("num or die not a decimal")
        exit(1)

    if num < 1 or die < 2:  # num must be at least 1, and die must be at least 2
        err("Number of dice must be at least 1, and die must be at least 2")
        exit(1)
    return num, die, mod


def roll_em(num, die, mod):
    """Takes a quantity "num" and a die-type "die", rolls 'em, and 
    prints each roll and the total and returns the total"""
    total = 0
    while num > 0:
        roll = randint(1, die)
        total += roll
        print(roll)
        num -= 1
    return total + mod


def display_total(total):
    print("\nFinal roll total: {}".format(total))


def crit_check(total):
    if total == 20:
        print("\n!!! Critical Hit !!! \n")
        # sleep(1)
        # reroll = randint(1,20)
        # print("Original roll: {0}    Reroll: {1}\n ".format(total,reroll))

    elif total == 1:
        print("!!! Critical Failure !!! \n")
        # sleep(1)
        # reroll = randint(1,20)
        # print("Original Roll: {0}    Reroll: {1}\n ".format(total,reroll))


def main():
    """diceroller has no parameters; runs until the user exits

    While diceroller is running, it will continually loop, starting 
    out with asking for the user to input a "roll." The input must 
    start with a number, end with a number, and only contain the letter
    "d" in between. It is not case sensitive, and the user may put 
    spaces or not between them. 
    If the input is not recognized, an error message will appear, and 
    it wil send the user back to the original prompt. 
    If the user types "help" it will display a helpful message.
    If the user types "q" (not case sensitive), it will end the program.
    If the user types "r" (not case sensitive), it will reuse the previous roll.

    """
    prev_roll = None
    while True:
        dicestring = sanitize(input("\nDice to roll: "))
        if dicestring == "q":
            print("Thanks for rolling!\n")
            exit(0)
        elif dicestring == "r":
            if prev_roll == None:
                print("No previous rolls available.")
                continue
            else:
                dicestring = prev_roll
        elif dicestring == "help" or dicestring == "h":
            print(info_msg)
            continue
        elif len(dicestring) < 3 or "d" not in dicestring:
            err(NOT_VALID)
            continue
        num, die, mod = parse_dicestring(dicestring)
        mod_text = f" + {mod}" if mod else ""

        print(f"\nRolling {num} d{die}{mod_text}...")

        total = roll_em(num, die, mod)
        if num > 1 or mod:
            display_total(total)
        if dicestring == "1d20":
            crit_check(total)
        prev_roll = dicestring


if __name__ == "__main__":

    print(welcome_msg)
    print(info_msg)
    main()

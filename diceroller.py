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

Type \"r\" to repeat the previous roll.
Type \"help\" to repeat this prompt. \n
Type \"q\" to exit.
"""

error_msg = "\nThat's not a valid roll. Please try again.\n"

prev_roll = None

def err():
    print(error_msg)

def sanitize(input_string):
    """Takes a str as input, removes weird chars, and outputs the 
    string in lower case

    """
    input_string = input_string.lower()
    sanitized_string = ""
    for i in input_string:
        if i.isalnum():
            sanitized_string += i
    return sanitized_string

def roll_em(num,die):
    """Takes a quantity "num" and a die-type "die", rolls 'em, and 
    prints each roll and the total and returns the total"""
    total = 0
    while num > 0:
        roll = randint(1,die)
        total += roll
        print(roll)
        num -=1
    return total

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



def diceroller():
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

        num = ""
        die = ""
        if dicestring == "q":
            print("Thanks for rolling!\n")
            break
        elif dicestring == "r":
            if prev_roll == None:
                print("No Previous rolls available.")
                continue
            else:
                dicestring = prev_roll
        elif dicestring == "help":
            print(info_msg)
            continue
        elif len(dicestring) < 3 or "d" not in dicestring:
            err()
            continue
        for i in range(len(dicestring)):

            if dicestring[i] == "d":
                num = dicestring[:i]
                die = dicestring[(i+1):]
        if not num.isdecimal() or not die.isdecimal():
            err()
            continue
        

        num = int(num)
        die = int(die)

        if num < 1 or die < 2 : # num must be at least 1, and die must be at least 2
            err()
            continue

        print("\nRolling {0} d{1}...".format(num,die))

        total = roll_em(num,die)
        if num > 1:
            display_total(total)
        if dicestring =="1d20":
            crit_check(total)
        prev_roll = dicestring

        

        
        #reroll = sanitize(input("Reroll? Y/N " ))
        #if reroll == "n" or reroll == "exit":
        #    cont = False
            
print(welcome_msg)
print(info_msg)
diceroller()

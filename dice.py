import os
import time
from random import randint
from dices import dices


def roll_dice():
    n = 0
    while n < 3:
        dice = randint(1, 6)
        os.system('clear')
        if dice == 1:
            dices.one()
        if dice == 2:
            dices.two()
        if dice == 3:
            dices.three()
        if dice == 4:
            dices.four()
        if dice == 5:
            dices.five()
        if dice == 6:
            dices.six()
        time.sleep(.400)
        n += 1


keep_rolling = True
while keep_rolling:
    user_input = input("\nRoll the dice (y/n): ")
    if user_input.lower() == 'y':
        roll_dice()
    elif user_input.lower() == 'n':
        keep_rolling = False
        os.system('clear')
        print("\nHave a nice day!!")
    else:
        print("\nWrong input type (y)es to roll again or (n)o to exit")

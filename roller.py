#!/usr/bin/env python

# roller.py
# AUTHOR: JONAH MILLER (JONAH.MILLER@COLORADO.EDU)

# The main dice roller function

import dice

def main ():
    quit_var = True
    while(quit_var):
        print("Dice roller!")
        number_dice = input("How many dice? ")
        number_sides = input("What sided dice are they? ")
        if (number_dice or number_sides) == "quit":
            quit_var=False
        else:
            result = dice.roll_ndm(int(number_sides),int(number_dice))
            total = sum(result)
            print("results...")
            print(result)

main()

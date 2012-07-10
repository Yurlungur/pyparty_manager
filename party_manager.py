#!/usr/bin/env python

# party_manager.py
# Author: Jonah Miller

# This is the main wrapper for my D&D party management software
# written in python. 

# Dependencies:
import characters # Character sheets stored as nested dictionaries
import random as rand # Random number generator
import dice # Dice rolling functions
from dnd_classes import * # The main classes used: 
                          # weapon
                          # character
                          # party

# Build the party from a configuration file.
pp = party(characters.char_hash)

# Additional classes for your individual party members.
isaac = character(characters.isaac)
paulo = character(characters.paulo)
emily = character(characters.emily)


def print_dic(dictionary):
    "Prints a dictionary."
    print("Result\tBonus")
    for i in dictionary.keys():
        print("{}\t{}".format(i,dictionary[i]))
    return


# Some convenient shorthand functions
def initiative():
    "Roll initiative for the party."
    initiatives = pp.roll_att('INITIATIVE')
    print_dic(initiatives)
    return initiatives

def spot():
    "Roll spot checks for the party."
    spots = pp.roll_skill('SPOT')
    print_dic(spots)
    return spots

def listen():
    "Roll listen checks for the party."
    listens = pp.roll_skill('LISTEN')
    print_dic(listens)
    return listens

def search():
    "Roll search checks for the party."
    searches = pp.roll_skill('SEARCH')
    print_dic(searches)
    return searches

def hide():
    "Roll hide checks for the whole party."
    hides = pp.roll_skill('HIDE')
    print_dic(hides)
    return hides

def move_silently():
    "Move silently for the whole party."
    silents = pp.roll_skill('MOVE SILENTLY')
    print_dic(silents)
    return silents

def list_attacks(charname):
    "List attacks a character has."
    return pp.members[charname].ATTACKS.keys()

def make_attack(charname,attackname):
    "Make an attack using a character and an attack."
    return pp.members[charname].ATTACKS[attackname].make_attack()
    


def main():
    print("Party manager!\n Manage your party!\n A tool for DMs!")

main()

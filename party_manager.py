#!/usr/bin/env python

# party_manager.py
# Author: Jonah Miller

# This is the main wrapper for my D&D party management software
# written in python. 

# Dependencies:
import legacy # Contains dictionaries with character stats

import dice # Dice rolling functions
from dnd_classes import * # The main classes used: 
                          # weapon
                          # character
                          # party
from characters import *


# Initialize the party class. Useful only for rolling things for a
# specific party if you segregate the party.
pp = party(character_list)

def print_dic(dictionary):
    "Prints a dictionary."
    print("Result\tBonus")
    for i in dictionary.keys():
        print("{}\t{}".format(i,dictionary[i]))
    return


# Some convenient shorthand functions
def roll_att(attribute):
    """Rolls an arbitrary attribute for the entire party. Different
    from roll_skill. Accepts a string.

    Returns:
    {'charname':[result,bonus],...}
    """
    rolls = {} # Represent roll per character. Use human-readable strings.
    for i in character_list: # Character dict holds character
                             # object strings.
        charname = i.name # Get the key as the character name
        # Attribute you care about. References a dictionary inside
        # character class. That dictionary transforms a human-readable
        # string to an attribute of a character.
        c_attribute = i.map(attribute) 
        # Add the roll to the dictionary with the character name as the key.
        rolls[charname] = [dice.roll_1dx(20) + c_attribute,c_attribute]
    return rolls # Return the dictionary.

def roll_skill(skill):
    """Rolls an arbitrary skill for the entire party. Different from
    roll_att. Accepts a string.
    
    Returns:
    {'charname':[result,bonus],...}
    """
    rolls = {} # Represent roll per character. Use human-readable strings.
    for i in character_list: # Character dict holds character
                             # object strings.
        charname = i.name # Get the key as the character name
        # Skills for the character.
        c_skills = i.SKILLS
        # Skills you care about. If the skill is known by the
        # character, just access the correct skill, which is stored as
        # a value in a dictionary. Otherwise, use the generalized
        # skill map which includes ALL skills.
        if skill in c_skills.keys():
            c_skill = c_skills[skill]
        else:
            c_skill = i.map(skill_map[skill])
        rolls[charname] = [dice.roll_1dx(20) + c_skill, c_skill] # Make the roll
        return rolls # Return the dictionary.

def initiative():
    "Roll initiative for the party."
    initiatives = roll_att('INITIATIVE')
    print_dic(initiatives)
    return initiatives

def spot():
    "Roll spot checks for the party."
    spots = roll_skill('SPOT')
    print_dic(spots)
    return spots

def listen():
    "Roll listen checks for the party."
    listens = roll_skill('LISTEN')
    print_dic(listens)
    return listens

def search():
    "Roll search checks for the party."
    searches = roll_skill('SEARCH')
    print_dic(searches)
    return searches

def hide():
    "Roll hide checks for the whole party."
    hides = roll_skill('HIDE')
    print_dic(hides)
    return hides

def move_silently():
    "Move silently for the whole party."
    silents = roll_skill('MOVE SILENTLY')
    print_dic(silents)
    return silents

def main():
    print("Party manager!\n Manage your party!\n A tool for DMs!")

main()

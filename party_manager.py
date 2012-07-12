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
    """
    Rolls an arbitrary skill for the entire party. Different from
    roll_att. Accepts a string.
    
    Returns:
    {'charname':[result,bonus],...}
    """
    rolls = {} # Represent roll per character. Use human-readable strings.
    for chtr in character_list: # Character dict holds character
                                # object strings.
        charname = chtr.name # Get the key as the character name
        # Skills for the character.
        c_skills = chtr.SKILLS
        # Skills you care about. If the skill is known by the
        # character, just access the correct skill, which is stored as
        # a value in a dictionary. Otherwise, use the generalized
        # skill map which includes ALL skills.
        if skill in list(c_skills.keys()):
            c_skill = c_skills[skill]
        else:
            c_skill = chtr.map(skill_map[skill])
        # Make the roll
        rolls[charname] = [dice.roll_1dx(20) + c_skill, c_skill] 
    return rolls # Return the dictionary.


def roll():
    return dice.roll_1dx(20)

def initiative(charlist = []):
    """
    Roll initiative for the party. If arguments given, do it for the
    character list.
    """
    if len(charlist) == 0:
        initiatives = roll_att('INITIATIVE')
        print_dic(initiatives)
        return initiatives
    else:
        rolls = {}
        for i in charlist:
            rolls[i.name] = [dice.roll_1dx(20) + i.INITIATIVE, i.INITIATIVE]
        print_dic(rolls)
        return rolls

def spot(charlist = []):
    """
    Roll spot checks for the party. If arguments given, do it for the
    character list.
    """
    if len(charlist) == 0:
        spots = roll_skill('SPOT')
        print_dic(spots)
        return spots
    else:
        rolls = {}
        for i in charlist:
            rolls[i.name] = i.roll_skill('SPOT')
        print_dic(rolls)
        return rolls

def listen(charlist = []):
    """"
    Roll listen checks for the party. If arguments given, do it for the
    character list.
    """
    if len(charlist) == 0:
        listens = roll_skill('LISTEN')
        print_dic(listens)
        return listens
    else:
        rolls = {}
        for i in charlist:
            rolls[i.name] = i.roll_skill('LISTEN')
        print_dic(rolls)
        return rolls

def search(charlist = []):
    """"
    Roll search checks for the party. If arguments given, do it for the
    character list.
    """
    if len(charlist) == 0:
        searches = roll_skill('SEARCH')
        print_dic(searches)
        return searches
    else:
        rolls = {}
        for i in charlist:
            rolls[i.name] = i.roll_skill('SEARCH')
        print_dic(rolls)
        return rolls

def hide(charlist = []):
    """
    Roll hide checks for the whole party. If arguments given, do it for the
    character list.
    """
    if len(charlist) == 0:
        hides = roll_skill('HIDE')
        print_dic(hides)
        return hides
    else:
        rolls = {}
        for i in charlist:
            rolls[i.name] = i.roll_skill('HIDE')
        print_dic(rolls)
        return rolls

def move_silently(charlist = []):
    """
    "Move silently for the whole party. If arguments given, do it for the
    character list.
    """
    if len(charlist) == 0:
        silents = roll_skill('MOVE SILENTLY')
        print_dic(silents)
        return silents
    else:
        rolls = {}
        for i in charlist:
            rolls[i.name] = i.roll_skill('MOVE SILENTLY')
        print_dic(rolls)
        return rolls

# SAVES
def fort():
    "Fortitude saves for the whole party."
    forts = roll_att('FORT')
    print_dic(forts)
    return forts

def ref():
    "Reflex saves for the whole party."
    refs = roll_att('REF')
    print_dic(refs)
    return refs

def will():
    "Will saves for the whole party."
    wills = roll_att('WILL')
    print_dic(wills)
    return wills

def main():
    print("Party manager!\n Manage your party!\n A tool for DMs!")

main()

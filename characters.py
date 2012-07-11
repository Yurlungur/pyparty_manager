#!/usr/bin/env python

# characters.py
# Author: Jonah Miller (jonah.miller@colorado.edu)

# This file holds initialization of characters


# Dependencies
import legacy # Character sheets stored as nested dictionaries
import dnd_classes # main classes used: weapon,character,party

# Classes for your individual party members.
isaac = dnd_classes.character()
isaac.read_from_dict(legacy.isaac)
paulo = dnd_classes.character()
paulo.read_from_dict(legacy.paulo)
emily = dnd_classes.character()
emily.read_from_dict(legacy.emily)

# Character name dictionary. Used in party class initialization:
character_list = [isaac,paulo,emily]



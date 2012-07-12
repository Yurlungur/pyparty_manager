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

# Initialize new characters
# Ali
ali = dnd_classes.character()
ali.name = "Ali"
ali.STR = -1
ali.DEX = 3
ali.CON = 1
ali.INT = -1
ali.WIS = 1
ali.CHA = 2
ali.BA = 1
ali.GRA = -1
ali.INITIATIVE = 3
ali.AC = {'FULL':15,
          'TOUCH':13,
          'FLAT-FOOTED':12}
ali.SAVES = {'FORT':1,
             'REF':3,
             'WILL':0}
ali.ATTACKS = {'short sword':[[0],[1,6,0],[19,2]],
               'short bow':[[4],[1,6,0],[20,3]],
               'FULL':[[0],[1,6,0],[19,2]]}
ali.SKILLS = {'CLIMB':1,
              'CRAFT MAKING ARROWS':0,
              'DIPLOMACY':4,
              'DISABLE DEVICE':2,
              'ESCAPE ARTIST':7,
              'GATHER INFORMATION':6,
              'HIDE':8,
              'KNOWLEDGE (DUNGEONEERING)':0,
              'LISTEN':8,
              'MOVE SILENTLY':6,
              'OPEN LOCK':4,
              'SENSE MOTIVE':3,
              'SLEIGHT OF HAND':5,
              'SPOT':5}

# Character name dictionary. Used in party class initialization:
character_list = [isaac,paulo,emily,ali]



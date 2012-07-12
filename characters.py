#!/usr/bin/env python

# characters.py
# Author: Jonah Miller (jonah.miller@colorado.edu)

# This file holds initialization of characters


# Dependencies
import legacy # Character sheets stored as nested dictionaries
import dnd_classes # main classes used: weapon,character,party

# Classes for your individual party members.
"""
isaac = dnd_classes.character()
isaac.read_from_dict(legacy.isaac)
paulo = dnd_classes.character()
paulo.read_from_dict(legacy.paulo)
emily = dnd_classes.character()
emily.read_from_dict(legacy.emily)
"""

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
ali.FORT = 1
ali.REF = 6
ali.WILL = 1
ali.AC = {'FULL':15,
          'TOUCH':13,
          'FLAT-FOOTED':12}
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
			  'LISTEN':8,
			  'MOVE SILENTLY':6,
			  'OPEN LOCK':4,
			  'SEARCH':0,
			  'SENSE MOTIVE':3,
			  'SLEIGHT OF HAND':5,
			  'SPOT':5}

# Emily
emily = dnd_classes.character()
emily.name = "Emily"
emily.STR = 1
emily.DEX = 2
emily.CON = 1
emily.INT = 0
emily.WIS = 2
emily.CHA = 0
emily.BA = 1
emily.GRA = 1
emily.INITIATIVE = 2
emily.FORT = 4
emily.REF = 5
emily.WILL = 5
emily.AC = {'FULL':14,
          'TOUCH':14,
          'FLAT-FOOTED':12}
emily.ATTACKS = {'unarmed':[[2],[1,6,1],[20,2]],
               'sling':[[3],[1,4,0],[20,2]],
               'FULL':[[0,0],[1,6,1],[20,2]]}
emily.SKILLS = {
			  'CLIMB':2,
			  'CONCENTRATION':2,
			  'DIPLOMACY':2,
			  'HIDE':4,
			  'JUMP':2,
			  'KNOWLEDGE NATURE':2,
			  'LISTEN':4,
			  'MOVE SILENTLY':5,
			  'SENSE MOTIVE':4,
			  'SP0T':3,
			  'SURVIVAL':4
			  }

# Isaac
isaac = dnd_classes.character()
isaac.name = "Isaac"
isaac.STR = 2
isaac.DEX = 0
isaac.CON = -1
isaac.INT = 2
isaac.WIS = 0
isaac.CHA = -1
isaac.BA = 2
isaac.GRA = 4
isaac.INITIATIVE = 0
isaac.FORT = 2
isaac.REF = 3
isaac.WILL = 0
isaac.AC = {'FULL':15,
          'TOUCH':10,
          'FLAT-FOOTED':12}
isaac.ATTACKS = {'scimitar':[[4],[1,6,2],[18,2]],
               'shortbow':[[3],[1,6,2],[20,3]],
               'FULL':[[4,4],[1,6,2],[18,2]]}
isaac.SKILLS = {
			  'CLIMB':5,
			  'CRAFT STONEWORK':4,
			  'HEAL':3,
			  'HIDE':3,
			  'JUMP':3,
			  'KNOWLEDGE DUNGEONEERING':4,
			  'KNOWLEDGE GEOGRAPHY':3,
			  'LISTEN':1,
			  'MOVE SILENTLY':0,
			  'OPEN LOCK':4,
			  'PROFESSION CIVIL ENGINEER':3,
			  'RIDE':2,
			  'SEARCH':4,
			  'SP0T':4,
			  'SURVIVAL':5,
			  'SWIM':4,
			  'USE ROPE':2
			  }

#JJ
jj = dnd_classes.character()
jj.name = "JJ"
jj.STR = 0
jj.DEX = 2
jj.CON = 0
jj.INT = 2
jj.WIS = 1
jj.CHA = 2
jj.BA = 1
jj.GRA = 1
jj.INITIATIVE = 6
jj.FORT = 0
jj.REF = 5
jj.WILL = 4
jj.AC = {'FULL':16,
          'TOUCH':12,
          'FLAT-FOOTED':14}
jj.ATTACKS = {'shortbow':[[3],[1,6,0],[20,3]],
               'rapier':[[1],[1,6,0],[18,2]],
               'FULL':[[1,1],[1,6,0],[20,3]]}
jj.SKILLS = {'APPRAISE':5,
			 'BLUFF':7,
			 'DECIPER SCRIPT':3,
			 'DIPLOMACY':10,
			 'DISGUISE':4,
			 'GATHER INFORMATION':5,
			 'KNOWLEDGE BARDIC':5,
			 'LISTEN':6,
			 'MOVE SILENTLY':5,
			 'PERFORM VIOLIN':7,
			 'SEARCH':4,
			 'SPELLCRAFT':6,
			 'SP0T':3}

#Josh
josh = dnd_classes.character()
josh.name = "Josh"
josh.STR = -1
josh.DEX = 3
josh.CON = 0
josh.INT = 2
josh.WIS = -1
josh.CHA = 0
josh.BA = 1
josh.GRA = 0
josh.INITIATIVE = 3
josh.FORT = 0
josh.REF = 6
josh.WILL = 0
josh.AC = {'FULL':16,
          'TOUCH':13,
          'FLAT-FOOTED':13}
josh.ATTACKS = {'sickle':[[0],[1,6,-1],[20,2]],
               'trident':[[4],[1,6,0],[20,3]],
               'FULL':[[0,0],[1,6,0],[20,2]]}
josh.SKILLS = {
			  'BALANCE':6,
			  'BLUFF':6,
			  'DECIPER SCRIPT':4,
              'DISABLE DEVICE':6,
              'ESCAPE ARTIST':7,
			  'HIDE':6,
			  'LISTEN':3,
			  'MOVE SILENTLY':7,
			  'OPEN LOCK':5,
			  'SEARCH':5,
			  'SENSE MOTIVE':3,
			  'SLEIGHT OF HAND':7,
			  'SPOT':3,
			  'SWIM':7,
			  'TUMBLE':7}

# Paulo
paulo = dnd_classes.character()
paulo.name = "Paulo"
paulo.STR = 3
paulo.DEX = 4
paulo.CON = 0
paulo.INT = 2
paulo.WIS = 3
paulo.CHA = 1
paulo.BA = 2
paulo.GRA = 4
paulo.INITIATIVE = 4
paulo.FORT = 3
paulo.REF = 7
paulo.WILL = 3
paulo.AC = {'FULL':16,
          'TOUCH':14,
          'FLAT-FOOTED':12}
paulo.ATTACKS = {'short sword':[[5],[1,6,3],[19,2]],
               'longbow':[[6],[1,8,3],[20,3]],
               'longbow rapid shot':[[4,4],[1,8,3],[20,3]]}
paulo.SKILLS = {
			  'CLIMB':7,
			  'HIDE':9,
			  'KNOWLEDGE DUNGEONEERING':5,
			  'KNOWLEDGE GEOGRAPHY':5,
			  'KNOWLEDGE NATURE':5,
			  'LISTEN':8,
			  'MOVE SILENTLY':9,
			  'SEARCH':8,
			  'SP0T':10,
			  'SURVIVAL':7
			  }

#Zac
zac = dnd_classes.character()
zac.name = "Zac"
zac.STR = 2
zac.DEX = 2
zac.CON = 0
zac.INT = 2
zac.WIS = 1
zac.CHA = 1
zac.BA = 2
zac.GRA = 4
zac.INITIATIVE = 2
zac.FORT = 3
zac.REF = 6
zac.WILL = 4
zac.AC = {'FULL':17,
          'TOUCH':12,
          'FLAT-FOOTED':14}
zac.ATTACKS = {'katana':[[5],[1,10,2],[19,2]],
               'wakizashi':[[2],[1,6,0],[19,2]]}
zac.SKILLS = {
			  'BALANCE':7,
			  'DIPLOMACY':3,
			  'INTIMIDATE':11,
			  'JUMP':6,
			  'KNOWLEDGE NOBILITY':3,
			  'LISTEN':5,
			  'RIDE':4,
			  'SEARCH':4,
			  'SENSE MOTIVE':7,
			  'SP0T':4,
			  'SWIM':4,
			  'TUMBLE':7
			  }

# Character name dictionary. Used in party class initialization:
character_list = [ali,emily,isaac,jj,josh,paulo,zac]

# Generic skills dictionary, for ease of creation 
"""
			  'APPRAISE':0,
			  'BALANCE':0,
			  'BLUFF':0,
			  'CLIMB':0,
			  'CONCENTRATION':0,
			  'CRAFT':0,
			  'DECIPER SCRIPT':0,
			  'DIPLOMACY':0,
			  'DISABLE DEVICE':0,
			  'DISGUISE':0,
			  'ESCAPE ARTIST':0,
			  'GATHER INFORMATION':0,
			  'HANDLE ANIMAL':0,
			  'HEAL':0,
			  'HIDE':0,
			  'INTIMIDATE':0,
			  'JUMP':0,
			  'KNOWLEDGE':0,
			  'LISTEN':0,
			  'MOVE SILENTLY':0,
			  'OPEN LOCK':0,
			  'PERFORM':0,
			  'PROFESSION':0,
			  'RIDE':0,
			  'SEARCH':0,
			  'SENSE MOTIVE':0,
			  'SLEIGHT OF HAND':0,
			  'SPELLCRAFT':0,
			  'SP0T':0,
			  'SURVIVAL':0,
			  'SWIM':0,
			  'TUMBLE':0,
			  'USE MAGIC DEVICE':0,
			  'USE ROPE':0
			  }
"""


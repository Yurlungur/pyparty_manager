#!/usr/bin/env python

# legacy.py
# Author: Jonah Miller (jonah.miller@colorado.edu)


# legacy.py contains dictionaries for characters to generate instances
# of the character class. In general, this is the way for batch
# generation. However, it usually isn't.


# A map of skills to character attributes. In case someone doesn't
# have a skill. Does not test whether trained or untrained.
# TODO: impliment untrained skill error handling
skill_map = {'APPRAISE':'INT',
             'BALANCE':'DEX',
             'BLUFF':'CHA',
             'CLIMB':'STR',
             'CONCENTRATION':'CON',
             'CRAFT':'INT',
             'DECIPHER SCRIPT':'INT',
             'DIPLOMACY':'CHA',
             'DISABLE DEVICE':'INT',
             'DISGUISE':'CHA',
             'ESCAPE ARTIST':'DEX',
             'FORGERY':'INT',
             'GATHER INFORMATION':'CHA',
             'HANDLE ANIMAL':'CHA',
             'HEAL':'WIS',
             'HIDE':'DEX',
             'INTIMIDATE':'CHA',
             'JUMP':'STR',
             'KNOWLEDGE':'INT',
             'LISTEN':'WIS',
             'MOVE SILENTLY':'DEX',
             'OPEN LOCK':'DEX',
             'PERFORM':'CHA',
             'PROFESSION':'WIS',
             'RIDE':'DEX',
             'SEARCH':'INT',
             'SENSE MOTIVE':'WIS',
             'SLEIGHT OF HAND':'DEX',
             'SPELLCRAFT':'INT',
             'SPOT':'WIS',
             'SURVIVAL':'WIS',
             'SWIM':'STR',
             'TUMBLE':'DEX',
             'USE MAGIC DEVICE':'CHA',
             'USE ROPE':'DEX'}

# Character Sheet Data Structures Keys should be self-explanatory.
# Combat is a little confusing. The key is 'ATTACKS'. The value is
# another dictionary. Each key is an attack, each value is a list. The
# first value of the list is the bonus for each attack, the second
# value is a list with damage ndm+damage_bonus. The last element is a
# list with critical range and modifier.
#  E.g.
# 'ATTACKS':{'scimitar':[[5],[1,6,2],[18,2]]}
isaac = {'NAME':'Isaac',
         'ABILITIES':{'STR':2,
                      'DEX':0,
                      'CON':-1,
                      'INT':2,
                      'WIS':0,
                      'CHA':-1},
         'SAVES':{'FORT':2,
                  'REF':3,
                  'WILL':0},
         'AC':{'FULL':15,
               'TOUCH':10,
               'FLAT-FOOTED':12},
         'BA':2,'GRA':3,'INITIATIVE':0,
         'ATTACKS':{'scimitar':[[5],[1,6,2],[18,2]],
                    'FULL':[[3,3],[1,6,2],[18,2]],
                    'shortbow':[[2],[1,6,2],[20,3]]},
         'SKILLS':{'CLIMB':3,
                   'CRAFT':{'STONEWORKING':4},
                   'HEAL':3,
                   'HIDE':1,
                   'JUMP':3,
                   'KNOWLEDGE':{'DUNGEONEERING':4,
                                'GEOGRAPHY':3,
                                'NATURE':2},
                   'LISTEN':1,
                   'MOVE SILENTLY':2,
                   'PROFESSION':{'CIVIL ENGINEER':3},
                   'RIDE':2,
                   'SEARCH':4,
                   'SPOT':4,
                   'SURVIVAL':5,
                   'SWIM':4,
                   'USE ROPE':2}}

paulo = {'NAME':'Paulo',
         'ABILITIES':{'STR':3,
                      'DEX':4,
                      'CON':0,
                      'INT':2,
                      'WIS':3,
                      'CHA':1},
         'SAVES':{'FORT':3,
                  'REF':7,
                  'WILL':3},
         'AC':{'FULL':16,
               'TOUCH':14,
               'FLAT-FOOTED':12,},               
         'BA':2,'GRA':4,'INITIATIVE':4,
         'ATTACKS':{'Shortsword':[[5],[1,6,3],[19,2]],
                    'FULL':[[4,4],[1,8,3],[20,3]],
                    'longbow':[[6],[1,8,3],[20,3]]},
         'SKILLS':{'CLIMB':7,
                   'HIDE':9,
                   'KNOWLEDGE':{'DUNGEONEERING':5,
                                'GEOGRAPHY':5,
                                'NATURE':5},
                   'LISTEN':8,
                   'MOVE SILENTLY':9,
                   'SEARCH':8,
                   'SPOT':10,
                   'SURVIVAL':7}}

emily = {'NAME':'Ariadne',
         'ABILITIES':{'STR':1,
                      'DEX':2,
                      'CON':1,
                      'INT':0,
                      'WIS':2,
                      'CHA':0},
         'SAVES':{'FORT':4,
                  'REF':5,
                  'WILL':5},
         'AC':{'FULL':14,
               'TOUCH':14,
               'FLAT-FOOTED':12,},               
         'BA':1,'GRA':1,'INITIATIVE':2,
         'ATTACKS':{'sling':[[1],[1,4,0],[20,2]],
                    'FULL':[[-1,-1],[1,6,1],[20,2]],
                    'unarmed':[[1],[1,6,1],[20,2]]},
         'SKILLS':{'BALANCE':2,
                   'CLIMB':2,
                   'CONCENTRATION':2,
                   'DIPLOMACY':2,
                   'ESCAPE ARTIST':2,
                   'HIDE':4,
                   'JUMP':2,
                   'KNOWLEDGE':{'NATURE':2},
                   'LISTEN':4,
                   'MOVE SILENTLY':5,
                   'SENSE MOTIVE':4,
                   'SPOT':3,
                   'SURVIVAL':4}}

# Character index. Lists the characters and their dictionaries as a
# dictionary.
char_hash = {'Isaac':isaac,
             'Paulo':paulo,
             'Emily':emily}


#!/usr/bin/env python

# dnd_classes.py
# Author: Jonah Miller

# The D&D object data structures for python

# Import the basic die roller functions

# GNU License

import dice   # Dice roller
import copy
#import numpy as np

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



# Classes
class weapon:
    """A class that holds information about a D&D weapon."""
    # Constructor
    def __init__(self,bonus,damage,crit_range,crit_multiplier):
        "Makes an instance of the weapon class."
        self.bonus = bonus
        self.damage = damage 
        self.crit_range = crit_range
        self.crit_multiplier = crit_multiplier
    # Make an attack
    def make_attack(self):
        # Some namespace simplifications
        damage = self.damage
        crit_range = self.crit_range
        crit_multiplier = self.crit_multiplier
        bonus = self.bonus

        # Roll to hit
        attack_roll = [dice.roll_1dx(20)+i for i in bonus]
        # Roll damage. Even if you miss, damage is rolled. Be careful!
        attack_damage = [dice.sum_ndm(damage[0], damage[1])+damage[2] for i in bonus]
        # Check for crits and multiply by appropriate values.
        for i in range(len(attack_roll)):
            if attack_roll[i] >= self.crit_range:
                # TODO: make it roll for multiplier
                attack_damage[i] += sum([dice.sum_ndm(damage[0],damage[1])+damage[2] for i in range(self.crit_multiplier-1)])
        
        # Return roll resuts
        return [attack_roll,attack_damage]
                

class character:
    """"A D&D Character. Has a number of attributes.
    By default, a character has empty attributes.
    # A list of abilities a character can have.
    self.abilities = ['STR','DEX','CON','INT','WIS','CHA']
    # Ability modifiers
    STR = 'EMPTY'
    DEX = 'EMPTY'
    CON = 'ENPTY'
    INT = 'EMPTY'
    WIS = 'EMPTY'
    CHA = 'EMPTY'
    # A list of saves a character can have
    saves = ['FORT','REF','WILL']
    FORT = 'EMPTY'
    REF = 'EMPTY'
    WILL = 'EMPTY'
    # Armor class 
    AC = {'FULL':'EMPTY',
               'TOUCH':'EMPTY',
               'FLAT-FOOTED':'EMPTY'}
    BA = 'EMPTY'
    GRA = 'EMPTY'
    INITIATIVE = 'EMPTY'
    # Attacks
    self.ATTACKS = {}
    def get_attacks(self):
        return self.ATTACKS.keys()
    # Skills
    SKILLS = {}"""
    def get_skills(self):
        return self.SKILLS.keys()

    # A function that maps strings to actual attributes
    def map(self,attribute_name):
        attributes = {'STR':self.STR,
                      'DEX':self.DEX,
                      'CON':self.CON,
                      'INT':self.INT,
                      'WIS':self.WIS,
                      'CHA':self.CHA,
                      'FORT':self.FORT,
                      'REF':self.REF,
                      'WILL':self.WILL,
                      'AC':self.AC,
                      'BA':self.BA,
                      'GRA':self.GRA,
                      'INITIATIVE':self.INITIATIVE,
                      'ATTACKS':self.ATTACKS,
                      'SKILLS':self.SKILLS}
        return attributes[attribute_name]

        
    # Roll an attribute
    def roll_att(self,attribute_name):
        """Rolls an attribute for a single character. Works only for
        attributes, not skills! 

        Returns:
        [result,bonus]"""
        attribute = self.map(attribute_name)
        return [dice.roll_1dx(20) + attribute,attribute]
    
    # Roll a skill
    def roll_skill(self,skill_name):
        """Rolls a skill for a single character. Accepts a string.

        Returns:
        [result,bonus]
        """
        # If the skill is something the character has trained in, it's
        # in the dictionary defined by the self.SKILLS attribute. Just
        # use it.
        if skill_name in self.SKILLS.keys():
            skill = self.SKILLS[skill_name]
        # If the character is not trained in the skill, then assume
        # it's the character's ability modifier.
        else:
            skill = self.map(skill_map[skill_name])
        return [dice.roll_1dx(20) + skill, skill]

    # Constructor. Makes an empty class.
    def __init__(self):
        # Empty attributes we need
        self.name = 'unknown'
        self.abilities = ['STR','DEX','CON','INT','WIS','CHA']
        self.saves = ['FORT','REF','WILL']
        self.AC = {}
        self.SKILLS = {}
        self.ATTACKS = {}
        
        # Empty ability modifiers
        self.STR = 0
        self.DEX = 0
        self.CON = 0
        self.INT = 0
        self.WIS = 0
        self.CHA = 0

        # Empty saves
        self.FORT = 0
        self.REF = 0
        self.WILL = 0

        # Empty base attack bonus/initiative
        self.BA = 0
        self.GRA = 0
        self.INITIATIVE = 0
                
    # Constructor. Reads info from a charstats file in characters module.
    def read_from_dict(self,charstats):
        # Empty attributes we need
        self.abilities = ['STR','DEX','CON','INT','WIS','CHA']
        self.saves = ['FORT','REF','WILL']
        self.AC = {}
        self.SKILLS = {}
        self.ATTACKS = {}

        # Ability modifies
        self.name = charstats['NAME']
        self.STR = charstats['ABILITIES']['STR']
        self.DEX = charstats['ABILITIES']['DEX']
        self.CON = charstats['ABILITIES']['CON']
        self.INT = charstats['ABILITIES']['INT']
        self.WIS = charstats['ABILITIES']['WIS']
        self.CHA = charstats['ABILITIES']['CHA']

        # Saves
        self.FORT = charstats['SAVES']['FORT']
        self.REF = charstats['SAVES']['REF']
        self.WILL = charstats['SAVES']['WILL']
        
        # Armor class
        for i in charstats['AC'].keys():
            self.AC[i] = charstats['AC'][i]
            
        # Base attack, grapple, initiative
        self.BA = charstats['BA']
        self.GRA = charstats['GRA']
        self.INITIATIVE = charstats['INITIATIVE']
        
        # Attacks
        for i in charstats['ATTACKS'].keys():
            # Some name simplifications
            a_bonus = charstats['ATTACKS'][i][0]
            a_damage = charstats['ATTACKS'][i][1]
            a_crit_range = charstats['ATTACKS'][i][2][0]
            a_crit_mult = charstats['ATTACKS'][i][2][1]
            # Initialize an attack
            self.ATTACKS[i] = weapon(a_bonus,a_damage,
                                     a_crit_range, a_crit_mult)
        # Skills
        for i in charstats['SKILLS'].keys():
            self.SKILLS[i] = charstats['SKILLS'][i]




class party:
    "The party."
    # Roll an attribute for the entire party. Takes a string as input.
    def roll_att(self,attribute):
        rolls = {}
        for i in self.members:
            charname = i.name
            c_attribute = i.map(attribute)
            rolls[charname] = [dice.roll_1dx(20) + c_attribute,c_attribute]
        return rolls
            
    # Roll a skill for the entire party. Takes a string as input. 
    def roll_skill(self,skill):
        rolls = {}
        for i in self.members:
            charname = i.name
            c_skills = i.SKILLS
            if skill in c_skills.keys():
                c_skill = c_skills[skill]
            else:
                c_skill = i.map(skill_map[skill])
            rolls[charname] = [dice.roll_1dx(20) + c_skill, c_skill]
        return rolls

    # Make the party. Takes a dictionary as input. The keys are
    # character names, the values are stat blocks.
    def __init__(self, character_list):
        self.members = character_list


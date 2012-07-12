#!/usr/bin/env python

# Toplevel aliases for party management
import legacy
import dice
from dnd_classes import *
from characters import *
from party_manager import *

#Character attack aliases
def iatk(attack_name): 
    "Isaac attacks"
    return isaac.ATTACKS[attack_name].make_attack()

def eatk(attack_name):
    "Emily attacks"
    return emily.ATTACKS[attack_name].make_attack()

def patk(attack_name):
    "Paulo attacks"
    return paulo.ATTACKS[attack_name].make_attack()

def aatk(attack_name):
    "Ali attacks"
    return ali.ATTACKS[attack_name].make_attack()

def jatk(attack_name):
    "Josh attacks"
    return josh.ATTACKS[attack_name].make_attack()

def jjatk(attack_name):
    "J.J. attacks"
    return jj.ATTACKS[attack_name].make_attack()

def zatk(attack_name):
    "Zack attacks"
    return zack.ATTACKS[attack_name].make_attack()

#Character roll 

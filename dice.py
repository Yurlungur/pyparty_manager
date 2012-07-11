#!/usr/bin/env python

# dice.py
# Author: Jonah Miller (jonah.miller@colorado.edu)

# Import modules
import random as rand

def roll_1dx(x):
    return rand.randint(1, x)

def roll_ndm(n, m):
    resultlist = []
    for i in range(n):
        resultlist.append(roll_1dx(m))
    print("results...")
    print(resultlist)
    return resultlist

def sum_ndm(n,m):
    resultlist = []
    for i in range(n):
        resultlist.append(roll_1dx(m))
    result = sum(resultlist)
    return result

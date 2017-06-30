#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
	A little program using card1 module. Type ``usage()``.

"""

import sys


import parentheses_checker1 as parentheses_checker
#import parentheses_check2 as parenthses_checker

def usage ():
    print("Veuillez indiquer le fichier pour savoir si il est bien parenthésé.")
    exit (1)
    
if len (sys.argv) != 2:
    usage ()
    
parentheses_checker.well_parentheses(sys.argv[1])

print()

# eof

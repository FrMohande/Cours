#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
	A little program using card1 module. Type ``usage()``.

"""

import sys


import card1 as card

def usage ():
    print ('Usage : {:s} x1'.format(sys.argv[0]))
    print ('with x1 numbers of cards for each player')
    exit (1)
    
if len (sys.argv) != 2:
    usage ()
    
card.jeu_bataille(int(sys.argv[1]))

print()

# eof

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#Outioua Mohand -- Jonathan Soleillet


from stack import *

    
    
def well_parentheses(filename):
    """
    Print which parenthesis is closed or not 

    :param filename: file
    :type filename: file
    :UC: None
    :Example:
	
    >>> well_parentheses("stack.py")
    >>> well_parentheses("bad_stack1.py")
    'Closed parenthese ] at line 41 char 13 don't match the open parenthese ( at line 41 char 9'
    >>> well_parentheses("bad_stack2.py")
    'Parenthese ( at line 80 char 13 has no matching closed parenthese.'
    >>> well_parentheses("bad_stack3.py")
    'Parenthese [ at line 10 char 2 has no matching closed parenthese.'
    >>> well_parentheses("bad_stack4.py")
    'No open parenthese matching parenthese ] at line 76 char 20'
    """
    stream = open(filename,'r')
    ouvrant = create()
    retour = True
    list_line_char = [0,0]
    list_ouvrant = ['(','[','{']
    list_fermant = [')',']','}']
    c = stream.readlines()
    for i,phrase in enumerate(c) :
        list_line_char[0] = i
        ligne = i
        for j,lettre in  enumerate(phrase) :
            list_line_char[1] = j
            phrase = i
            if lettre in list_ouvrant:
                push((lettre,list_line_char[0],list_line_char[1]),ouvrant)
            elif lettre in list_fermant :
                if not is_empty(ouvrant):
                    if list_ouvrant.index(top(ouvrant)[0]) == list_fermant.index(lettre):
                        pop(ouvrant)
                    else :
                        temp = pop(ouvrant)
                        print('Closed parenthese',lettre,'at line ',ligne,' char ', j,' don\'t match the open parenthese ', temp[0],' at line ', temp[1], ' car ', temp[2])
                else:
                    print("No open parenthese matching parenthese ", lettre,' at line ', ligne, 'char ' , j)
    if not is_empty(ouvrant):
        temp = top(ouvrant)
        print("Parenthese ", temp[0],' at line ', temp[1], 'char ' , temp[2], " has no matching closed parenthese.")
    stream.close()

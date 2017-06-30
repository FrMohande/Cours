#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#Outioua Mohand -- Jonathan Soleillet


from stack import *

##Autre méthode
##def well_parentheses(filename):
##    stream = open(filename,'r')
##    ouvrant = create()
##    fermant = create()
##    retour = True
##    list_ouvrant = ['(','[','{']
##    list_fermant = [')',']','}']
##    c = stream.readlines()
##    for phrase in c :
##        for lettre in phrase :
##            if lettre in list_ouvrant:
##                push(lettre,ouvrant)
##                #print(lettre)
##            elif lettre in list_fermant :
##                push(lettre,fermant)
##                #print(lettre)
##    while not is_empty(ouvrant) and  not is_empty(fermant) :
##        temp_ouvert = pop(ouvrant)
##        temp_fermante = pop(fermant)
##        if list_ouvrant.index(temp_ouvert) != list_fermant.index(temp_fermante):
##            retour = False
##    if retour :
##        print('Well parenthesed')
##    else :
##        print('Bad parenthesed')
##    stream.close()


def well_parentheses(filename):
    """
    Print if the file is well parenthesed or not

    :param filename: file
    :type filename: file
    :UC: None
    :Example:

    >>> well_parentheses("stack.py")
    'Well parenthesed'
    >>> well_parentheses("bad_stack1.py")
    'Bad parenthesed'
    >>> well_parentheses("bad_stack2.py")
    'Bad parenthesed'
    >>> well_parentheses("bad_stack3.py")
    'Bad parenthesed'
    >>> well_parentheses("bad_stack4.py")
    'Bad parenthesed'
    """
    stream = open(filename,'r')
    ouvrant = create()
    retour = True
    list_ouvrant = ['(','[','{']
    list_fermant = [')',']','}']
    c = stream.readlines()
    for i,phrase in enumerate(c) :
        for j,lettre in  enumerate(phrase) :
            if lettre in list_ouvrant:
                push(lettre,ouvrant)
            elif lettre in list_fermant :
                if not is_empty(ouvrant):
                    if list_ouvrant.index(top(ouvrant)) == list_fermant.index(lettre):
                        pop(ouvrant)
                    else :
                        temp = pop(ouvrant)
                        retour = False
                else:
                    retour = False
    if not is_empty(ouvrant):
        temp = top(ouvrant)
        retour = False
    if retour :
        print('Well parenthesed')
    else :
        print('Bad parenthesed')
    stream.close()

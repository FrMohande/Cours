#!/usr/bin/python3
# -*- coding: utf-8 -*-
#Outioua Mohand -- Jonathan Soleillet


"""
:mod:`card1` module : version 1 of a (simple) module for card 

:author: `Outioua Mohand et Jonathan Soleillet`

:date: 2015, september

Cards are defined by a value and a color. Possible values and colors are listed in card.values and card.colors. 

"""
from random import *
import builtins


colors = ['heart','clover','pike','tile']
values = ['7','8','9','10','V','Q','K','A']

def create(value,color):
    """
    creates a card with value and color
    
    :param value: value of the card
    :type value: element of card.value
    :param color: color of the card
    :type color: element of card.color
    :return: a new card with value and color
    :rtype: card
    :UC: None
    """
    assert(color in colors),"the color have to be heart,clover,pike or tile"
    assert(value in values),"the value have to be 7,8,9,10,V,Q,K or A"
    card = {'color':color,'value':value}
    return card

def randomcard():
    """
    create a cards whose value and color are randomly chosen
    
    :return: a randomly chosen card
    :rtype: card
    """
    card = {'color':choice(colors),'value':choice(values)}
    return card


def color(card):
    """
    returns the color of the card

    :param card: the card
    :type card:
    :param type: card
    :type type:
    :return: the color of the card
    :UC: None
    :Example:

    >>> c = create('A','heart')
    >>> color(c)
    'heart'
    
    """
    return card['color']
def value(card):
    """
    returns of the value of the card

    :param card: the card
    :type card: card
    :return: the value of the card
    :UC: None
    :Example:

    >>> c = create('A',heart')
    >>> value(c)
    'A'
    """
    return card['value']

def compare_value(card1,card2):
    """
    compares cards values, returns :
      * a positive number if card1’s value is greater than card2’s
      * a negative number if card1’s value is lower than card2’s
      * 0 if card1’s value is the same greater than card2’s
    :param card1: the first card
    :type card1: card
    :param card2: the second card
    :type card2: card
    :return:
      * a positive number if card1’s value is greater than card2’s
      * a negative number if card1’s value is lower than card2’s
      * 0 if card1’s value is the same greater than card2’s
    :rtype: int
    :UC: None
    :Example:

    >>> c1 = create('Ace','heart')
    >>> c2 = create('King','heart')
    >>> c3 = create('Ace','spade')
    >>> compare_value(c1,c2) > 0
    True
    >>> compare_value(c2,c1) < 0
    True
    >>> compare_value(c1,c3) == 0
    True
    """
    index1 = values.index(card1['value'])
    index2 = values.index(card2['value'])
    return index1-index2

def compare_color(card1,card2):
    """
    compares cars colors,return :
        * a positive number if card1’s color is greater than card2’s
        * a negative number if card1’s color is lower than card2’s
        * 0 if card1’s color is the same greater than card2’s
      
    :param card1: the first card
    :type card1: card
    :param card2: the second card
    :type card2: card
    :return:
      * a positive number if card1's color is greather than card2's
      * a negative number if card1's color is lower than card2's
      * 0 if card1's color is the same greather than card2's
    :rtype: int
    :UC: None
    """
    index1 = colors.index(card1['color'])
    index2 = colors.index(card2['color'])
    return index1-index2

def compare(card1,card2):
    """
    compares cards, first it compares cards values and if equal cards colors returns :
      * a positive number if card1 is greater than card2
      * a negative number if card1 is lower than card2
      * 0 if card1 is the same greater than card2
    :param card1: the first card
    :type card1: card
    :param card2: the second card
    :type card2: card
    :return:
      * a positive number if card1 is greater than card2
      * a negative number if card1 is lower than card2
      * 0 if card1 is the same greater than card2
    :rtype: int
    :UC: None
    :Example:

    >>> c1 = create('Ace','heart')
    >>> c2 = create('King','heart')
    >>> c3 = create('Ace','spade')
    >>> c1bis = create('Ace','heart')
    >>> compare(c1,c2) > 0
    True
    >>> compare(c2,c1) < 0
    True
    >>> compare(c1,c3) < 0
    True
    >>> compare(c1,c1bis) == 0
    True
    """
    if compare_value(card1,card2) == 0 :
        return compare_color(card1,card2)
    else :
        return compare_value(card1,card2)

def __to_string(card):
    """
    returns a string representation of the card

    :param card: the card
    :type card: card
    :return:  a string representation of the card
    :rtype: string
    :UC: None
    :Example:

    >>> c = create('Ace','heart')
    >>> to_string(c)
    'Ace of heart'
    """
    return value(card) + ' of ' + color(card)


def print(card,end='\n'):
    """
    print the card

    :param card: the card
    :type card: card
    :param end: [optional] separator (default is \\\n)
    :type end: string
    :UC: None
    """
    builtins.print (__to_string(card), end=end)


def create_card_game():
    """
    create the game card

    :return: a list who contains the cards
    :rtype: list
    :UC: None
    """
    jeu_carte = list()
    for i in range(len(values)):
        for j in range(len(colors)):
            jeu_carte.append(create(values[i],colors[j]))
    return jeu_carte
def distribution(nombre_carte,jeu_carte,joueurs):
    """
    distribute the card for each player

    :param jeu_carte: list who contains the cards
    :type jeu_carte: list
    :param joueurs: the players
    :type joueurs: dictionary
    :UC: None
    """
    cpt = 0 
    while len(jeu_carte) != 0 and cpt < nombre_carte: 
        joueurs['j1'].append(jeu_carte[0])
        jeu_carte.remove(jeu_carte[0])
        cpt = cpt + 1
        if cpt < nombre_carte : 
            joueurs['j2'].append(jeu_carte[0])
            jeu_carte.remove(jeu_carte[0])
            cpt = cpt + 1
def my_reverse(l,l2):
    """
    renverse the list

    :param l1: list
    :type l1: list
    :param l2: list
    :type l2: list
    :UC: None
    :Example:

    >>> my_reverse([0,1,2,3],[])
    [3,2,1,0]
    """
    for i in range(len(l)-1,-1,-1):
        l2.append(l[i])
    return len(l2)


def jeu_bataille(n):
    """
    plays to the War (card game)

    :param n: numbers of cards for each player
    :type n: int
    :UC: numbers of cards
    """
    assert n in range(len(colors) * len(values)+1),"the number has to be less or equal to %d" %(len(colors) * len(values))
    table = list()
    joueurs = {'j1':[],'j2':[]}
    jeu_carte = create_card_game()
    #shuffle permet de mélanger aléatoirement la liste
    shuffle(jeu_carte)
    distribution(n,jeu_carte,joueurs)
    fin = ''
    bataille = False
    cpt = 0
    ##builtins.print(len(joueurs['j1']),len(joueurs['j2']))
    while len(joueurs['j1']) !=0 and len(joueurs['j2']) != 0:
        if bataille:
            pref = '\t'
        else :
            pref = ''
        builtins.print(pref,'joueur 1 joue : ',end='') 
        print(joueurs['j1'][0])
        builtins.print(pref,'joueur 2 joue : ',end='')
        print(joueurs['j2'][0])
        
        table.append(joueurs['j1'][0])
        table.append(joueurs['j2'][0])
        joueurs['j1'].remove(joueurs['j1'][0])
        joueurs['j2'].remove(joueurs['j2'][0])
        ##builtins.print(len(joueurs['j1']),len(joueurs['j2']))
        if(compare_value(table[len(table)-2],table[len(table)-1]) > 0):
            #joueur 1 gagne la manche
            my_reverse(table,joueurs['j1'])
            table.clear()
            bataille = False
            builtins.print('joueurs 1 gagne la manche')
        elif(compare_value(table[len(table)-2],table[len(table)-1]) < 0):
            #joueur 2 gagne la manche
             my_reverse(table,joueurs['j2'])
             table.clear()
             bataille = False
             builtins.print('joueurs 2 gagne la manche')
        else:
            #bataille
            builtins.print("bataille")
            bataille = True
        if not bataille :
            builtins.print()	
    ##builtins.print(len(joueurs['j1']),len(joueurs['j2']))
    if  len(joueurs['j1']) !=0 and len(joueurs['j2']) ==0  :
        builtins.print("joueur 1 gagne")
        builtins.print("joueur 2 perd")
    elif len(joueurs['j1']) ==0 and len(joueurs['j2']) !=0:
        builtins.print("joueur 2 gagne le jeu")
        builtins.print("joueur 1 perd le jeu")
    else:
        builtins.print("Il y a une équalité entre les deux joueurs")
        
    

        

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#Outioua Mohand
#Jeudi 15 octobre - TP 7 : Dessiner avec la tortue (episode 2)


'''Toutes les questions et fonctions ont été traités et sont fonctionnelles.'''

from turtle import *
l_symboles = ['+','-','F']
speed(0)

#Dessiner un ordre

#1
def dessiner(longueur,degree,liste):
    for c in liste:
        assert(c in l_symboles),"La séquence doit uniquement contenir les symboles + - F"
        if c == 'F':
            forward(longueur)
        if c == '-':
            right(degree)
        if c == '+':
            left(degree)
#2

#dessiner(100,60,['F', '-', '-', 'F', '-', '-', 'F', '-', '-'])
#dessiner(100,90,['F','+','F','+','F','+','F'])


def hexagone_regulier(n):
    l = ['F','+'] * n
    dessiner(100,360/n,l)
#hexagone_regulier(4)



#Dériver un ordre


#1
            
def derive(so,r):
    l = list()
    for c in so:
        if c == 'F':
            for cr in r:
                l.append(cr)
        else:
            l.append(c)
    return l
#print(derive(['F', '+', 'F'],['F', '-', 'F']))

#2
def derive_n(so,r,n):
    cpt = n
    l = derive(so,r)
    if n == 0:
        return so
    if n == 1:
        return l
    while cpt > 1:
        l = derive(l,r)
        cpt = cpt - 1
    return l
#print(derive_n(['F', '+', 'F'],['F', '-', 'F'],2))


#Fractales





def fractales(n,so,r,degree):
    l = list()
    l = derive_n(so,r,n)
    long = 3**(5-n)
    dessiner( long ,degree,l)
    
#1

def Flocon_de_Koch():
    so = ['F', '-', '-', 'F', '-', '-', 'F', '-', '-']
    r = ['F', '+', 'F', '-', '-', 'F', '+', 'F']
    fractales(5,so,r,60)
#Flocon_de_Koch()
    
#2
def Courbe_quadratique():
    so = ['F']
    r =  ['F', '+', 'F', '-', 'F', '-', 'F', '+', 'F']
    fractales(5,so,r,90)
#Courbe_quadratique()
    
#3
def courbe_de_Kochso(n):
    so = ['F']
    r = ['F', '+', 'F', '-', 'F', '-', 'F', '+', 'F']
    fractales(n,so,r,90)

#courbe_de_Kochso(3)


    
def terdragon(n):
    so = ['F']
    r = ['F','+','F','-','F']
    fractales(n,so,r,120)
#terdragon(5)

def derive_3(l1, l2, l3):
    lRes = list()
    for c in l1:
        if c == 'L':
            lRes = lRes + l2
        elif c == 'R':
            lRes = lRes + l3
        else:
            lRes.append(c)
    return lRes

def derive_n_3(l1, l2, l3, n):
    for i in range(n):
        l1 = derive_3(l1, l2, l3)
    return l1

def dragon_curve(n):
    lDragon = derive_n_3(['F','L'],['L', '+', 'R', 'F', '+'],['-', 'F', 'L', '-', 'R'],n)

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#Outioua Mohand
#Vendredi 2 octobre - TP5 : Dessiner avec la tortue


'''Toutes les fonctions ont été réalisées mise à part le billard problème dans ma 2ème boucle '''


#Exemple :: Dessiner une étoile
from turtle import *
from math import *
from random import *

speed(0)


#module turtle

#2
'''forward(100) permet de tracer une ligne vers la droite'''

#3
'''Si on ajoute un forward(100) celà continue de tracer le trait vers la droite'''

#4
''' forward() avec une valeur négatif celà trace le trait vers la gauche'''

#5

#left(radians(20))

''' D'après help(left) et help(right) les valeurs sont par défaut en degrée
on peux convertir via radians() ou degree()'''


#6

#goto(5,105)
'''goto(x,y) permet de tracer un trait en fonction de la position absolue'''
'''goto trace un trait qui peux être non droit'''


#7 


#Dessiner avec des carrés

'''penup lève le crayon'''
'''pendown je baisse le crayon'''

#1

def carre(l):
    for i in range(0,4):
        forward(l)
        left(90)
#carre(10)
    
#2
def carreAligne(l):
    for j in range(0,10):
        for i in range(0,4):
            forward(l)
            left(90)
        penup()
        forward(l + 5 )
        pendown()
        
#carreAligne(10)

#3

#l * 10 longueur total du carré et 5 * 10 = décalage entre les carrés


def carrebis(l):
    for i in range(0,10):
        x,y = position()
        carreAligne(l)
        penup()
        forward(-(l*10+10*5))
        goto(x,y-15)
        pendown()
#carrebis(10)



#4


def carreEmboite(l):
    for i in range(0,50):
        carre(l*i)

#carreEmboite(10)


def carres_tournant(n,l):
    for i in range(0,n):
        right(360//n)
        carre(l)
#carres_tournant(7,100)


#Dessiner des polygones réguliers

#A - Cas des polygones convexes

#1

'''L'angle est 360° divisé par le nombre de coté'''
#2
def polygone_reg_convexe(n,l):
    for i in range(0,n):
            forward(l)
            left(360/n)
#3
            
#polygone_reg_convexe(4,100)
#polygone_reg_convexe(5,100)
#polygone_reg_convexe(6,100)
#polygone_reg_convexe(7,100)


#B - Cas des polygones étoilés

#1
def polygone_etoile(n,l,k):
    angle = 360/n
    for i in range(0,n):
        forward(l*k)
        left(angle*k)
#2

#polygone_etoile(5,100,3)
#polygone_etoile(7,100,3)
#polygone_etoile(8,100,3)
#polygone_etoile(11,100,5)



#3
'''oui,  polygone_etoile(5,100,1) '''


#Mouvement brownien




#abs => valeur absolue
def abs(n):
    return (n,-n)[n<0]

def tortue_sortie(n,l):
    if abs(n) > l/2:
        return True
    else:
        return False
    
def move_brownien(l):
    x,y = position()
    penup()
    goto(-200,-200)
    pendown()
    pencolor('blue')
    carre(l)
    penup()
    goto(0,0)
    pendown()
    pencolor('red')
    while( not(tortue_sortie(x,l)) and not(tortue_sortie(y,l))):
        x,y = position()
        pas = randint(1,10)
        degree = randint(0,359)
        left(degree)
        forward(pas)
        #print("x:  ",x,"  y:   ",y)
        
#move_brownien(400) 

#Billard

def rectangle(long,larg):
    goto(0,0)
    color("red", "green")
    begin_fill()
    forward(long)
    left(90)
    forward(larg)
    left(90)
    forward(long)
    left(90)
    forward(larg)
    end_fill()
    penup()
    goto(long/2,larg/2)
    pendown()
def billard_sortie(n,l):
    ''' True en dehors du rectancle; False dans le rectangle'''
    if n < 0 or n > l:
        return True
    else:
        return False

def parcours_trajectoire(long,larg,posX,posY,degree,rebonds):
    n = 1
    i = 1
    cpt = 0 
    x,y= 0,0
    rectangle(long,larg)
    goto(posX,posY)
    left(degree)
    while n <= rebonds:
        while(not(billard_sortie(x,long)) and not(billard_sortie(y,larg))):
            x,y = position()
            forward(-i)
            cpt = cpt + 1
            print(n,cpt)
        goto(floor(x),floor(y))
        print(n,cpt)
        cpt= 0
        setheading(90+ heading())
        n = n + 1
#parcours_trajectoire(400,300,0,0,12,30)


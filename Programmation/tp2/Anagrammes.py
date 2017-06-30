#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#Outioua Mohand

#Quelques méthodes sur les listes et chaînes

'''toutes les fonctions et questions ont été traités cependant il y a un problème dans
mon dictionnaire ANAGRAMMES contient plus de mots ce que la consigne demande'''


#Méthode split

#1

s = "la méthode split est parfois bien utile"
#a
s.split (' ')
'''['la', 'méthode', 'split', 'est', 'parfois', 'bien', 'utile']'''
#b
s.split ('e')
'''['la méthod', ' split ', 'st parfois bi', 'n util', '']'''

#c
s.split ('é')
'''['la m', 'thode split est parfois bien utile']'''

#d
s.split()
'''['la', 'méthode', 'split', 'est', 'parfois', 'bien', 'utile']'''
#e
#s.split ('')
'''ValueError: empty separator'''
#f
s.split ('split')
'''['la méthode ', ' est parfois bien utile']'''



#2

'''La fonction split permet de séparer la chaine en paramètre de la fonction et de me mettre dans un tableau la
nouvelle chaine'''

#3

''' Non la méthode ne modifie pas la chaine à laquelle elle s'applique'''


#Méthode join


l = s.split()

#a
"".join (l)
''''laméthodesplitestparfoisbienutile'''

#b
" ".join (l)
''''la méthode split est parfois bien utile'''

#c
";".join (l)
'''la;méthode;split;est;parfois;bien;utile'''

#d
" tralala ".join (l)
'''la tralala méthode tralala split tralala est tralala parfois tralala bien tralala utile'''

#e

#print ("\n".join (l))

'''
la
méthode
split
est
parfois
bien
utile'''

#f
"".join(s)
'''la méthode split est parfois bien utile'''
#g
"!".join (s)
''' 'l!a! !m!é!t!h!o!d!e! !s!p!l!i!t! !e!s!t! !p!a!r!f!o!i!s! !b!i!e!n! !u!t!i!l!e' '''
#h

#"".join ()
'''TypeError: join() takes exactly one argument (0 given)'''

#i
"".join ([])
''' renvoie ''  '''




#2

''' La fonction join permet à la chaine de caractère en paramètre le caractère appellant cette fonction '''


#3

''' Non la méthode ne modifie pas la chaine à laquelle elle s'applique'''


#4
def join(caract,liste):
    s = ''
    for caract_liste in liste:
        s = s + caract_liste + caract 
    return s
join ('.', ['raymond', 'calbuth', 'ronchin', 'fr'])






#Méthode sort



#1

#a

l = list ('timoleon')
l.sort()
'''['e', 'i', 'l', 'm', 'n', 'o', 'o', 't']'''

#b

s = "Je n'ai jamais joué de flûte."
l = list (s)
'''' ', ' ', ' ', ' ', ' ', "'", '.', 'J', 'a', 'a', 'a', 'd', 'e', 'e', 'e', 'f', 'i', 'i', 'j', 'j', 'l', 'm', 'n', 'o', 's', 't', 'u', 'é', 'û']'''
''' l'ordre est l'espace,aspotrophe, le point, les majuscule puis les lettre minuscule '''

#c
l = ['a', 1]
''' le sort provoque une erreur car trier des int et des str'''


#Une fonction sort pour les chaînes


def sort(s):
    new_chaine = ''
    l = list(s)
    l.sort()
    for c in l:
        new_chaine = new_chaine + c
    return new_chaine

#print(sort('timoleon'))



#Anagrammes

#1

'''sont_anagrammes avec utilisation du sort() '''

def sont_anagrammes_sort(c1,c2):
    temp,temp2 =  '',''
    if len(c1) == len(c2):
        temp = sort(c1)
        temp2 = sort(c2)
        for i in range(0,len(c1)):
            if temp[i] != temp2[i]:
                return False
        return True
    return False

#print(sont_anagrammes_sort('organe','onagre'))

#2

'''sont_anagrammes avec utilisation d'un dictionnaire '''

def sont_anagrammes_dict(c1,c2):
    d = dict()
    for l1 in c1:
        if l1 in d[l1]:
            d[l1] = d[l1] + 1
        else:
            d[l1] = 1
    for l2 in c2:
        if l2 in d[l1]:
            d[l1] = d[l1] - 1
            if d[l1] == 0:
                return False
        return False
    return True
#3

'''sont_anagrammes avec utilisation d'une liste '''

def sont_anagrammes_liste(c1,c2):
    l = list(c1)
    for i in range(0,len(l)):
        if l[i].count == 0:
            return False
    return True

#print(sont_anagrammes_sort('organe','onagre'))


#Casse et accentuation

''' é è ê ë à û ü ù'''

#1
EQUIV_NON_ACCENTUE = {'é':'e','è':'e','ê':'e','ë':'e','à':'a','û':'u','ü':'u'
                      ,'ù':'u'}

#2


def bas_casse_sans_accent(c):
    new_chaine = ''
    for i in range(0,len(c)):
        ''' Dans le cas d'un accent en majuscule'''
        temp = c[i].lower()
        if temp in EQUIV_NON_ACCENTUE:
            temp = EQUIV_NON_ACCENTUE[temp]
        new_chaine = new_chaine + temp
    return new_chaine
        
#print(bas_casse_sans_accent('Orange'))



#3

def sont_anagrammes(c1,c2):
    return sont_anagrammes_sort(bas_casse_sans_accent(c1),
                                bas_casse_sans_accent(c2))
#print(sont_anagrammes('orangé', 'ORGANE'))





#Recherche d’anagramme



from lexique import *

#3

#print(len(LEXIQUE))
''' ce lexique contient 139719 mots'''

#4

#print(len(set(LEXIQUE)))
''' ce lexique ne contient aucun  mot unique donc  139719 mots' '''


#Anagrammes d’un mot : première méthode

def anagrammes(c):
    l = list()
    for i in range(0,len(LEXIQUE)):
        if(sont_anagrammes(LEXIQUE[i],c)):
                l.append(LEXIQUE[i])
    return l


#print(anagrammes('Orange'))
#print(anagrammes ('Calbuth'))





#Anagrammes d’un mot : seconde méthode

#Notes on peux utiliser "for k in sorted(dictionnaire):"

'''Problème dans mon dictionnaireo il y 'a 119502 éléménts au lieu des 118625 demandés '''

def cle(c):
    return sort(bas_casse_sans_accent(c))


ANAGRAMMES = dict()
def construire_dico():    
    for i in range(0,len(LEXIQUE)):
        cle_d = cle(LEXIQUE[i])
        mot = LEXIQUE[i]
        if cle_d in ANAGRAMMES:
            ANAGRAMMES[cle_d] = ANAGRAMMES[cle_d] + [mot]
        else:
            ANAGRAMMES[cle_d] = [mot]
construire_dico()

def anagrammes_seconde(c):
    return ANAGRAMMES[cle(c)]


#print(anagrammes_seconde('Orange'))
#print(anagrammes ('Calbuth'))



#Comparaison des deux méthodes


def imprime_anagrames_v1():
    for i in range(0,30):
        print(anagrammes(LEXIQUE[i]))

def imprime_anagrames_v2():
    for i in range(0,30):
        print(LEXIQUE[i],i,anagrammes_seconde(LEXIQUE[i]))
        
#imprime_anagrames_v1()
#print('Imprimer v2')
#print()
#print()
#imprime_anagrames_v2()

'''On constates que le parcours est beaucoup plus long que la recherche dans le dictionnaire'''


#Phrases d’anagrammes

def suivante(liste_actu,list_Indmax):
    '''Fonction universel permettant de faire varier les indices d'une liste
    '''
    for j in range(len(liste_actu)-1,-1,-1):
        if (liste_actu[j] < list_Indmax[j] ):
            liste_actu[j] += 1
            return True
        else :
            liste_actu[j] = 0
    return False

def anagrammes_phrase(phrase):
    mots = phrase.split(' ')
    liste_ana = []
    indice_max = []
    liste_phrase = []
    indice_actuel = []
    phrase = ''
    for c in mots:
        liste_ana.append(anagrammes(c))
    
    for liste in liste_ana:
        indice_max.append(len(liste)-1)
        indice_actuel.append(0)

    while(suivante(indice_actuel,indice_max)):
        for indice,indice2 in enumerate(indice_actuel):
            phrase +=  liste_ana[indice][indice2] +" "
        liste_phrase.append(phrase)
        phrase =""
        print(indice_actuel)
    return liste_phrase



#Sauvegarde et récupération

def creer_fichier():
    sortie = open("anagrammes.txt","w",encoding="utf8")
    l = list()
    for k in ANAGRAMMES:
        sortie.write(k+":")
        sortie.write(":".join(ANAGRAMMES[k]))
        sortie.write("\n")
    sortie.close()
    
        
#creer_fichier()


#2

''' La taille de ce fichier est de 2841502 octets'''


#3

def creer_dicto():
    d = dict()
    l = list()
    f = open("anagrammes.txt","r",encoding="utf8")
    #replaces("\n",'') permets de supprimer les \n lors de la lecture 
    ligne = f.readline().replace("\n",'')
    while ligne != '':
        l = ligne.split(":")
        d[l[0]] = l[1:]
        ligne = f.readline()
    f.close()
    return d

#creer_dicto()


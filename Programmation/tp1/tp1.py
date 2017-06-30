from datetime import *


c = 20
f = 9 / 5 * c + 32

#test1 
print(f) 

f2 = 75
c2 = 5 / 9 * (f2-32)

#test2
print(c2) 

def celcius_en_fahrenheit(c):
    return 9 / 5 * c + 32
def fahrenheit_en_celsius(f):
    return 5 / 9 * (f-32)

#test3
print(celcius_en_fahrenheit(c))
print(fahrenheit_en_celsius(f2))
print()

ref_an = 1900
ref_mois = 1
ref_jour = 1

nbre_sec_jour = 3600 *24
nbre_sec_an = nbre_sec_jour * 365.2425
nbre_sec_mois = nbre_sec_an / 12

anniversaire_an = 1993
anniversaire_mois = 12
anniversaire_jour = 14

seconde_anniversaire = ((anniversaire_an * nbre_sec_an) + (anniversaire_mois * nbre_sec_mois) + (anniversaire_jour * nbre_sec_jour))- (( ref_an * nbre_sec_an ) + ( nbre_sec_mois * ref_mois) + ( ref_jour * nbre_sec_jour)) 

#test
print("age en seconde",seconde_anniversaire)

def nbre_sec_depuis_1900(an,mois,jour):
    nbre_sec_date = ((an * nbre_sec_an) + (mois * nbre_sec_mois) + (jour * nbre_sec_jour))
    nbre_sec_ref = (( ref_an * nbre_sec_an ) + ( nbre_sec_mois * ref_mois) + ( ref_jour * nbre_sec_jour))  
    return nbre_sec_date - nbre_sec_ref
#test
print(nbre_sec_depuis_1900(1993,12,14))
print()


def age_en_secondes(date):
    nbre_sec_date = ((date.day * nbre_sec_jour) + (date.month * nbre_sec_mois) + (date.year * nbre_sec_an))
    nbre_sec_ref = (( ref_an * nbre_sec_an ) + ( nbre_sec_mois * ref_mois) + ( ref_jour * nbre_sec_jour))
    return nbre_sec_date - nbre_sec_ref

#test
print(age_en_secondes(date.today()))
print()


'''------------------------ ------------ ------------ ------------ ------------  '''

from math import log
from math import floor

''' ln '''
def log_base(a,b):
    return log(a) / log(b)

def taille(n):
    return floor(1 + log_base(n,10))

#test
print(taille(500))
print(taille(2**100))
print()

''' on peut pas faire un log négatif '''


def afficher_debut(x):
    a0 = x - floor(x)
    a1 = 1 / (a0 - floor(a0))
    a2= 1 / ( a1 - floor(a1))
    print(a0,a1,a2)


print(afficher_debut(3.14159))       
    









    


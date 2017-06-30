#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
:mod:`competitor` module

:author: `FIL - IEEA - Univ. Lille1.fr <http://portail.fil.univ-lille1.fr>`_

:date: October, 2015

Module for competitor representation.
A competitor

"""
import list1 as list1
from Time import *
def create (first_name, last_name, sex, num):
    """
    
    :param first_name: first name of a competitor
    :type name: string
    :param last_name: last name of a competitor
    :type name: string
    :param sex: sex of a competitor 'M' or 'F'
    :type name: string
    :param num: bib number of the competitor
    :type num: int
    :return: a new record for this competitor
    :rtype: competitor
    :UC: num > 0 and sex in 'MF'
    """
    assert type (num) == type (0) and num > 0
    assert sex in 'MF'
    return {
        'first_name' : first_name,
        'last_name' : last_name,
        'sex' : sex,
        'num' : num,
        'performance' : None
    }

def get_firstname (comp):
    """
    
    :param comp:
    :type comp: competitor
    :return: first name of competitor comp
    :rtype: str
    :UC: none
    """
    return comp['first_name']

def get_lastname (comp):
    """
    
    :param comp:
    :type comp: competitor
    :return: last name of competitor comp
    :rtype: str
    :UC: none
    """
    return comp['last_name']

def get_bibnum (comp):
    """

    :param comp:
    :type comp: competitor
    :return: bib number of competitor comp
    :rtype: str
    :UC: none

    """
    return comp['num']

def get_performance (comp):
    """

    :param comp:
    :type comp: competitor
    :return: performance of competitor comp
    :rtype: time
    :UC: none
    """
    return comp['performance']


def get_sex (comp):
    """

    :param comp:
    :type comp: competitor
    :return: sex of competitor comp
    :rtype: time
    :UC: none
    """
    return comp['sex']

def set_perf (comp, d):
    """

    :param comp: competitor to be modified
    :type comp: competitor
    :param d: performance of competitor comp
    :type d: time
    :return: None
    :Side effect: performance of competitor comp is modified with value d
    :UC: none
    """
    comp['performance'] = d
    
def read_competitors(filename):
    assert(".csv" in filename),'Le fichier doit être un fichier csv !'
    clef = list1.empty_list()
    d = {}
    cle = []
    stream = open(filename,"r")
    phrase = stream.readline()
    phrase = stream.readline()
    cpt = 1
    while phrase != '' :
        cle = phrase.split(';')
        d = create (cle[0], cle[1], cle[2], cpt)
        if list1.is_empty(clef) :
            clef = list1.cons(d,clef)
        else :
            clef = list1.cons(d,clef)
        phrase = stream.readline()
        cpt = cpt + 1
    clef = list1.reverse(clef)
    return clef
def print_results(l_competitors):
    print("Prénom",end="\t")
    print("Nom",end="\t")
    print("Sexe",end="\t")
    print("Num.",end="\t")
    print("Performance")
    l_temp = l_competitors
    while not list1.is_empty(l_temp):
        l_tete = list1.head(l_temp)
        performance = ()
        if len(get_firstname(l_tete)) <= 7 :
            print(get_firstname(l_tete),end="\t")
            print(get_lastname(l_tete),end="\t")
            print(get_sex(l_tete),end="\t")
            print(get_bibnum(l_tete),end="\t")
        else :
            print(get_firstname(l_tete),end=" ") 
            print(get_lastname(l_tete),end=" ")
            print(get_sex(l_tete),end="\t")
            print(get_bibnum(l_tete),end=" ")
        if get_performance(l_tete) == None :
            print()
        else :
            performance = get_performance(l_tete)
            if len(str(get_hours(performance))) == 1 :
                print("0" + str(get_hours(performance)),end=":")
            elif len(str(get_hours(performance))) == 2 :
                print(str(get_hours(performance)),end=":")
            print(get_minutes(performance),end=":")
            print(get_secondes(performance))

        l_temp = list1.tail(l_temp)

def save_results(l_competitors,filename):
    stream = open(filename + ".csv","w+")
    l_temp = l_competitors
    stream.write("Prénom;Nom;Sexe;Num_dossard;Performance\n")
    while not list1.is_empty(l_temp) :
        l_tete = list1.head(l_temp)
        stream.write(str(get_firstname(l_tete)) + ";")
        stream.write(str(get_lastname(l_tete)) + ";")
        stream.write(str(get_sex(l_tete)) + ";")
        stream.write(str(get_bibnum(l_tete)) + ";")
        if get_performance(l_tete) == None:
            stream.write("\n")
        else :
            performance = get_performance(l_tete)
            if len(str(get_hours(performance))) == 1 :
                stream.write("0" + str(get_hours(performance)) +  ":")
            elif len(str(get_hours(performance))) == 2 :
                stream.write(str(get_hours(performance)) +  ":")
            stream.write(str(get_minutes(performance)) + ":")
            stream.write(str(get_secondes(performance)) + "\n")
        l_temp = list1.tail(l_temp)
    stream.close() 
        
        
    
    
    
if __name__ == '__main__':
    l_competitors = read_competitors("small_inscrits.csv")
    l_performance = read_performances("small_performances.csv")
    set_performances(l_competitors,l_performance)
    print_results(l_competitors)
    save_results(l_competitors,"small_race_result")



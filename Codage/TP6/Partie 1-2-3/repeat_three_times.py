#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#Outioua Mohand -- Jonathan Soleillet
#25 novembre 2015
#TP : Simulation d’un canal bruité, et codage correcteur d’erreur - Codage par répétition


#8

def encode(byte):
    assert(0<=byte<=255),"il faut que votre byte soit compris entre 0 et 255"
    return [byte,byte,byte]

def majority(bytes_read):
    #table de vérité + tableau de karnaugh
    assert(len(bytes_read)==3),"la chaine de byte doit être de taille 3."
    return (bytes_read[1]&bytes_read[2]) | (bytes_read[0] & bytes_read[2]) | (bytes_read[0] & bytes_read[1])
    
def  binary_weight(w):
    cmp = 0
    while(w>=1):
        a = w %2

        if a == 1 :
            cmp = cmp +1 
        w = w // 2
    return cmp

def nb_errors(bytes_read):
    #distance d'hamming
    #temp = w' 
    assert(len(bytes_read) == 3),"la chaine de byte doit être de taille 3."
    temp = majority(bytes_read)
    retour = binary_weight(temp^bytes_read[0]) + binary_weight(temp^bytes_read[1]) + binary_weight(temp^bytes_read[2])

    return retour


def decode(bytes_read):
    assert(len(bytes_read) == 3),"la chaine de byte doit être de taille 3."
    majoritys = majority(bytes_read)
    nb_error = nb_errors(bytes_read)
    return (majoritys,nb_error,nb_error)

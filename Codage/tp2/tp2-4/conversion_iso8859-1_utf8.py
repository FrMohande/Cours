#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#Outioua Mohand -- Jonathan Soleillet
#30 Septembre 2015

#Notes

''' iconv permet de convertir un fichier d'un codage dans un autre'''
#20
#1
'''iconv --from-code ISO-8859-1 --to-code UTF-8 --output utf8.txt cigale-ISO-8859-1.txt
Permet de convertir de ISO-8859-1 en UTF-8'''
#2
'''iconv --from-code UTF-8 --to-code ISO-8859-1 --output ISO-8859-1.txt cigale-UTF-8.txt
Permet de convertir de UTF-8 en ISO-8859-1'''

''' la commande file permet de savoir le type de fichier '''

#IV.2

#22


''' n = caractère à convertir en binaire
Pour extraire l'octet de poids fort il suffit de faire : (n >>6) or 192
Pour extraire l'octet de poids faible il suffit de faire :  (n and 63) + 128 '''

#23

def isolatin_to_utf8(entree):
    '''Converts the first ISO-8859-1 character from the input stream to a UTF-8 character.
    Parameters:	stream (io.BufferedReader) – The input sream opened in binary mode for reading
    Return type:	tuple
    Returns:	A tuple containing one or two bytes representing the UTF-8 character which corresponds to the ISO-8859-1 read in the input stream. If the end of file is reached, None will be returned.
    CU:	stream is opened in read and binary modes'''
    try:
        n = entree.read(1)[0]
    except IndexError :
        return None
    if n < 128 :
        #ASCII
        return (n,)
    else :
        #ISO-8859-1
        temp = n
        firstOct = temp >> 6
        firstOct = firstOct | 192
        sndOct = (n & 63) + 128
        return firstOct,sndOct

#24
def convert_file(source, dest, conversion):
    '''
    Convert `source` file using the `conversion` function and writes the
    output in the `dest` file.

    :param source: The name of the source file
    :type source: str
    :param dest: The name of the destination file
    :type dest: str
    :param conversion: A function which takes in parameter a stream (opened\
    in read and binary modes) and which returns a tuple of bytes.
    :type conversion: function
    '''
    entree = open(source, 'rb')
    sortie = open(dest, 'wb')
    octets_sortie = conversion(entree)
    while octets_sortie != None:
        sortie.write(bytes(octets_sortie))
        octets_sortie = conversion(entree)
    sortie.close()

def conversion_file_isolatin_utf8(source, dest):
    '''
    Converts `source` file from UTF-8 encoding to ISO-8859-1.
    The output is written in the `dest` file.
    '''
    convert_file(source, dest, isolatin_to_utf8)

#conversion_file_isolatin_utf8('cigale-ISO-8859-1.txt','temp.txt')

#25

def  utf8_to_isolatin(entree):
    '''Converts the first ISO-8859-1 character from the input stream to a UTF-8 character.
    Parameters:	stream (io.BufferedReader) – The input sream opened in binary mode for reading
    Return type:	tuple
    Returns:	A tuple containing one or two bytes representing the UTF-8 character which corresponds to the ISO-8859-1 read in the input stream. If the end of file is reached, None will be returned.
    CU:	stream is opened in read and binary modes'''
    try:
        poidsfort = entree.read(1)[0]
        
    except IndexError :
        return None
    if poidsfort >= 128 :
        poidsfaible = entree.read(1)[0]
        poidsfort = poidsfort & 3
        poidsfort = poidsfort << 6
        poidsfaible = poidsfaible & 63
        n = poidsfort + poidsfaible
        print(n,poidsfort,poidsfaible)
        return (n,)
    else :
        return (poidsfort,)
    
    

    
def convert_file_utf8_to_isolatin(source, dest):
    convert_file(source, dest, utf8_to_isolatin)

convert_file_utf8_to_isolatin('toto.txt','temp.txt')

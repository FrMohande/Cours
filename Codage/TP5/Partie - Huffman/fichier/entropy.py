#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#Outioua Mohand -- Jonathan Soleillet
#10 novembre 2015 --TP5 : Compression


#Note personnelles :

#xxd __.data pemets d'afficher le contenu dans un .data

#permet de crée les fichiers extrêmes

## crée un fichier avec un suel octet qui se répété plusieurs fois

##out_file = open('toto.data', 'wb')
##
##for i in range(10):
##    out_file.write(b'1')
##out_file.close()

## crée un fichier avec tous les symboles en octets

##out_file = open('titi.data', 'wb')
##
##for i in range(256):
##    out_file.write(bytes([i]))
##out_file.close()



# ------------------------------------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------------------------------------



#1 -a


#La valeur maximale de l'entropie d'un fichier est le log à base 2  256 donc 8 bits

#Pour que le fichier atteint la valeur maximale de l'entropie, il faut que tous les octets ( ou symboles) soit équiprobable
# ce qui veux dire que chaque caractère doit apparaitre le même nombre de fois que les autres.


#1-b

#la valeur minimum de l'entropie d'un fichier est de 0

#Pour que le fichier atteints la valeur minimum il faut qu'il y ait que un seul octet
#et qui peux se répèter plusieurs fois



import sys
from math import log




def log_base(a,b):
    ''' ln '''
    return log(a) / log(b)


#3 - 6

def entropy(filename): 
    '''
    Computes the entropy of the file called `filename`.

    :param filename: Input file name.
    :type filename: str
    :return: A tuple whose first element is an integer: the number of bytes read\
    and the second element is a float: the entropy of the file's content
    :rtype: tuple
    '''
    counters = {}
    '''
    Dictionary that will store the number of occurrences of each byte.
    '''
    total_sum = 0
    nb_bytes = 0
    dif = 0.0
    
    
    # Read the file to count occurrences of each byte
    infile = open(filename, 'rb')
    byte = infile.read(1)
    while len(byte) > 0 :
        if byte in counters:
            counters[byte] = counters[byte] + 1
        else:
            counters[byte] = 1
        byte = infile.read(1)
        nb_bytes = nb_bytes + 1
    # Calcul de l'entropie à partir des effectifs des octets.
    for cle in counters :
        total_sum = total_sum + ( counters[cle] * (log_base(counters[cle],2)) )
    entropy_file = log_base(nb_bytes,2) - (total_sum / nb_bytes)
    #Calcul du fichier avec un codage optimal
    optimal = 100 - (((nb_bytes*entropy_file/8)/nb_bytes) * 100)
    return (nb_bytes,entropy_file,optimal)
        
#4

#1
#cigale.txt 622 octets  l'entropie vaut 4.5 bits par octets
#sonnet18.txt 626 octets  l'entropie vaut 4.39 bits par octets
#entropy.py 2976 octets  l'entropie vaut 4.71 bits par octets
#codage.bmp 378054 octets  l'entropie vaut 4.44 bits par octets
#codage.png 64951 octets  l'entropie vaut 7.98 bits par octets
#entropy.zip 1101 octets  l'entropie vaut 7.69 bits par octets
#morse.mp3 71470 octets  l'entropie vaut 7.95 bits par octets
#morse.wav 782380 octets  l'entropie vaut 7.44 bits par octets



#Interprétation :
# Plus les fichiers compressés plus l'entropie est élèvé on évite la répétition du même symbole, plus d'information
# Pour les fichiers non compressés l'entropie est moins élévé, effectivement, on a répétition des symboles, moins d'information



#5
# l'encadrement de la taille d'un fichier est

# H(s) = l'entropie du fichier
# q = taille de l'alphabet binaire = 256 dans notre cas
# n(c) = longueur moyenne


# H(s) / log2(q) <= n(c) < (H(s) / log2(q)) + 1
# H(s) / 8 <= n(c) < (H(s) / 8 + 1 si on a un codage optimal 



#7
#le fichier cigale.txt avec une codage optimal devrait être réduit de 43.65%
#le fichier sonnet18.txt  avec une codage optimal devrait être réduit de 45.03%
#le fichier entropy.py avec une codage optimal devrait être réduit de 39.10%
#le fichier codage.bmp avec une codage optimal devrait être réduit de 44.40%
#le fichier codage.png avec une codage optimal devrait être réduit de 0.168798%
#le fichier entropy.zip avec une codage optimal devrait être réduit de 1.96%
#le fichier morse.mp3 avec une codage optimal devrait être réduit de 0.538673%
#le fichier morse.wav avec une codage optimal devrait être réduit de 6.936509%


#Interprétations:

#On compressant les fichiers, le taux  d'apparitions des symboles sont plus faibles donc il est normal que on peux
# moins optimiser ces fichiers.
#Tandis que les fichiers non compréssés il est encore possible de les optimiser puis qu'on peux encore réduire
# le taux d'apparation des symboles.






def usage():
    print ("Usage: %s <filename>" % sys.argv[0])
    print ("\t<filename>: filename for which we want to compute the entropy.\n")
    exit(1)

def main():
    if len(sys.argv) != 2:
        usage()
    (nb_bytes, entro,optimal) = entropy(sys.argv[1])
    print ("%d bytes read." % nb_bytes)
    print ("Entropy = %f bits per byte." % entro)
    print ("An optimal coding would reduce this file size by %f%%." % optimal)
    
if __name__ == '__main__':
    main()

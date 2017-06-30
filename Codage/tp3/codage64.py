#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#Outioua Mohand -- Jonathan Soleillet
#Vendredi 16 octobre - TP3 : Base 64



#L’utilitaire base64

import sys

#1
'''
Pour avoir 0 symboles =, il faut un fichier de taille multiple de 6
Ex : cigale-UTF-8.txt -> taille = 639 octets -> 639 * 8 bits -> 5112 % 6 = 0
On aura donc aucun sextets incomplet

Pour avoir 2 symboles =, il faut un fichier de taille multiple de 6
Ex : 2symboles.txt -> taille = 638 octets -> 638 * 8 bits -> 5104 % 6 = 4
On aura un sextets incomplet où il manquera 4 bits, il y aura donc deux fois le symbole ==

Pour avoir 1 symboles =, il faut un fichier de taille multiple de 6
Ex : 1symbole.txt -> taille = 637 octets -> 637 * 8 bits -> 5096 % 6 = 2
On aura un sextets incomplet où il manquera 2 bits, il y aura une fois le symbole =

'''

#2
'''
Le lien qui éxiste entre la taille des fichiers et le nombre de symboles = présents en fin de fichier
est (6-((TAILLE*8)%6))/2 = Nombre de symboles '=' à ajouter
Ex : (6-((637*8)%6))/2 = (6-2)/2 = 2, il y aura 2 symboles '=' présent
Où TAILLE est exprimer en octet
'''

#3
'''
La taille du fichier codé est plus grande que celle du fichier original, ce qui est normal on utilise,
par exemple un octet par caractère alors qu'ici on utilise de sextets

'''

#2 Codage d'un fichier en base 64

#4
BASE64_SYMBOLS = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q',
                  'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h',
                  'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
                  'z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '+', '/']
#print(BASE64_SYMBOLS[0],BASE64_SYMBOLS[5],BASE64_SYMBOLS[63]

#2.2 Encodage

#5
def bytes_to_symbols(data):
    '''
    Takes (at most) three bytes of data in input and returns the corresponding bas64 symbols.
    Parameters:	data – A list of at most three bytes
    Returns:	Four base64 symbols corresponding to the data given in input
    Return type:	str
    CU:	len(data) <= 3
    '''   
    assert(len(data) <= 3),"Takes (at most) three bytes of data in input"
    retour = ''
    taille = len(data) * 8
    nb_symbol = (6-(taille % 6))//2
    if len(data) == 1 :
        ''' == '''
        Code1 = data[0] >> 2
        Code2 = data[0] & 3
        Code2 = Code2 << 4
        retour = BASE64_SYMBOLS[Code1] + BASE64_SYMBOLS[Code2] + '='*nb_symbol
    if len(data) == 2 :
        ''' = '''
        Code1 = data[0] >> 2
        Code2 = ((data[0] & 3)<<4) + (data[1] >> 4)
        Code3 = data[1] & 15
        Code3 = Code3 << 2
        retour = BASE64_SYMBOLS[Code1] + BASE64_SYMBOLS[Code2] + BASE64_SYMBOLS[Code3] +  '='*nb_symbol
    if len(data) == 3 :
        ''' aucun'''
        Code1 = data[0] >> 2
        Code2 = ((data[0] & 3)<<4) + (data[1] >> 4)
        Code3 = ((data[1] & 15) << 2) + (data[2] >> 6)
        Code4 = (data[2] & 63)
        retour = BASE64_SYMBOLS[Code1] + BASE64_SYMBOLS[Code2] + BASE64_SYMBOLS[Code3] +  BASE64_SYMBOLS[Code4]
    return retour

#print(bytes_to_symbols([5]))
#print(bytes_to_symbols([4, 163]))
#print(bytes_to_symbols([28, 89, 101]))
#print(bytes_to_symbols([]))

#6 & 7 

def  base64_encode(source):
    '''
    Encode a file in base64 and outputs the result on standard output.

    :param source: the source filename
    :type source: str
    '''
    input = open(source, 'rb')
    data = input.read(3)
    nb = 0
    while len(data) > 0:
        
        if nb == 19:
            nb = 0
            print()   
        print (bytes_to_symbols(data), end='')
        nb = nb + 1
        data = input.read(3)
    print()
    input.close();


#print('Sans Symbole = ')
#base64_encode('cigale-UTF-8.txt')


#III  Décodage d’un fichier au format base 64

def decode_base64_symbol(symbol):
    assert(symbol in BASE64_SYMBOLS) , "decode_base64_symbol: the symbol is not part of base64"
    for i in range(len(BASE64_SYMBOLS)):
        if BASE64_SYMBOLS[i] == symbol:
            return i



def symbols_to_bytes(symbols):
    '''Convert base64 symbols to bytes
    Parameters:	symbols (str) – a string of four base64 symbols (plus the =)
    Returns:	a list of one to 3 bytes whose values correspond to the base64 symbols
    Return type:	list
    CU:	len(symbols) == 4'''
    cpt = 0
    for c in symbols:
        if c == '=':
            cpt = cpt + 1
    if cpt == 0 :
        ''' aucun ='''
        data1 = decode_base64_symbol(symbols[0])
        data2 = decode_base64_symbol(symbols[1])
        data3 = decode_base64_symbol(symbols[2])
        data4 = decode_base64_symbol(symbols[3])
        temp1 = (data2 & 15) << 4
        temp2 = (data3 & 3) << 6
        retour = [(data1 << 2) + (data2 >> 4), temp1 + (data3 >> 2), temp2 + data4 ]
    if cpt == 1 :
        ''' ='''
        data1 = decode_base64_symbol(symbols[0])
        data2 = decode_base64_symbol(symbols[1])
        data3 = decode_base64_symbol(symbols[2])
        temp1 = (data2 & 15) << 4
        retour = [ (data1 << 2) + (data2 >>4),temp1 + (data3>>2)]
    if cpt == 2:
        '''== '''
        data1 = decode_base64_symbol(symbols[0])
        data2 = decode_base64_symbol(symbols[1])
        retour = [(data1 << 2) + (data2 >> 4)]
    return retour
    

#print(symbols_to_bytes('BQ=='))
#print(symbols_to_bytes('BKM='))
#print(symbols_to_bytes('HFll'))

'''Vérification que nos deux fonctions fonctionnenent correctement'''
#print(bytes_to_symbols([4, 116, 20]))
#print(symbols_to_bytes('BHQU'))


#10

#notes du prof

''' UTF8
é   oxC3 oxA9

print(chr(0xC3) => a accentués
print(chr(0xA9) => ©
print(chr(0xC3A9) => n'importe quoi


import sys
écrit et affiche la valeur
sys.stdout.buffer.write(byte[0xC3,0xA9])) => é2
sys.stdout.buffer.write([0xC3,0xA9,0x41,0x42]) => éAB4
sys.stdout.buffer.write(bytes([]) => 0
Utilisez python3 au lieu de idle3 pour la fonction'''

def process_base64_line(line):
    ''' Process a line from a base64 input and writes the conversion on the output
    Parameters:	line (str) – a line of a base64 output
    CU:	len(line) % 4 == 0 and the line only contains base64 symbols'''
    temp = []
    for i in range(0,len(line),4):
        temp = temp + symbols_to_bytes(line[0+i:4+i])
    sys.stdout.buffer.write(bytes(temp))

#print(process_base64_line('TGEgQ2lnYWxlIGV0IGxhIEZvdXJtaQoKTGEgQ2lnYWxlLCBheWFudCBjaGFudMOpClRvdXQgbCfD'))

''' exécuter cette ligne il faut aller dans un terminale à cause du sys.stdout.buffer enlever cette ligne en commentaire et écrire 
    python3 codage64.py'''



def base64_decode(source):
    '''Decode a source file encoded in base64 and output the result.
    ''Parameters:	source (str) – the filename of the base64 file to decode'''
        
    input = open(source, 'rb')
    data = input.read(77)
    while len(data) > 0:
        ''' de supprimer les \n'''
        data = data.strip(b'\n')
        ''' de supprimer les b' '''
        process_base64_line(data.decode())
        data = input.read(77)            
    input.close();

#base64_decode('cigale.b64')
''' exécuter cette ligne il faut aller dans un terminale à cause du sys.stdout.buffer enlever cette ligne en commentaire et écrire 
    python3 codage64.py'''

#4


#12

'''Pour utiliser l'utilitare il suffit tout simplement de faire les commandes :
-pour encoder : python3 base_64 -e "cigale-UTF8.txt" 
-pour decoder : python3 base_64 -d "cigale.b64"  '''




#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#Outioua Mohand -- Jonathan Soleillet


#II

#8

#print("et",100 & 100)
#print("ou",101 | 111)
#print("ou exlc",100 ^ 110)
#print("non", ~100)
#print(">>", 1000 >> 2)
#print("<<", 1 << 2)


#9

''' le décalage à gauche signifie une multiplication
le décalage à droite signifie une division

Pour savoir de combien on multiplie ou division on mets en puissance de 2 le chiffre après le décalage

ex 1000 >> 2 est équivalent à 1000/2^2 donc 1000/4 => 250'''


#10

def deux_puissance(n):
    '''Compute 2^n
    Parameters:	n (int) – The power of two
    Returns:	The value of 2^n
    Return type:	int
    CU:	n >= 0'''
    assert(n >= 0),"CU:	n >= 0"
    return 1 << n

#print(deux_puissance(2))
#print(deux_puissance(4))




#11

'''' Pour tester si un entier est pair on fait un + 1 sur le bits de poids faible
si c'est égal à 1 l'entier est pair si c'est égal à 0 c'est impaire
L'opérateur logique est le xor et il faut qu'il soit bits à bits.'''



#12

def integer_to_binary_str(n):
    '''Get a binary representation of an integer.
    Parameters:	integer (int) – the integer to be converted in binary
    Return type:	str
    Returns:	Return the binary representation (as a string) of integer
    CU:	integer >= 0'''
    assert(n >=0),"integer >= 0"
    q = n
    r = ""
    if n == 0:
        return "0"
    while q != 0:
        r  = str(q % 2) + r
        q = q // 2
    return r

#print(integer_to_binary_str(85))
#print(integer_to_binary_str(0))



#13
def binary_str_to_integer(s):
    '''Inverse function of conversions.integer_to_binary_str()
    Parameters:	bin_str (str) – The input binary string
    Returns:	The integer whose binary representation is bin_str
    Return type:	int
    CU:	bin_str is a binary string (containing only 0s or 1s).'''
    
    puissance = len(s)-1
    r  = 0
    for i in range(len(s)):
        assert( (s[i] != 1) or (s[i] != 0)),"CU:	bin_str is a binary string (containing only 0s or 1s)"
        if s[i] == '1' :
            r = r + 2 ** puissance
        puissance = puissance - 1
    return r

#print(binary_str_to_integer('1010101'))





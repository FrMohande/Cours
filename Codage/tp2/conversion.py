#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#Outioua Mohand -- Jonathan Soleillet

#Conversion de bases

#Notes

''' %x % 123 ==  {:x}.format(123)

for i in range(16):
    print("{:d}\t{:b}\t{:x}".format(i,i,i))'''


#I.1


#1

'''%x => permet de convertir en hexadécimal

%X => permet de convertir en hexadécimal mais si il y a une lettre A...F celle ci va être en majuscule.

%o => permet de convertir en octal'''

#2

#print(bin(1331))
#print(hex(1331))
#print(oct(1331))






#I.2

#3

'''Lorsque n est un entier compris entre 0 et 9, chr(ord('0') + i) va
nous afficher les chiffres de la table ascii ( 0 à 9)'''

'''Si n>=10 l'expression va nous afficher les caractères spéciaux(:,>,<,...) et
les lettres ( a,b,...z,A,...Z)'''


#4

'''chr => int to char
ord => char to int'''

''' chr(ord('7') + i) '''



#5
def integer_to_digit(n):
    ''' Convert an integer in a hexadecimal digit
    Parameters:	integer (int) –
    Returns:	the character representing the hexadecimal digit
    Return type:	str'''
    if n < 10:
        return chr(ord('0') + n)
    else:
        return chr(ord('7') + n)

#for i in range(16):
    #print(integer_to_digit(i))

#6


def integer_to_string(n,b):
    '''Gives the representation in base base of the integer integer.
Parameters: integer (int) – the integer we want to represent
    base (int) – the base in which the integer must be represented

Returns:The string representation of the integer given in parameter in base base.
Return type: str
CU: base >= 2 and base <= 16 and integer >= 0'''
    assert( 2 <= b <= 16 and n >= 0 ), "CU: base >= 2 and base <= 16 and integer >= 0" 
    q = n
    r = ""
    hexa = ['A','B','C','D','E','F']
    if n == 0:
        return "0"
    while q != 0:
        if q % b < 10 :
            r  = str(q % b) + r
        else :
            r = hexa[(q % b)-10] + r 
        q = q // b
    return r
#print(integer_to_string(15,16))
#print(integer_to_string(1331, 2))
#print(integer_to_string(250, 16))


#7

def tab():
    for i in range(0,21):
        print(i,":",integer_to_string(i,2),integer_to_string(i,8),integer_to_string(i,16))
#tab()


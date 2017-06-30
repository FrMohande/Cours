#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#Outioua Mohand -- Jonathan Soleillet

#La numération shadok

'''GA = 'O'
BU = '−'
ZO = 'L'
MEU = '◿' '''

#3
GA = chr(0x004F)
BU = chr(0x2212)
ZO = chr(76)
MEU = chr(0x25FF)


ALPHABET_SHADOK = [GA,BU,ZO,MEU] = [chr(0x004F),chr(0x2212),chr(76),chr(0x25FF)]

''' 13 dec  = 3 *4+1 = 3 1 en base 4 = '◿-' '''

def dec_to_base(n,b):
    q = n
    r = ""
    while q != 0:
        r  = str(q % b) + r 
        q = q // b
    return r



#4
def entier_en_shadok(n):
    if n!= 0:
        c = str(dec_to_base(n,4))
        r = ""
        for i in c:
            r = r + ALPHABET_SHADOK[int(i)] 
        return r
    else :
        return ALPHABET_SHADOK[0]
print(entier_en_shadok(13))
print(entier_en_shadok(0))

#5
print(entier_en_shadok(2014))
print(dec_to_base(2014,4))
print()
print()

#6


def base_to_dec(n,b):
    convert = str(n)
    r = 0
    j = len(convert)-1
    for i in convert:
        r = r + int(i)*b**j
        j = j - 1
    return r
print(base_to_dec(1,4))
print()
print()


def shadok_en_entier(n):
    t = len(n)
    i = 0
    u = ""
    for j in range(0,len(n)) :
        while n[j] != ALPHABET_SHADOK[i] :
            i = i+1
        u = u + str(i)
        i = 0
    return base_to_dec(int(u),4)
print(shadok_en_entier(MEU+BU))
        
        
#Messages Shadok

#1

'''1 octet = 8 bits
shadok est en base 4 donc 2² donc on prends par paquet de 2'''

#2

def octet_en_shadok(o):
    assert type(o) in {int}
    assert o in range(256), "Le paramètre de octect_en_shadock dois être compris entre 0 et 255"
    b = entier_en_shadok(o)
    if len(b) < 4 :
        b = ALPHABET_SHADOK[0]*(4 - len(b)) + b
    return  b
def code_car_en_shadok(c):
    return octet_en_shadok(ord(c))
        
def code_en_shadok(c):
    l = ''
    for k in c :
        l = l + octet_en_shadok(ord(k))    
    return l
def decode_car_du_shadok(c):
    return chr(shadok_en_entier(c))


def decode_du_shadok(s):
    l = ''
    temp = ''
    for i in range(0,len(s)-3,4):
        temp = s[i:i+4]
        print(i,temp)
        l = l + decode_car_du_shadok(temp)
    return l 

print(decode_du_shadok('−−−O−LL−−L◿−−L◿◿−L◿O−L−−−L◿◿−L◿L'))

#decode_du_shadok('−O−◿−OO−−OOL−−−−−−LL−O◿◿−O◿−−O−−−−−−')

''''GABUZOMEU'''
































    

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#Outioua Mohand -- Jonathan Soleillet


#14


from op_logique import *
import struct


def byte_to_binary(byte):
    '''Get a list of bytes corresponding to a binary string.
    Parameters:	binary (str) – A binary string representing one or several bytes
    Returns:	A list of bytes. We assume that the binary string is encoded in big endian
    Return type:	list
    CU:	binary is a binary string whose length is a multiple of 8.
    If we don't have an entire byte, we fill the binary string to have an entire bit'''
    res = integer_to_binary_str(byte)
    n = len(res)
    res = "0"*(8-n) + res 
    return res

#print(byte_to_binary(255))
#print(byte_to_binary(1))
#print(byte_to_binary(0))



#15

def float_to_bin(n):
    '''Get the binary representation of a float (the struct.pack() method should be used).
Parameters:	float (float) – The float to be converted
Returns:	The binary representation according to the IEEE-754 32-bit encoding
Return type:	str'''
    res = ""
    bytes_stored = struct.pack('>f', n)
    for i in range(4):
        res = res + byte_to_binary(bytes_stored[i])
    return res
#print(float_to_bin(3.5))



#16

def change_a_bit(binary,position):
    '''Changes a bit in a binary string.
Parameters: binary (str) – The binary string
    position (int) – The position at which the bit must be changed in binary.
Returns: The modified binary string where the bit at position position has bee changed
Return type: str
CU: 0 <= position < len(binary) and binary is a binary string'''
    assert all([c in '01' for c in binary]),"CU: binary is a binary string"
    assert(0 <= position < len(binary)),"CU: 0 <= position < len(binary)"
    if(binary[position] == '1'):
        return binary[:position] + '0' + binary[position+1:]
    else:
        return binary[:position] + '1' + binary[position+1:]
#print(change_a_bit('0110',0))
#print(change_a_bit('0110',1))



#17

def binary_to_bytes(s):
    '''Get a list of bytes corresponding to a binary string.
Parameters:	binary (str) – A binary string representing one or several bytes
Returns:	A list of bytes. We assume that the binary string is encoded in big endian
Return type:	list
CU:	binary is a binary string whose length is a multiple of 8.
If we don't have an entire byte, we fill the binary string to have an entire bit'''
    cpt = 1
    r,temp = "",s
    l = []
    if( len(s) % 8 != 0):
        temp = "0"*(8- len(s) % 8) + temp
    n = len(temp) // 8
    while cpt <= n :
        for i in range(8*(cpt-1),8*cpt):
            r = r + temp[i]
        l.append(binary_str_to_integer(r))
        r = ""
        cpt = cpt + 1
    return l

#print(binary_to_bytes('110101101101011111011000'))


#18
'''%.2f% permet de convertir un float en chaine de caractère'''

def change_a_bit_in_float(n,bit_position):
    '''Changes a bit in the IEEE-754 32-bit float representation. Uses the struct.unpack() method.
    Parameters: float (float) – The float we want to modify
              bit_position (int) – The position (in the binary IEEE-754 representation) where the bit will be modified.
    Returns: the value of float where the bit at position bit_position in its IEEE-754 binary representation has been changed
    Return type: float
    CU: bit_position >= 0 and bit_position < 32'''
    assert(0 <= bit_position < 32),"CU: bit_position >= 0 and bit_position < 32"
    r = float_to_bin(n)
    bytes_stored = struct.unpack('>f', bytes(binary_to_bytes(change_a_bit(r,bit_position))))
    return  bytes_stored  

#print('%.2f' % change_a_bit_in_float(3.14,0))



#19

#print('%.2f' % change_a_bit_in_float(2.0,0))
#print('%.2f' % change_a_bit_in_float(2.0,9))
#print('%.2f' % change_a_bit_in_float(2.0,31))

''' Modfier le premier bit, modifie le signe du réel, le 9e change '''

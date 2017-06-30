#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#Outioua Mohand -- Jonathan Soleillet
#25 novembre 2015
#TP : Simulation d’un canal bruité, et codage correcteur d’erreur - CBSSM appliqué sur un fichier



'''
   Simulating an information transmission through a noisy channel.
   
   :author: FIL - IEEA - Univ. Lille 1 (déc. 2010, août 2015)
'''

import sys
from binary_channel import *
from repeat_three_times import *

#Notes

#Pour comparer les octets entre deux fichiers cmp -b -l "fichier1" "fichier2"
#Pour savoir le nombre d'octets différents on rajoute | wc -l
#read(1) nous renvoie 1 bytes qui est une chaine d'octet

def transmit(p, encode, in_filename, out_filename):
    '''
    Read bytes in the input, process them using the `encode` function,
    send them through a CBSSM (whose error probability is `p`) and finally
    write them in the output.

    :param p: Error probability
    :type p: float
    :param encode: A function that takes a byte in parameter and returns a list of bytes.
    :type encode: function
    :param in_filename: Input filename
    :type in_filename: str
    :param out_filename: Output filename
    :type out_filename: str
    :UC: 0 <= p <= 1
    '''
    stream_read = open(in_filename,"rb")
    stream_write = open(out_filename,"wb")
    byte = stream_read.read(1)
    #read(1) => 1 bytes
    while byte != b'' :
        list_byte = encode(byte[0])
        for c in list_byte:
            #on utilise bytes[] car avec bytes() on crée une chaine de byte de taille de l'entier
            stream_write.write(bytes([cbssm(p,c)]))
        byte = stream_read.read(1)
    stream_write.close()
    stream_read.close()
    
def put_byte_in_list(byte):
    '''
    Put a byte in a list of one element.

    :param byte: A byte
    :type byte: int
    :return: A list of one element: `byte`
    :rtype: list
    :Examples:

    >>> put_byte_in_list(120)
    [120]
    >>> put_byte_in_list(64)
    [64]
    '''
    return [byte]

def receive(nb_bytes, decode, in_filename, out_filename):
    '''
    Decode a file transmitted with an error-correction code.
    The error-correction used must encode one or several bytes at the same time.
    
    The function reads bytes in the input, process them using the `decode`
    function, and finally write them in the output.

    :param nb_bytes: The number of bytes to read so that one byte is decoded.
    :type nb_bytes: int
    :param decode: A function that takes a `bytes` object (containing `nb_bytes` bytes) in parameter and returns a byte
    :type decode: function
    :param in_filename: Input filename
    :type in_filename: str
    :param out_filename: Output filename
    :type out_filename: str
    :UC: nb_bytes > 0
    '''
    assert(nb_bytes > 0), "erreur fdp"
    stream_read = open(in_filename,"rb")
    stream_write = open(out_filename,"wb")
    byte = stream_read.read(nb_bytes)

    detected = 0
    corrected = 0 
    while byte != b'' :
        byte_decode = decode(byte)
        detected = detected + byte_decode[1]
        corrected = corrected + byte_decode[2]
        stream_write.write(bytes([byte_decode[0]]))
        byte = stream_read.read(nb_bytes)
    stream_write.close()
    stream_read.close()
    return (detected,corrected)



def usage ():
    '''
    `usage ()` indicates how to use the program
    '''
    print( "Usage : %s <p> <input> <output>" % sys.argv[0]);
    print( "\t<p> = error probability (on one bit)") ;
    print( "\t<input> = filename corresponding to the CBSSM input") ;
    print( "\t<output> = filename corresponding to the CBSSM output") ;
    exit(1)


def main ():
    if len(sys.argv) != 4:
        usage ()
    else:
        nb_byte = int(sys.argv[1])
        p = float(sys.argv[1])
        in_filename = sys.argv[2]
        out_filename = sys.argv[3]
        transmit(p, put_byte_in_list, in_filename, out_filename)
        #receive(nb_byte, decode,in_filename,out_filename)
        exit(0)

if __name__ == '__main__':
    main()

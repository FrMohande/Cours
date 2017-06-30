#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#Outioua Mohand -- Jonathan Soleillet
#2 novembre 2015
#TP7 : Simulation d’un canal bruité, et codage correcteur d’erreur - Codage de Hamming


#17
import numpy as np

#18
g_8_4 = np.matrix([[1,0,0,0,1,1,0,1],[0,1,0,0,0,1,1,1],[0,0,1,0,1,0,1,1],[0,0,0,1,1,1,1,0]])

#19
controlT_g_8_4 = np.vstack([g_8_4.T[4:].T, np.identity(4,dtype=int)])
modulo2 = np.vectorize(lambda i: i % 2)

#21

def value_to_vector(value, size):
    '''
    Transform an integer to a vector of the given size.

    :param value: The integer to transform in a binary vector
    :type value: int
    :param size: The size of the returned vector
    :type size: int
    :return: A matrix of 1 row and `size` elements. The elements in the matrix\
    correspond to the base 2 representation of the integer.
    :rtype: matrix
    :UC: 0 <= value < 2^size
    :Examples:

    >>> np.array_equal(value_to_vector(0, 4), np.matrix('0 0 0 0'))
    True
    >>> np.array_equal(value_to_vector(12, 4), np.matrix('1 1 0 0'))
    True
    >>> np.array_equal(value_to_vector(13, 4), np.matrix('1 1 0 1'))
    True
    '''
    assert value >= 0 and value < (1 << size), "The value cannot fit in %d bits" % size
    binary_list = [int(i) for i in ('{0:0%db}' % size).format(value)]
    return np.matrix(binary_list)

def vector_to_value(vector):
    '''
    Transform a vector to an integer

    :param vector: A binary matrix containing a single row
    :type vector: matrix
    :return: The inverse of the function `hamming.value_to_vector`
    :rtype: int
    :Examples:

    >>> vector_to_value(np.matrix([1, 0, 0, 0]))
    8
    >>> vector_to_value(value_to_vector(12, 4))
    12
    >>> vector_to_value(value_to_vector(0, 4))
    0
    '''
    binary_list = vector.tolist()[0]
    n = len(binary_list)
    return sum(b << (n-i-1) for i, b in enumerate(binary_list))

#22
def hamming_encode(value, g):
    '''
    For a Hamming (or Hamming-like) encoding taking 4 bits in input.
    Parameters:
      value (int) – An integer value where at most the four least significant bits are set
      g (matrix) – The generating matrix for that encoding

    Returns: The value of the Hamming encoding using the generating matrix g.
    Return type: int
    UC:	0 <= value < 16
    '''
    assert(0<=value<=16),"Value must be in range 0 to 16"
    return vector_to_value(modulo2(value_to_vector(value,4)*g))

#23
def encode_byte_8_4(byte):
    '''
    Encode the byte using Hamming-like [8,4] encoding
    Parameters:	byte (int) – The byte to encode
    Returns:	A list of two bytes corresponding to the encoding of byte
    Return type:  list
    UC:	0 <= byte < 256
    '''
    assert(0<=byte<256),"Value must be in range 0 to 256"
    fst_part = byte >> 4
    snd_part = byte & 15
    x = hamming_encode(fst_part,g_8_4)
    y = hamming_encode(snd_part,g_8_4)
    return [x,y]

#24
def get_data_from_8_4(value, controlT):
    '''
    Parameters:	
      value – a byte that was encoded using a [8, 4, 4]-linear coding
      type – int
      controlT – The transpose of the control matrix of the encoding.
      type – matrix
    Returns: A tuple of three elements. 1. The decoded value (between 0 and 16) using the [8, 4, 4]-linear coding. Errors are corrected, if possible. 2. A boolean whose value is False iff no error was detected. 3. A boolean whose value is False iff no error was corrected.
    Return type: tuple
    UC:	0 <= value < 256
    '''
    assert(0<=value<256),"Value must be in range 0 to 256"
    controle = value & 15
    syndrome = modulo2(value_to_vector(value,8)*controlT)
    index_err = -1
    if vector_to_value(syndrome) != 0:
        syndrome = syndrome.tolist()[0]
        for i in range(0,8):
            if controlT.tolist()[i] == syndrome :
                index_err = i
        if index_err == -1 :
            #syndrome non nul et non présent dans la matrice de controle
            return value >> 4,True,False
        else :
            #syndrome non nule et présent dans la matrice de contrôle
            value = value ^ (1<<(7-index_err))
            return value >> 4,True,True
    else :
        #syndrome nul
        return value >> 4,False,False

#25

def decode_byte_8_4(bytes_read) :
    '''
    Using the two bytes that have been transmitted return the decoded byte (possibly corrected), together with information on the number of errors detected or corrected.
    Parameters:	bytes_read (bytes) – Two bytes
    Returns:	A tuple of three elements. 1. The decoded value (between 0 and 255) using the [8, 4, 4]-linear coding. Errors are corrected, if possible. 2.
    An integer corresponding to the number of detected errors. 3. An integer corresponding to the number of corrected errors.
    Return type:	tuple
    UC:	len(bytes_read) == 2
    '''
    assert(len(bytes_read) == 2),"function take 2 bytes max"
    nb_error = 0
    nb_corrected = 0
    fst_part,fst_err,fst_correc = get_data_from_8_4(bytes_read[0],controlT_g_8_4)
    snd_part,snd_err,snd_correc = get_data_from_8_4(bytes_read[1],controlT_g_8_4)
    #Table de vérité
    # erreur et corrigé = 1 erreur et 1 corrigé
    # erreur et pas corrigé = 2 erreurs et 0 corrigé
    # pas erreur et pas corrigé = 0 erreur et 0 corrigé
    if fst_err and fst_correc :
        # erreur et corrigé = 1 erreur et 1 corrigé
        nb_error = 1
        nb_corrected = 1
    elif fst_err and not fst_correc :
        # erreur et pas corrigé = 2 erreurs et 0 corrigé
        nb_error = nb_error + 2

    if snd_err and snd_correc :
        # erreur et corrigé = 1 erreur et 1 corrigé
        nb_error =  nb_error + 1
        nb_corrected = nb_corrected + 1
    elif snd_err and not snd_correc :
        # erreur et pas corrigé = 2 erreurs et 0 corrigé
        nb_error = nb_error + 2
    return ((fst_part << 4) + snd_part),nb_error,nb_corrected

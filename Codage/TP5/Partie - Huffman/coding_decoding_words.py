#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#Outioua Mohand -- Jonathan Soleillet
#10 novembre 2015 --TP4 : Codages et décodages



#Mettre tout les tests en fin de fichier ex 
#if __name__ == '__main__':
    #print()


from coding import *


source_alphabet1 = ['a', 'b', 'c']
code = ['010', '100', '110']
my_coding = create(source_alphabet1, code)


source_alphabet = \
                ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N',\
                 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', ' ']
code1 = \
      [ "00000", "00001", "00010", "00011", "00100", "00101", "00110", "00111", "01000", "01001", "01010", "01011", "01100",\
             "01101", "01110", "01111", "10000", "10001", "10010", "10011", "10100", "10101", "10110", "10111", "11000", "11001", "11111" ]

code2 = \
      [".-/", "-.../", "-.-./", "-../", "./", "..-./",\
            "--./", "..../", "../", ".---/", "-.-/", ".-../", "--/", "-./", "---/", ".--./", "--.-/", ".-./", ".../", "-/", "..-/", "...-/", ".--/", "-..-/", "-.--/", "--../", "---./"]

code3 = \
       ["1010", "0010011", "01001", "01110", "110", "0111100", "0111110", "0010010", "1000", "011111110", "011111111001", "0001", "00101", "1001",\
            "0000", "01000", "0111101", "0101", "1011", "0110", "0011", "001000", "011111111000", "01111110", "0111111111", "01111111101", "111"]






#2

def affichage_code(src_alphabet,code,coding):
    for i in range(len(src_alphabet)):
        print(coding.code(src_alphabet[i]))       
#3
def affichage_decode(src_alphabet,code,coding):
    for i in range(len(src_alphabet)):
        print(coding.decode(code[i]))

#4

#Si on tente de coder un symbole qui n'est pas dans l'alphabet source il y a une exception
#coding.Not_codable_symbol'''

#5

#Si on tente de décoder un mot qui n'est pas dans le code
#on obtient une exception de type coding.Undecodable_word'''


#6

coding1 = create(source_alphabet, code1)
coding2 = create(source_alphabet, code2)
coding3 = create(source_alphabet, code3)




#8

def code_word(word,prm_coding):
    '''
    Code a word with the provided coding
    Parameters:	
    word (str) – the word to be coded
    my_coding (Coding) – the coding to use for coding the word
    Returns:	word coded with my_coding
Return type:	str
CU:	
Symbols in the word are in the source alphabet of the coding
Examples:'''
    s = ''
    for carac in word:
        try:
            s = s + prm_coding.code(carac)
        except Not_codable_symbol:
            raise Not_codable_symbol ('symbole {:s} non codable'.format(carac))
    return s

#9

#print(code_word('CODAGE', coding1))
#print(code_word('CODAGE', coding2))
#print(code_word('CODAGE', coding3))

#11
def decode_fixed_length_word(codeword, prm_coding):
    '''
    Decode a word using a fixed-length coding
    Parameters:	
        codeword (str) – the codeword to be decoded
        my_coding (Coding) – the coding to use for decoding the codeword

    Returns: the result of decoding codeword with my_coding
    Return type:    str
    CU:	The codeword was obtained from the coding my_coding'''
    s = ''
    for i in range(0,len(codeword),5):
        try:
            s = s + prm_coding.decode(codeword[i:i+5])
        except Undecodable_word:
            raise Undecodable_word ('mot {:s} non decodable'.format(codeword[i:i+5]))
    return s

#12

#print(decode_fixed_length_word("000100111000011000000011000100",coding1))

#13

#LA PHILANTHROPIE DE L OUVRIER CHARPENTIER
#14 - 15
def decode_comma_word(word, comma, prm_coding):
    '''
    Code a word with the provided comma coding
    Parameters:	
    word (str) – the word to be coded
    comma (str) – the symbol used as a separator
    my_coding (Coding) – the coding to use for coding the word
    Returns:	word decoded with my_coding
    Return type:    str
    CU:	len(comma) == 1 and Symbols in the word are in the source alphabet of the coding'''
    assert(len(comma) == 1),"Le séparateur doit avoir un seul caractère"
    s = ''
    mot = ''
    if len(word) == 0 :
        return '' 
    if comma in word and word[len(word)-1] == comma:
        for i in range(len(word)):
            mot = mot + word[i]
            if word[i] == "/" :
                try:
                    s = s + prm_coding.decode(mot)
                except Undecodable_word:
                    raise Undecodable_word ('symbole {:s} non codable'.format(mot))
                mot = ''
    else :
        raise Undecodable_word ("decode_comma_word: comma not found, cannot decode the word")
    return s


#16

#POUR LA FRANCE D EN BAS DES NOUILLES ENCORE

#PREFIXE

def decode_prefix_letter(word, my_coding):
    '''
    Decodes the first letter of the word, assuming a prefix coding was used.

    :param word: A word that was coded using `coding`
    :type word: str
    :param my_coding: The coding used for (de)coding
    :type my_coding: coding.Coding
    :return: a tuple whose elements are: 1) the symbol associated with the\
    first decodable prefix 2) the length of the first decodable prefix
    :rtype: tuple
    :CU: `word` was coded using `my_coding`
    :Examples:

    >>> decode_prefix_letter("0010010", coding3)
    ('H', 7)
    >>> decode_prefix_letter("00100101000", coding3)
    ('H', 7)
    >>> decode_prefix_letter("00", coding3)
    Traceback (most recent call last):
    ...
    coding.Undecodable_word: decode_prefix_letter: no decodable prefix
    '''
    word_length = len(word)
    for i in range(1,word_length+1):
        try:
            prefix = my_coding.decode(word[:i])
            return (prefix, i)
        except:
            pass
    raise Undecodable_word

#18

def decode_prefix_word(word,my_coding):
    '''
    Decode a word with a prefix coding
    Parameters:	
    word (str) – the word to be decoded
    my_coding (Coding) – the prefix coding that was used for coding the word
    
    Returns:	word decoded with my_coding
    
    Return type:	str
    CU:	The word was coded using the coding my_coding'''
    index = 0
    mot = ''
    while index != len(word):
        (symbol,taille_symb) = decode_prefix_letter(word[index:],my_coding)
        mot = mot + symbol
        index = index + taille_symb
        symbol = ''
    return mot
        
#19

#THALES EST TOUJOURS A FAIRE


#Stockage et lecture en binaire

from flottant import * 

#20
#Le fichier file.txt contient les lettres A et B
import tempfile; r=tempfile.NamedTemporaryFile()
def write_bits(stream,bits):
    '''
    Write bits (a number multiple of 8) in a writable stream.
    Parameters:	
    stream – a steam opened in write and binary modes
    bits (str) – a string made of binary characters
    
    Action: Writes all the possible bits to the stream. We recall that bits can only be written byte per byte (8 bits per 8 bits).
    Returns:	the bits that have not been written yet to the stream'''
    assert('b' in stream.mode and stream.writable()),"The stream must be opened in write and binary modes ('wb')"
    byte = bytes(binary_to_bytes(bits[:len(bits)-(len(bits)%8)]))
    stream.write(byte)
    return bits[len(bits)-(len(bits)%8):]


#21

#Notre fonction binary_to_bytes rajoutes déjà les bits manquants si c'est inférieur à 8
def complete_byte(bits):
    '''
    Completes a byte.
    Parameters:	bits (str) – a binary string
    Returns:	A binary string of 8 bits which completes the string bits. The completion adds a 1 followed by as many zeroes as necessary to reach 8 bits.
    Return type:	str
    CU:	len(bits) < 8'''
    assert(len(bits)<8)," I cannot complete a completed byte!"
    nb_0 = 8 - len(bits) - 1 
    bits = bits + '1' + '0'*nb_0
    return bits

#22
def read_bits(stream):
    '''
    Get the first 8 bits from the input stream.
    Parameters:	stream – The input stream which was opened in read and binary modes.
    Returns:	A binary string made of 8 bits (or an empty string)
    Return type:	str
    CU:	The stream was opened in read and binary modes.'''
    assert('b' in stream.mode and stream.readable()),"The stream must be opened in read and binary modes ('wb')"
    temp = list(stream.read(1))
    if len(temp) !=0 :
        return byte_to_binary(temp[0])
    else :
        return ''

#23
def uncomplete_byte(bits):
    '''
    The reverse function of complete_byte.
    Parameters:	bits – a string of 8 bits
    Returns:	A binary string of length < 8 for which the completion was removed (from the last 1-bit to the end).
    Return type:	str
    CU:	len(bits) == 8'''
    assert(len(bits)==8),'I can only uncomplete a byte'
    compteur = len(bits)-1
    while bits[compteur] != '1':
        compteur = compteur - 1
    return bits[:compteur]

#24
def remove_completion(bits):
    '''
    Remove the completion bits from the end of a binary string.
    Parameters:	bits (str) – a binary string of length >= 8 (which was already completed)
    Returns:	Return the binary string where the completion has been removed at the end (please note that the completion is done only on the last byte).
    Return type:	str
    CU:	len(bits) >= 8'''
    assert(len(bits) >= 8),'Length de bits must be >= 8'
    s = bits[:len(bits)-8]
    s = s + uncomplete_byte(bits[len(bits)-8:])
    return s

def flush_binary_string(binary, stream):
    '''
    Flush a binary string by writing as many bytes as possible in the output
    stream.

    :param binary: A binary string
    :type binary: str
    :param stream: An output stream
    :return: the bits that could not be written in the output stream (the\
    length of the returned string is necessarily < 8).
    :Examples:

    >>> import tempfile; r=tempfile.NamedTemporaryFile()
    >>> flush_binary_string('01000001', r)
    ''
    >>> r.seek(0);
    0
    >>> r.read().decode()
    'A'
    '''
    while len(binary) >= 8:
        binary = write_bits(stream, binary)
    return binary

def write_binary_string_in_file(binary, file):
    '''
    Write the binary string in the file (the string is written 8 bits per 8
    bits in the file).
    As the binary string can have any length, the last byte will be completed
    so that all the content could be written to the file.

    :param binary: a binary string
    :type binary: str
    :param file: The filename of the file where the binary string will be\
    written
    :type file: str
    :Examples:

    >>> import tempfile; r=tempfile.NamedTemporaryFile()
    >>> write_binary_string_in_file('01000001010', r.name)
    >>> r.seek(0);
    0
    >>> r.read().decode()
    'AP'
    '''
    out_file = open(file, 'wb')
    binary = flush_binary_string(binary, out_file)
    write_bits(out_file, complete_byte(binary))
    out_file.close()

def read_file(file):
    '''
    Read the data in the file and returns a binary string corresponding to
    that data.

    :param file: the filanem of the file to read.
    :type file: str
    :return: The binary string of the data that was stored in the file. The\
    completion will be removed from the binary string.
    :rtype: str
    :Examples:

    >>> import tempfile; r=tempfile.NamedTemporaryFile()
    >>> write_binary_string_in_file('01000001010', r.name)
    >>> r.seek(0);
    0
    >>> read_file(r.name)
    '01000001010'
    '''
    in_file = open(file, 'rb')
    bits = ''
    binaire = read_bits(in_file)
    while binaire != '':
        bits += binaire
        binaire = read_bits(in_file)
    in_file.close
    if len(bits) > 0:
        bits = remove_completion(bits)
    return bits

#25

# La taille du fichier mot3.data est 15 octets
# La longueur de la chaîne mot3 est de 112.
#La différence s'explique par le bourrage lorsque la taille de la châine de bits à écrire
#n'est pas multiple de 8: 15 * 8 = 120 bits,


#26

#On obtient ''0110001001010100001110101111111010110110111011000000011011111110000000110101101111110101110111100101010000101110'
# grâce à read_file('mot3.data') le mot est bien identique  à mot3


if __name__ == '__main__':
    affichage_code(source_alphabet1,code,my_coding)
    affichage_decode(source_alphabet1,code,my_coding)
    print()
    print(coding1.code('O'))
    print(coding1.decode('01110'))
    print(coding2.code('A'))
    print(coding2.decode(".-/"))
    print(coding3.code('Y'))  
    print(coding3.decode("0111111111"))
    print()
    print(code_word('CODAGE', coding1))
    print(code_word('CODAGE', coding2))
    print(code_word('CODAGE', coding3))
    print()
    print(decode_fixed_length_word('111111100100000', coding1))
    print(decode_fixed_length_word(code_word(''.join(source_alphabet), coding1), coding1))
    print(decode_fixed_length_word("01011000001111101111001110100001\
011000000110110011001111000101110011110100000100111110001100100111110101111111011101010010101100\
01010000010010001111110001000111000001000101111001000110110011010000010010001",coding1))
    print(decode_comma_word('', '/', coding2))
    print(decode_comma_word(code_word(''.join(source_alphabet), coding2), '/', coding2))
    print(decode_comma_word(".--./---/..-/.-./---./.-../.-/--\
-./..-./.-./.-/-./-.-././---./-.\
./---././-./---./-.../.-/.../---\
./-.././.../---./-./---/..-/../.\
-../.-.././.../---././-./-.-./--\
-/.-././","/",coding2))
    f = open('file.txt', 'wb')
    f.write(bytes([65, 66]))
    f.close()
    write_bits(r, '1101111100000001')
    r.seek(0)

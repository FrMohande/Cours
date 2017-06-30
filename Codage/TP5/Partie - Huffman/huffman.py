#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#Outioua Mohand -- Jonathan Soleillet
#24 novembre 2015 --TP5 : Compression - Partie 3 et 4 : Huffman

'''
Implantation de l'algorithme de Huffman

@author FIL - IEEA - Univ. Lille (août 2015)
'''


import doctest
import operator
from huffman_tree import HuffmanTree
import coding
import struct
from coding_decoding_words import *

def symbol_occurrences(stream):
    '''
    Read the stream and count the occurrences of each symbol in the stream
    
    :param stream: a stream opened (in read mode and in binary mode)
    :return: A dictionary whose keys are symbols and the associated values are\
    the corresponding number of occurrences
    :rtype: dict
    :Examples:
    
    >>> from io import StringIO # StringIO is used to have examples based on strings.
    >>> symbol_occurrences(StringIO("ababcaba")) == {'c': 1, 'b': 3, 'a': 4}
    True
    >>> symbol_occurrences(StringIO('aaaa')) == {'a': 4}
    True
    >>> symbol_occurrences(StringIO(''))
    {}
    >>> symbol_occurrences(StringIO('abcd')) == {'a': 1, 'b': 1, 'c': 1, 'd': 1}
    True
    '''
    counters = dict()
    byte = stream.read(1)
    while len(byte) > 0 :
        if byte in counters:
            counters[byte] = counters[byte] + 1
        else:
            counters[byte] = 1
        byte = stream.read(1)
    return counters 

    
#9

#La 1er liste sont les items du dictionnaire triée par leur nombre d'occurence
#La second permet de crée l'arbre de huffman par rapport à la liste triée
#On utilise deux liste pour ne pas faire le trie en même temps que la création que l'arbre de huffman sinon on doit parcourrir la liste à chaque fois pour pouvoir faire l'arbre.
#Donc on diminue le coût de l'algorithme
def create_forest(occurrences):
    '''
    Create the initial list of Huffman trees based on the dictionary of
    symbols given in parameter.
    
    :param occurrences: Number of occurrences of each symbol.
    :type occurrences: dict
    :return: A list sorted in ascending order on the number of occurrences\
    and on the symbols of Huffman trees of all symbols provided in\
    `occurrences`.
    :Examples: 

    >>> create_forest({'a': 4, 'c': 2, 'b': 1})
    [|b:1|, |c:2|, |a:4|]
    >>> create_forest({'e': 1, 'f': 1, 'g': 1, 'h': 1, 'a':2})
    [|e:1|, |f:1|, |g:1|, |h:1|, |a:2|]
    '''
    #key=lambda item: (item[1], item[0]) permet de trier par rapport à l'items 1 du dictionnaire
    #sinon le trie va se faire par ordre lexicographique (a,b,c,...,z)
    sorted_occs = sorted(occurrences.items(), key=lambda item: (item[1], item[0]))
    forest = [HuffmanTree(leaf[0], leaf[1]) for leaf in sorted_occs]
    return forest

def pop_least_element(list1, list2):
    '''
    Get and remove the lowest element from two lists sorted in ascending order.

    :param list1: First list sorted in ascending order
    :type list1: list
    :param list2: Second list sorted in ascending order
    :type list2: list
    :return: The lowest element among the two lists
    :UC: The two lists are sorted in ascending order and there is at least\
    one element among the two lists.
    :Examples:

    >>> pop_least_element([1], [2])
    1
    >>> pop_least_element([2], [1])
    1
    >>> pop_least_element([], [1])
    1
    >>> pop_least_element( [1], [])
    1
    '''
    assert(len(list1) + len(list2) >= 1)
    if len(list1) == 0:
        return list2.pop(0)
    if len(list2) == 0:
        return list1.pop(0)
    if list2[0] < list1[0]:
        return list2.pop(0)
    return list1.pop(0)

def create_huffman_tree(occurrences):
    '''
    Return a Huffman tree of the symbols given in `occurrences`.
    
    :param occurrences: Number of occurrences of each symbol.
    :type occurrences: dict
    :return: Return a single Huffman tree (obtained with Huffman algorithm)\
    of the symbols in `occurrences`.
    :rtype: huffman_tree.HuffmanTre
    :Examples:
    
    >>> create_huffman_tree({'a': 4, 'b': 1, 'c': 2})
    |bca:7|_<|bc:3|_<|b:1|, |c:2|>, |a:4|>
    >>> create_huffman_tree({'a': 1, 'b': 1, 'c': 2})
    |cab:4|_<|c:2|, |ab:2|_<|a:1|, |b:1|>>
    '''
    symbol_list = create_forest(occurrences)
    tree_list = []

    while len(tree_list) + len(symbol_list) != 1:
        (elem1, elem2) = (pop_least_element(symbol_list, tree_list),\
                          pop_least_element(symbol_list, tree_list))
        new_tree = HuffmanTree(left = elem1, right=elem2)
        tree_list.append(new_tree)

    if len(tree_list) == 1:
        return tree_list[0]
    return symbol_list[0]

def get_coding_from_tree(tree, code=''):
    '''
    Get the codes associated to the symbols.

    :param tree: A HuffmanTree
    :type tree: huffman_tree.HuffmanTree
    :param code: (optional parameter) the path that was followed to access the\
    current root of the tree
    :return: a list of tuples. Each tuple is made of a symbol and a code.\
    The order of the tuples in the list does not matter
    :rtype: list
    :Examples:

    >>> c=get_coding_from_tree(create_huffman_tree({'a': 4, 'b': 1, 'c': 2}))
    >>> len(c)
    3
    >>> c.count(('a', '1')) == 1
    True
    >>> c.count(('b', '00')) == 1
    True
    >>> c.count(('c', '01')) == 1
    True
    '''
    if tree.isLeaf():
        return [(tree.symbol, code)]
    return get_coding_from_tree(tree.left, code + '0') \
        + get_coding_from_tree(tree.right, code + '1')
    
def huffman_coding(tree):
    '''
    Creates a Huffman coding from a Huffman tree.

    :param tree: A Huffman tree
    :type tree: huffman_tree.HuffmanTree
    :return: A Huffman coding based on the Huffman tree given in parameter
    :rtype: coding.Coding
    :Examples:

    >>> c = huffman_coding(create_huffman_tree({'a': 4, 'b': 1, 'c': 2}))
    >>> c.code('a') + ' ' + c.code('b') + ' ' + c.code('c')
    '1 00 01'
    >>> c = huffman_coding(create_huffman_tree({'a': 1, 'b': 2, 'c': 3, 'd': 5}))
    >>> c.code('a') + ' ' + c.code('b') + ' ' + c.code('c') + ' '\
    + c.code('d')
    '110 111 10 0'
    '''
    result = get_coding_from_tree(tree, '')
    alphabet = list(map(lambda i: i[0], result))
    codes = list(map(lambda i: i[1], result))
    return coding.create(alphabet, codes)

def write_occurrences(occurrences, filename):
    '''
    Write the symbol occurrences in the given file
    
    :param occurrences: The dictionary of symbol occurrences
    :type occurrences: dict
    :param filename: The filename where the occurrences must be written.
    :type filename: str
    '''
    
    stream = open(filename, 'wb')
    for c in occurrences:
        stream.write(bytes(c))
        stream.write(bytes(struct.pack('i',occurrences[c])))
    stream.close()
def read_occurrences(filename):
    '''
    Read the symbol occurrences from the given file.

    :param filename: The filename where the occurrences must be read.
    :type filename: str
    :return: A dictionary of the symbol occurrences
    :rtype: dict
    :Examples:

    >>> import tempfile; temp = tempfile.NamedTemporaryFile()
    >>> d = {b'c': 1, b'b': 3, b'a': 4}
    >>> write_occurrences(d, temp.name)
    >>> read_occurrences(temp.name) == d
    True
    >>> d = {b'e': 1, b'f': 1, b'g': 1, b'h': 1, b'a':2}
    >>> write_occurrences(d, temp.name)
    >>> read_occurrences(temp.name) == d
    True
    '''
    stream = open(filename,'rb')
    byte = stream.read(1)
    occurence = dict()
    while byte != b'':
        key = byte
        byte = stream.read(struct.calcsize('i'))
        value = struct.unpack('i',byte)
        occurence[key] = value[0]
        byte = stream.read(1)
    stream.close()
    return occurence

    
    
def huffman_encode(filename, out_filename):
    '''
    Encode a file using Huffman algorithm and writes the result to 
    an other file.
    
    Two files will be created. One called `out_filename` containing
    a Huffman encoding of the input file. Another one called
    `out_filename`+".code" which will contain the occurrences of each 
    symbol.

    :param filename: The filename of the file to be encoded.
    :type filename: str
    :param out_filename: The filename of the file where the resulting\
    encoding will be stored.
    :type out_filename: str
    '''
    occurence = dict()
    stream = open(filename, 'rb')
    # Calcul du nombre d'occurrences
    occurence =symbol_occurrences(stream)
    # Création du codage de Huffman
    codage = huffman_coding(create_huffman_tree(occurence))
    # Ecriture du fichier stockant le dictionnaire d'occurrences
    write_occurrences(occurence,out_filename.replace(".encode","")+'.code')
    # Mise de la tête de lecture au début du fichier pour le reparcourir
    stream.seek(0)
    # Parcours du fichier et encodage des symboles lus
    byte = stream.read(1)
    s = ''
    while byte != b'':
        s = s + codage.code(byte)
        byte = stream.read(1)
    write_binary_string_in_file(s,out_filename)


def prefix_tree_decoding(bits, tree):
    '''
    Return the decoding of the binary string given in parameter
    using the Huffman tree `tree`.
    
    :param bits: a binary string (only made of 0s and 1s)
    :type bits: str
    :param tree: a Huffman tree
    :type tree: huffman_tree.HuffmanTree
    :return: Return the concatenation of symbols represented by the binary string.\
    The binary string is decoded using the Huffman tree.
    :rtype: bytes
    :UC: The binary string must end in a leaf.
    :Examples:

    >>> tree = create_huffman_tree({b'a': 1, b'b': 2, b'c': 3, b'd': 5})
    >>> prefix_tree_decoding('111110100111111110', tree)
    b'bacdbba'
    '''
    noeud = tree
    sortie = b''
    for bit in bits:
        if noeud.isLeaf():
            sortie += noeud.symbol
            noeud = tree
        if bit == '0':
            noeud = noeud.left
        else:
            noeud = noeud.right
    assert(noeud.isLeaf()), "La chaine devrait se terminer sur une feuille"
    sortie += noeud.symbol
    return sortie
    
def huffman_decode(filename, out_filename):
    '''
    Decode a file encoded with a Huffman encoding.

    :param filename: the file name of the Huffman encoded file
    :type filename: str
    :param out_filename: the file name where the decoding will be stored
    :type out_filename: str
    '''
    temp = filename
    temp = temp.replace(".encode","")
    occurence = read_occurrences(temp+'.code')
    tree = create_huffman_tree(occurence)
    
    out_file = open(out_filename,'wb')
    s = read_file(filename)
    byte = prefix_tree_decoding(s,tree)
    print(byte)
    out_file.write(byte)
    out_file.close()

#huffman_encode("huffman_skeleton.py","huffman_skeleton.encode")


#13


#1
#huffman_encode("huffman_skeleton.py","huffman_skeleton.encode")
#huffman_decode("huffman_skeleton.encode","huffman_skeleton.decode")

#la taille du fichier compressé est de 5200 octets

#2
#Pour en déduire la longueur moyenne :

#la taille du fichier non compréssé est de 8800 octets, sa longueur moyenne est de 8
# la taille du fichier compréssé est de 5200 octets, sa longueur moyenne est de x

#Grâce au produit en croix :: x = 5200 * 8 / 8800  | x = 4.7
# la longueur du fichier non compressé est de 4.7



#3
#l'entropie du fichier original est de 4.69, sa taille en octet est 8880
#l'entropie du fichier compressé est de 7.76, sa taille en octet est de 5200

#produit en croix :
#8800 8
#x   4,69
#8800 * 4,69/8 = x
# x = 5159 ocets
#la taille du fichier compressé s'il était compressé avec un codage de longueur moyenne
#vallent l'entropie serait de 5159


#4

# on prends la valeur supérieur de l'entropie du fichier compressé pour avoir la longueur fixe minimale donc 5 bits
#8800*5/8 = 5500

#la taille du fichier compressé si il était un codage de longueur fixe serait de 5500 octets

#14

#En fesant diff les deux fichiers sont bien identiques



#15

#huffman_encode("cigale.txt","cigale.encode")
#huffman_encode("sonnet18.txt","cigale.encode")
#huffman_encode("morse.mp3","morse_mp3.encode")
#huffman_encode("morse.wav","morse_wav.encode")
#huffman_encode("entropy.py","entropy.encode")
#huffman_encode("entropy.zip","entropy_zip.encode")
#huffman_encode("codage.bmp","codage_bmp.encode")
#huffman_encode("codage.png","codage_png.encode")

#morse.wav,codage.png et morse.mp3 ne peuvent plus  être optimisé ( proche de 0% )
#le fichier zip n'a été optimisé car la valeur théorique était de 1.9% elle passe à 1.3%
#cigale.txt et sonnet18.txt ont été optimisé d'environ 34% car les valeurs théoriques étaient de 43.65% et 45.03% et elles passent d'environ 9%
#codage.bmp a été optimisé de 37% car la valeur était de 44% et on passe à 7%
#entropy.py a été optimisé de 38% car la valeur théoriques était de 41%


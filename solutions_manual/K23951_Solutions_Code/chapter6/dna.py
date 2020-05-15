#!/usr/bin/env python3

import urllib.request as web

def gcContent(dna):
    """Compute the GC content of a DNA sequence.
    
    Parameter:
        dna: a string representing a DNA sequence
        
    Return value: the GC content of the DNA sequence
    """
    
    dna = dna.lower()
    count = 0
    for nt in dna:             # nt is short for "nucleotide"
        if nt in 'cg':         
            count = count + 1
    return count / len(dna)
    
def countCodon(dna, codon):
    """Find the number of occurrences of a codon in a DNA sequence.
    
    Parameters:
        dna: a string representing a DNA sequence
        codon: a string representing a codon
        
    Return value: the number of occurrences of the codon in dna
    """
    
    count = 0
    for index in range(0, len(dna) - 2, 3):
        if dna[index:index + 3] == codon:
            count = count + 1
    return count

def complement(dna):
    """Return the complement of a DNA sequence.
    
    Parameter:
        dna: a string representing a DNA sequence
        
    Return value: the complement of the DNA sequence
    """
    
    dna = dna.lower()
    compdna = ''
    for nt in dna:
        if nt == 'a':
            compdna = compdna + 't'
        elif nt == 'c':
            compdna = compdna + 'g'
        elif nt == 'g':
            compdna = compdna + 'c'
        else:
            compdna = compdna + 'a'
    return compdna

def reverse(dna):
    """Return the reverse of a DNA sequence.
    
    Parameter:
        dna: a string representing a DNA sequence
        
    Return value: the reverse of the DNA sequence
    """
    
    revdna = ''
    for nt in dna:
        revdna = nt + revdna
    return revdna

def reverseComplement(dna):
    """Return the reverse complement of a DNA sequence.
    
    Parameter:
        dna: a string representing a DNA sequence
        
    Return value: the reverse complement of the DNA sequence
    """
    
    return reverse(complement(dna))

def hamming(seq1, seq2):
    """Find the Hamming distance between two equal-length DNA sequences.
    
    Parameters:
        seq1: a string representing a DNA sequence
        seq2: a string representing another DNA sequence
        
    Return value: the Hamming distance between the two DNA sequences
    """
    
    seq1 = seq1.lower()
    seq2 = seq2.lower()
    distance = 0
    for index in range(len(seq1)):
        if seq1[index] != seq2[index]:
            distance = distance + 1
    return distance

def readFASTA(filename):
    """Read a FASTA file containing a single sequence and return 
       the sequence as a string.
    
    Parameter:
        filename: a string representing the name of a FASTA file
        
    Return value: a string containing the sequence in the FASTA file
    """
    
    inputFile = open(filename, 'r', encoding = 'utf-8')
    header = inputFile.readline()
    dna = ''
    for line in inputFile:
        dna = dna + line[:-1]

    inputFile.close()
    return dna

def getFASTA(id):
    """Fetch the DNA sequence with the given id from NCBI and return 
       it as a string.
    
    Parameter:
        id: the identifier of a DNA sequence
        
    Return value: a string representing the sequence with the given id
    """
    
    prefix1 = 'http://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi'
    prefix2 = '?db=nuccore&id='
    suffix = '&rettype=fasta&retmode=text'
    url = prefix1 + prefix2 + id + suffix
    readFile = web.urlopen(url)
    header = readFile.readline()
    dna = ''
    for line in readFile:
        line = line[:-1]
        dna = dna + line.decode('utf-8')
    readFile.close()
    return dna

## exercism assignment:     rna_transcription.py
## description:             takes in a DNA sequence as a string and outputs the corresponding RNA sequence
## use:                     rna_transcription.py "[sequence]" ["sequence" ..]
##
## written by (GitHub):     cmdellinger
## written on:              11.01.2016
## last revised:            11.01.2016

## ------
## module import calls
## ------

import sys

## ------
## function definitions
## ------

## ------
## function:    to_rna
## inputs:      string
## outputs:     string
## purpose:     takes in a DNA sequence as a string and outputs the complementary RNA sequence as a string
## ------

def to_rna(DNA_sequence):
    DNA = 'GCTA'
    RNA = 'CGAU'
    RNA_sequence = ''
    i = 0
    while i < len(DNA_sequence):
        RNA_sequence += RNA[DNA.find(DNA_sequence[i])]
        i += 1
    return RNA_sequence

## ------
## class definitions
## ------

# none

## ------
## main
## ------
# test whether an argument is passed in the command line
if len(sys.argv) >= 2:
    i = 1
    while i < len(sys.argv):
        print("DNA sequence: " + sys.argv[i])
        print("RNA sequence: " + to_rna(sys.argv[i]))
        i += 1
              
else:
    # print syntax
    print("Invalid argument(s) - expected syntax:")
    print('  rna_transcription.py "[sequence]" ["sequence" ..]')

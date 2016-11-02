## exercism assignment:     pangram.py
## description:             takes in a sentence as a string and determines if the sentence is a pangram
## use:                     pangram.py '[sentence]'
##                              OR
##                          pangram.py "[sentence]"
##
## written by (GitHub):     cmdellinger
## written on:              10.31.2016
## last revised:            11.01.2016

## ------
## module import calls
## ------

import sys

## ------
## function definitions
## ------

## ------
## function:    is_pangram
## inputs:      string
## outputs:     Boolean
## purpose:     takes in a sentence as a string and evaluates whether the sentence is a pangram to a Boolean value. a pangram is a sentence that uses all the letter of the alphabet.
## ------

def is_pangram(sentence):
    # for loop scans through the sentence to find lower or upper case letter using decimal to ASCII conversion
    # if both .find methods are false (return -1), then the letter is missing
    for i in range(0,25):
        if sentence.find(chr(65 + i)) == -1 and sentence.find(chr(97 + i)) == -1:
            return False
    return True

## ------
## class definitions
## ------

# none

## ------
## main
## ------

# test whether an argument is passed in the command line
if len(sys.argv) != 2:
    # print syntax
    print("Invalid argument(s) - expected syntax:")
    print('  pangram.py "[sentence]"')
    print("       OR")
    print("  pangram.py '[sentence]'")
else:
    # build solution in plain text
    print('Sentence:')
    print('     ' + sys.argv[1])
    
    answer = 'is'
    if is_pangram(sys.argv[1]) == False:
        answer += ' not'
    answer += ' a pangram.'
    print(answer)

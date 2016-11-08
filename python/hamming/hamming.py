## exercism assignment:     hamming.py
## description:
## use:
##
## written by (GitHub):     cmdellinger
## written on:              11.01.2016
## last revised:            11.08.2016

## ------
## module import calls
## ------

# import sys

## ------
## function definitions
## ------

def distance(string1, string2):
    differences = 0
    
    for i in range(len(string1)):
        if string1[i] != string2[i]:
            differences += 1

    return differences

## ------
## class definitions
## ------

## ------
## main
## ------


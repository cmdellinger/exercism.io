## exercism assignment:     leap.py
## description:             evaluate whether year(s) passed in are leap years
## use:                     leap.py year [year..]
##
## written by (GitHub):     cmdellinger
## written on:              10.26.2016
## last revised:            11.02.2016

## ------
## module import calls
## ------

import sys

## ------
## function definitions
## ------

## ------
## function:    is_leap_year
## inputs:      integer
## outputs:     Boolean
## purpose:     takes in the year as an integer and evaluates whether the year is a leap year to a Boolean value
## ------

def is_leap_year(year):
    if year%4 == 0:
        if year%100 == 0 and year%400 != 0:
            return False
        return True
    return False

## ------
## main
## ------

## test whether an argument is passed in the command line
if len(sys.argv) > 1:

    ## start with first argument
    i = 1
    
    ## loop to test all arguments
    while i < len(sys.argv):
    
        ## saves first argument as the year to test
        testYear = int(sys.argv[i])
    
        ## building the string to return leap year determination in plain text
        answer = str(testYear) + " is"
        if is_leap_year(testYear) == False:
            answer += " not"
        answer += " a leap year"

        ## print the leap year evalution in plain test
        print(answer)

        ## increment for next argument
        i += 1

## when no year is passed in the command line
else:
    ## send some hate
    print("Invalid argument(s) - expected syntax:")
    print('  leap.py year [years ...]')

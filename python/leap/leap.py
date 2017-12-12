"""
Exercism.io assignment - leap.py
Written by cmdellinger

Usage:
  leap.py <4-digit year>...

Evaluates 4-digit year(s) and determines if they are leap years.

Options:
    -h
"""

## ------
## Exercism.io solution
## ------

def is_leap_year(year = 0000): # -> Boolean
    """ takes in a 4-digit year and evaluates whether it is a leap year """
    if year % 100 == 0:
        return year % 400 == 0
    else:
        return year % 4 == 0

## ------
## Command-line implementation
## ------

if __name__ == '__main__':
    from docopt import docopt
    # get list of years; list contains each year as a string
    years = docopt(__doc__)['<4-digit year>']
    # convert strings in list to integers
    years = [int(year) for year in years]

    for year in years:
        # start building the answer string to return leap year determination in plain text
        answer = str(year) + " is"
        # insert "not" if year is not a leap year
        if is_leap_year(year) == False:
            answer += " not"
        answer += " a leap year"
        # print the leap year evalution in plain text
        print(answer)

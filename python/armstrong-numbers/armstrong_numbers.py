"""
Exercism.io assignment: armstrong_numbers.py
written by (GitHub):    cmdellinger
Python version:         2.7
    
Usage:
    armsrtong_numbers.py <number>...

Determines whether a number is an armstrong number.

An Armstrong number is a number that is the sum of its own digits each
raised to the power of the number of digits.
    
See README file for more detailed information.
"""

## ------
## Exercism.io solution
## ------

def is_armstrong(number = 0): #-> boolean
    ''' returns whether a number is an Armstrong number '''
    # convert to string, split by putting in list, then changing values to int
    digits = map(int, list(str(number)))
    # is sum of nth power digits (x_1^n + x_2^n...) is equal to original number
    return number == reduce(lambda x,y: x+y, map(lambda x: x**len(digits), digits))

## ------
## Command-line implementation
## ------

if __name__ == '__main__':
    from docopt import docopt
    # get list of numbers; list has numbers as strings so map to int
    numbers = map(int, docopt(__doc__)['<number>'])
    for number in numbers:
        print "{} is {}an armstrong number".format(number, 'not '*(not is_armstrong(number)))

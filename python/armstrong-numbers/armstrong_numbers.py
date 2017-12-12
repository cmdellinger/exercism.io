"""
Exercism.io assignment: armstrong_numbers.py
written by (GitHub):    cmdellinger
Python version:         2.7
    
Usage:
    

An Armstrong number is a number that is the sum of its own digits each
raised to the power of the number of digits.
    
See README file for more detailed information.
"""

def is_armstrong(number = 0): #-> boolean
    ''' returns whether a number is an Armstrong number '''
    # convert to string, split by putting in list, then changing values to int
    digits = map(int, list(str(number)))
    # is sum of nth power digits (x_1^n + x_2^n...) is equal to original number
    return number == reduce(lambda x,y: x+y, map(lambda x: x**len(digits), digits))

"""
Exercism.io assignment - difference_of_squares.py
Written by cmdellinger
    
Usage:
    None
    
Find the sum of the squares, the square of the sum, or the difference between the two.
"""

## ------
## Exercism.io solution
## ------

def square_of_sum(number = 0): # -> integer
    ''' returns the square of the sums of natural numbers up to input number '''
    sum = 0
    for integer in xrange(1, number + 1):
        sum += integer
    return sum**2

def sum_of_squares(number = 0): # -> integer
    ''' returns the sum of the squares of natural numbers up to input number '''
    sum = 0
    for integer in xrange(1, number + 1):
        sum += integer**2
    return sum

def difference(number = 0): # -> integer
    ''' returns the difference betwenn the sum of squares and the square of the sum '''
    return abs(sum_of_squares(number) - square_of_sum(number))

## ------
## Command-line implementation
## ------

if __name__ == '__main__':
    print(__doc__)

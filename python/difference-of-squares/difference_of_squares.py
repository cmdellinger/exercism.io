"""
Exercism.io assignment - difference_of_squares.py
Written by cmdellinger
    
Usage:
    difference_of_squares.py <number> (--sosq|--sqos|--diff)
    
Options:
    --sosq  Sum of squares of natural numbers up to input number
    --sqos  Square of sums of natural numbers up to input number
    --diff  Difference between the sum of squares and the square of sums
    
Find the sum of the squares, the square of the sum, or the difference between the two
for the sequence up to the number provided.
"""

## ------
## Exercism.io solution
## ------

def square_of_sum(number = 0): # -> integer
    ''' returns the square of the sums of natural numbers up to input number '''
    total = 0
    for integer in xrange(number + 1):
        total += integer
    return total**2

def sum_of_squares(number = 0): # -> integer
    ''' returns the sum of the squares of natural numbers up to input number '''
    total = 0
    for integer in xrange(number + 1):
        total += integer**2
    return total

def difference(number = 0): # -> integer
    ''' returns the difference between the sum of squares and the square of the sum '''
    # square_of_sum is always greater than sum_of_squares
    return square_of_sum(number) - sum_of_squares(number)

## ------
## Command-line implementation
## ------

if __name__ == '__main__':
    from docopt import docopt
    number = int(docopt(__doc__)['<number>'])
    #if docopt(__doc__)['--sosq'] or docopt(__doc__)['--sqos'] or docopt(__doc__)['--diff']:
    if docopt(__doc__)['--sosq']:
        print "Sum of Squares: %d" % sum_of_squares(number)
    if docopt(__doc__)['--sqos']:
        print "Square of Sum: %d" % sum_of_squares(number)
    if docopt(__doc__)['--diff']:
        print "Difference: %d" % difference(number)

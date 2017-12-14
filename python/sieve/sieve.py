"""
Exercism.io assignment: sieve.py
written by (GitHub):    cmdellinger
Python version:         2.7

Usage:
    sieve.py <number>...

Implementation of the Sieve of Eratosthenes algorithm to find primes up to a
    given number.

Algorithm (from README):
The algorithm consists of repeating the following over and over:
    - take the next available unmarked number in your list (it is prime)
    - mark all the multiples of that number (they are not prime)
Repeat until you have processed each number in your range.

When the algorithm terminates, all the numbers in the list that have not
been marked are prime.
"""

## ------
## Exercism.io solution
## ------

def sieve(limit):
    ''' uses the Sieve of Eratosthenes algorithm to find primes up to limit.
        this version uses optimizations to speed up the algorithm.
    '''
    from math import sqrt
    # build True/False sieve array (Python evaluates non-zero to True)
    sieve_array = [0,0] + range(2, limit+1)
    # perform Sieve of Eratosthenes
    for i in xrange(2, int(sqrt(limit))+1):
        if sieve_array[i]:
            for j in xrange(i**2, limit+1, i):
                sieve_array[j] = 0
    # filter non-zero results
    return filter(lambda x: x, sieve_array)

## ------
## Command-line implementation
## ------

if __name__ == '__main__':
    from docopt import docopt
    # note: everything is stored by parser as string
    for number in map(int, docopt(__doc__)['<number>']):
        print "Maximum: {}\nPrimes: {}\n".format(number, sieve(number))

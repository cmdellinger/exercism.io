"""
Exercism.io assignment: sum_of_multiples.py
written by (GitHub):    cmdellinger
Python version:         2.7

See README for problem constraints.
"""

## ------
## Exercism.io solution
## ------

def sum_of_multiples(limit = 0, multiples = []): #-> int
    ''' sums all integers in [0, limit) that are divisible by any of the given
        multiples.
    '''
    factors = []
    for multiple in multiples:
        factors += range(multiple, limit, multiple)
    return sum(set(factors))

'''
# slower solution by about x10
def sum_of_multiples(limit, multiples):
    def divisible(number):
        return any([not number % multiple for multiple in multiples])
    return sum([multiple for multiple in range(limit) if divisible(multiple)])
'''

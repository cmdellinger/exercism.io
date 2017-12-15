"""
Exercism.io assignment: acronym.py
written by (GitHub):    cmdellinger
Python version:         2.7

Usage:
    acronym.py <"string">...

Changes strings of words into uppercase acronyms based on the first letters of
    each word in the string.

See README for problem constraints.
"""

## ------
## Exercism.io solution
## ------

def abbreviate(words = ''): #-> string
    ''' creates an uppercase acronym from the first letters in given string '''
    from re import findall
    return ''.join(word[0] for word in findall('[^\W]+',words.upper()))

## ------
## Command-line implementation
## ------

if __name__ == '__main__':
    from docopt import docopt
    # note: everything is stored by parser as string
    print ' '.join(abbreviate(string) for string
                   in docopt(__doc__)['<"string">'])

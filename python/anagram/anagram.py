"""
Exercism.io assignment - anagram.py
Written by cmdellinger

Usage:
    anagram.py --source=<original> <candidates>...

Determines which of the candidate words in the candidate list is an
anagram of the source word.

Options:
    --source=<original>     Source word for anagrams
"""

## ------
## Exercism.io solution
## ------

def detect_anagrams(original = '', candidates = []): #-> []
    ''' returns the list of candidates that are anagrams of the original '''
    sorted_original = sorted(list(original.lower()))
    return [candidate for candidate in candidates if sorted(list(candidate.lower())) == sorted_original and candidate.lower() != original.lower()]

## ------
## Command-line implementation
## ------

if __name__ == '__main__':
    from docopt import docopt
    original = docopt(__doc__)['--source']
    candidates = docopt(__doc__)['<candidates>']
    print 'anagrams: ' + ' '.join(detect_anagrams(original, candidates))

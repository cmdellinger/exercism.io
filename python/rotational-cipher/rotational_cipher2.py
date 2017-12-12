"""
Exercism.io assignment - rotational_cipher.py
written by (GitHub):     cmdellinger

Usage:
    rotational_cipher.py [--key=<key>] <strings>...

Options:
    --key=<key>     Rotational key [default: 13].
    
Executes a rotational cipher or Caesar cipher on the provided strings.
*Note: default rotational key is 13.
"""

## ------
## Exercism.io solution
## ------

from string import ascii_lowercase, ascii_uppercase

def rotate(statement = '', cipher_key = 00):
    key = cipher_key % 26 if abs(cipher_key) >= 26 else cipher_key
    
    def rotate_letter(character = ''):
        
        if not character.isalpha():
            return character
        if character.isupper():
            sequence = ascii_uppercase
        elif character.islower():
            sequence = ascii_lowercase
        index_new = sequence.find(character) + key
        rotated_index = index_new % 26 if abs(index_new) >= 26 else index_new
        return sequence[rotated_index]
        
    return ''.join(map(rotate_letter, statement))

## ------
## Command-line implementation
## ------

if __name__ == '__main__':
    from docopt import docopt
    print ' '.join([rotate(string, int(docopt(__doc__)['--key'])) for string in docopt(__doc__)['<strings>']])

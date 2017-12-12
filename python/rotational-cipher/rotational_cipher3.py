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

from string import ascii_lowercase, ascii_uppercase, translate, maketrans
from itertools import islice

# modified cycle from stackoverflow ( https://stackoverflow.com/a/8942392 )
def cycle(my_list, start_at=None):
    start_at = 0 if start_at is None else my_list.index(start_at)
    while True:
        yield my_list[start_at]
        start_at = (start_at + 1) % len(my_list)

def rotate(statement = '', cipher_key = 00):
    key = cipher_key % 26 if abs(cipher_key) >= 26 else cipher_key

    # generate cipher table
    cipher_uppercase = ''.join(islice(cycle(ascii_uppercase,ascii_uppercase[key]), 26))
    cipher_lowercase = ''.join(islice(cycle(ascii_lowercase,ascii_lowercase[key]), 26))
    cipher_table = maketrans(ascii_lowercase + ascii_uppercase, cipher_lowercase + cipher_uppercase)

    return statement.translate(cipher_table)

## ------
## Command-line implementation
## ------

if __name__ == '__main__':
    from docopt import docopt
    print ' '.join([rotate(string, int(docopt(__doc__)['--key'])) for string in docopt(__doc__)['<strings>']])

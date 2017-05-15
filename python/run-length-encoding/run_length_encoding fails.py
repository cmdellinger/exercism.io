"""
Exercism.io assignment - run_length_encoding.py
Written by cmdellinger
    
Usage:
    run_length_encoding.py encode <sequence_to_encode>...
    run_length_encoding.py decode <sequence_to_decode>...

Options:
    -h help
"""

## ------
## Exercism.io solution
## ------

def decode(sequence = ''): # -> string
    from re import findall
    decoded_sequence = ''
    for piece in findall(r'([0-9]*)([a-zA-Z])', sequence):
        # -> [('number','letter')...]
        if len(piece[0]):
            decoded_sequence += int(piece[0]) * piece[1]
        else:
            decoded_sequence += piece[1]
    return decoded_sequence
    '''
    Note about re.findall(r'([0-9]*)([a-zA-Z])', sequence)
    regex will return a list tuples in the form of ('number', 'letter')
    but will return a tuple with 'number' = '' if there is only a letter
    examples:
    '2C'    -> [('2', 'C')]
    '23C'   -> [('23', 'C')]
    'C'     -> [('', 'C')]
    '2C3B'  -> [('2', 'C'),('3', 'B')]
    '''

def encode(sequence = ''): # -> string
    from itertools import groupby
    encoded_sequence = ''
    for letter_group in ["".join(letters) for letter, letters in groupby(sequence)]:
        # -> ['letter_1...', 'letter_2...', 'letter_x...']
        group_length = len(letter_group)
        if group_length > 1:
            encoded_sequence += str(group_length) + letter_group[0]
        else:
            encoded_sequence += letter_group
    return encoded_sequence

## ------
## Command-line implementation
## ------

if __name__ == '__main__':
    from docopt import docopt
    # check docopt's dict for encode flag
    if docopt(__doc__)["encode"]:
        # step through list of sequences; list contains sequence as a string
        for sequence in docopt(__doc__)["<sequence_to_encode>"]:
            print sequence, "->", encode(sequence)
    # check docopt's dict for decode flag
    if docopt(__doc__)["decode"]:
        # step through list of sequences; list contains sequence as a string
        for sequence in docopt(__doc__)["<sequence_to_decode>"]:
            print sequence, "->", decode(sequence)

"""
Exercism.io assignment - run_length_encoding.py
Written by cmdellinger
    
Usage:
    run_length_encoding.py encode <sequence_to_encode>...
    run_length_encoding.py decode <sequence_to_decode>...
    
This script encodes and decodes strings of letters and spaces by changing character repeats to '<number of repeats>character'.
Examples:
    In[x]:  run_length_encoding.py encode 'gggcc'
    Out[x]: 'gggcc' -> '3g2c'

    In[y]:  run_length_encoding.py decode '3g2c'
    Out[y]: '3g2c' -> 'gggcc'

* Note: this script assumes that characters being encoded and decoded are letters and spaces (not numbers, etc.)

Options:
    -h help
"""

## ------
## Exercism.io solution
## ------
from re import split

def decode(sequence = ''): # -> string
    ''' returns the passed sequence as decompressed version
        '3g2c' -> 'gggcc'  '''
    from re import findall
    
    def decode_segment(segment = ''): # -> string
        ''' work-horse function to decode character sequences '''
        decoded_segment = ''
        for piece in findall(r'([0-9]*)([a-zA-Z\s])', segment):
        # -> [('number','letter')...]; if only 1 then 'number' = ''
            if len(piece[0]):
                decoded_segment += int(piece[0]) * piece[1]
            else:
                decoded_segment += piece[1]
        return decoded_segment

    return decode_segment(sequence)

def encode(sequence = ''): # -> string
    ''' returns the passed sequence as compressed version
        'gggcc' -> '3g2c'   '''
    
    from itertools import groupby
    
    def encode_segment(segment = ''): # -> string
        ''' work-horse function to encode character sequences '''
        encoded_segment = ''
        for letter_group in ["".join(letters) for letter, letters in groupby(segment)]:
        # -> ['letter_1...', 'letter_2...', 'letter_x...']
            group_length = len(letter_group)
            if group_length > 1:
                encoded_segment += str(group_length) + letter_group[0]
            else:
                encoded_segment += letter_group
        return encoded_segment

    # split input sequence by separating alpha-numeric sequences and everything else
    segments = split(r'(\s+)',sequence)
    # map work-horse function (decode_segment) onto segments and join
    return ''.join(map(encode_segment,segments))

## ------
## Command-line implementation
## ------

if __name__ == '__main__':
    from docopt import docopt
    
    if docopt(__doc__)["encode"]:
        # step through list of sequences; list contains sequence as a string
        for sequence in docopt(__doc__)["<sequence_to_encode>"]:
            print sequence, "->", encode(sequence)
    if docopt(__doc__)["decode"]:
        for sequence in docopt(__doc__)["<sequence_to_decode>"]:
            print sequence, "->", decode(sequence)

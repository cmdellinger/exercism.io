"""
Exercism.io assignment: atbash_cipher.py
written by (GitHub):    cmdellinger
Python version:         2.7
    
Usage:
    atbash_cipher.py --dec <"string">
    atbash_cipher.py --enc <"string">
    
Options:
    --enc,-e          flag to encode
    --dec,-d          flag to decode
    
Applies the atbash cipher to the given string. The atbash cipher reverses the
alphabet character, so 'a'-'z' becomes the corresponding 'z'-'a'.

Any non-alphanumeric will be stripped and encoded text will be output in blocks
of 5 character (as specified in problem's README file).
"""

## ------
## Exercism.io solution
## ------

def codec(text):
    ''' core cipher function to strip and encode/decode text '''
    from string import ascii_lowercase as alphabet
    def cipher(char = ''):
        ''' helper function to change only alpha characters '''
        if char.isalpha():
            # find index in alphabet string, then return opposite (~)
            return alphabet[~alphabet.index(char)]
        else: return char
    # strip string to letters and numbers, make lowercase, apply cipher, & join
    return ''.join(cipher(char) for char in filter(str.isalnum, text.lower()))

def encode(plain_text = ''):
    ''' strips string to letter/numbers and encodes using atbash cipher '''
    from re import findall
    # use regex to pull blocks of 5 characters and join returned list
    return ' '.join(findall('.{1,5}', codec(plain_text)))

def decode(ciphered_text = ''):
    ''' strips string to letter/numbers and decodes using atbash cipher '''
    return codec(ciphered_text)

## ------
## Command-line implementation
## ------

if __name__ == '__main__':
    from docopt import docopt
    text = docopt(__doc__)['<"string">']
    if docopt(__doc__)['--enc']: print encode(text)
    elif docopt(__doc__)['--dec']: print decode(text)
    else: print __doc__

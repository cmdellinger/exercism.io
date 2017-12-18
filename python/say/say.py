"""
Exercism.io assignment: say.py
written by (GitHub):    cmdellinger
Python version:         2.7
    
Usage:
    say.py <integer>
    
Changes integer in range [0, 1 000 000 000 000) into words.
    
See README for additional problem constraints.
"""

## ------
## Exercism.io solution
## ------

def say(number = 0):
    # quick escape and input range management
    if number == 0: return 'zero'
    if number < 0 or number > 999999999999:
        raise ValueError('Number must be from 0 to 999,999,999,999.')
    # import regex's findall for easy parsing
    from re import findall
    # define word pieces for translation
    ones = ['', 'one', 'two', 'three', 'four', 'five', 'six', 'seven',
            'eight', 'nine', 'ten', 'eleven', 'twelve', 'thirteen', 'fourteen',
            'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen', 'twenty']
    tens = ['','','twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy',
            'eighty','ninty', 'hundred']
    scales = ['billion', 'million', 'thousand', '']
    # break up number into blocks of three digits
    blocks = map(int, findall('\d{1,3}', str(int(number)).zfill(12)))
    ''' for some reason I'm getting an 'invalid literal' error without the int
        for number when I run the test, but not when I use the script in jupyter
    '''
    def eval_block(block = 000): #-> string
        ''' translates integers for numbers < 1000 to words '''
        hundred, ten = map(int, findall('\d{1,2}', str(block).zfill(4)))
        text = ''
        if hundred:
            text += ones[hundred] + ' ' + tens[10]
        if hundred and ten: text += ' and '
        if ten > 20:
            text += tens[ten//10] + '-' + ones[ten%10]
        elif ten:
            text += ones[ten]
        return text
    # build pieces by mapping blocks to words and zipping with scale words
    phrases = [' '.join([block, scale]).rstrip() for block, scale
               in zip(map(eval_block, blocks), scales) if block]
    # add 'and' to the last phrase is a number < 100 and its not the only phrase
    if blocks[-1] and any(blocks[:3]) and blocks[-1] < 100:
        phrases[-1] = 'and ' + phrases[-1]
    # join all the pieces
    return ' '.join(phrases)

## ------
## Command-line implementation
## ------

if __name__ == '__main__':
    from docopt import docopt
    # note: everything is stored by parser as string
    print say(int(docopt(__doc__)['<integer>']))

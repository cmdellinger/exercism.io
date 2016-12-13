"""
Exercism.io assignment - pangram.py
Written by cmdellinger
    
Usage:
    pangram.py <sentence>
    
Count the words in a string regardless of punctuation and capitalization.
Output wordlist and number of occurences.
"""

## ------
## Exercism.io exercise
## ------

def is_pangram(sentence = ''): # -> Boolean
    """ for loop scans through the sentence to find lower or upper case letter using decimal to ASCII conversion if both .find methods are false (return -1), then the letter is missing"""
    for i in range(0,25):
        if sentence.find(chr(65 + i)) == -1 and sentence.find(chr(97 + i)) == -1:
            return False
    return True

## ------
## main
## ------

if __name__ == '__main__':
    from docopt import docopt
    sentence = docopt(__doc__)['<sentence>']

    # build solution in plain text
    print('Sentence:')
    print('     ' + sentence)
    
    answer = 'is'
    if is_pangram(sentence) == False:
        answer += ' not'
    answer += ' a pangram.'
    print(answer)

"""
Exercism.io assignment - isogram.py
Written by cmdellinger
    
Usage:
    isogram.py <word>...

Returns whether each word is an isogram. An isogram (also known as a "nonpattern word") is a word or phrase without a repeating letter.

Options:
    -h
"""

## ------
## Exercism.io solution
## ------

def is_isogram(word = ''): #-> boolen
    ''' creates a list of only letters then sees if its the same length when duplicates are removed '''
    characters = [letter.lower() for letter in list(word) if letter.isalpha()]
    return len(characters) == len(list(set(characters)))

## ------
## Command-line implementation
## ------

if __name__ == '__main__':
    from docopt import docopt
    # get list of words; list contains each word as a string
    words = docopt(__doc__)['<word>']
    
    for word in words:
        '''
        """ this is shorter, but leaves an extra space in the answer """
        # print isogram evalution in plain text
        print word, "is", int(not(is_isogram(word)))*"not", "an isogram"
        '''
        # start building the answer to return isogram determination in plain text
        answer = word + " is"
        # insert "not" if word is not an isogram
        if is_isogram(word) == False:
            answer += " not"
        answer += " an isogram"
        # print isogram evalution in plain text
        print(answer)



"""
Exercism.io assignment - bob.py
Written by cmdellinger
    
Usage:
    bob.py <'message'>...
    
    Evaluates message(s) and replies with Bob's response.
    

Bob is a lackadaisical teenager. In conversation, his responses are very limited.
    
Bob answers 'Sure.' if you ask him a question.
    
He answers 'Whoa, chill out!' if you yell at him.
    
He says 'Fine. Be that way!' if you address him without actually saying
anything.
    
He answers 'Whatever.' to anything else.

Options:
    -h
"""

## ------
## Exercism.io solution
## ------

import re

def hey(message = ''): #-> string
    """ returns the response of bob as outlined in the porblem """

    answers = {"question": 'Sure.',
               "yell": 'Whoa, chill out!',
               "nothing": 'Fine. Be that way!',
               "other": 'Whatever.'}

    # uses regular expressions to searches for words
    if len(re.findall(u'[^\W_]+', message)) == 0:
        return answers["nothing"]
    # checks to see if all the letter chars are capital
    if message.isupper():
        return answers["yell"]
    # strips ending whitespace, then checks for '?' at end
    if message.strip().endswith('?'):
        return answers["question"]
    # returns default if all other conditions failed
    return answers["other"]

## ------
## Command-line implementation
## ------

if __name__ == '__main__':
    from docopt import docopt
    # get list of words; list contains each word as a string
    messages = docopt(__doc__)["<'message'>"]
    
    for message in messages:
        print "message:", message
        print "response:", hey(message)
        print ""

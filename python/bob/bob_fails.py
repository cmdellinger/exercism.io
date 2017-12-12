"""
Exercism.io assignment - bob.py
Written by cmdellinger
    
Usage:
    bob.py <message>...
    
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
               
    punctuation = re.findall(r'[.?!]+', message)
    words = re.findall(u'[^\W_]+', message)
    print punctuation
    print words
    if len(words) == 0:
        return answers["nothing"]
    if all([word.isupper() for word in words]):
        return answers["yell"]
    if len(punctuation):
        if punctuation[-1] == '!':
            return answers["yell"]
        if punctuation[-1] == '?':
            return answers["question"]
    return answers["other"]

## ------
## Command-line implementation
## ------


# print problem test cases if call script

if __name__ == '__main__':
    print hey("Let's go make out behind the gym!")

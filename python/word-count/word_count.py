## exercism assignment:     word_count.py
## description:
## use:
##
## written by (GitHub):     cmdellinger
## written on:              11.09.2016
## last revised:            11.12.2016

## ------
## module import calls
## ------

import string

## ------
## function definitions
## ------

def word_count(sentence = ''):
    word_list = []
    parsed_sentence = sentence.translate(None, string.punctuation).split()

    for word in range(len(parsed_sentence)):
        location = -1
        for match in range(len(word_list)):
            if parsed_sentence[word] == word_list[match][0]:
                location = match
        if location == -1:
            word_list.append([parsed_sentence[word], 1])
        else:
            word_list[location][1] += 1
    word_list = dict(word_list)
    return word_list



## ------
## class definitions
## ------

## ------
## main
## ------

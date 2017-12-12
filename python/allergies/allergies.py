"""
Exercism.io assignment: allergies.py
written by (GitHub):    cmdellinger
Python version:         2.7

Allergies class to store an allergy score to keep track of a person's allergies.
    Given a person's allergy score, determines whether or not they're allergic to a
    given item, and their full list of allergies.
    
See README file for more detailed information.
"""

class Allergies(object):
    ''' stores an allergy score '''
    # allergy score item values have binary incrementation so a list can be used
    # where the index is the place value for the binary digit
    ALLERGY_LIST = ['eggs',
                    'peanuts',
                    'shellfish',
                    'strawberries',
                    'tomatoes',
                    'chocolate',
                    'pollen',
                    'cats']
                    
    def build_lst(self): #-> []
        ''' generates a list of allergies from allergy score '''
        # essentially create a boolean array as a string by reversing and
        # choping to length of allergy list
        bin_to_s = '{0:b}'.format(self.number)[::-1][:len(self.ALLERGY_LIST)]
        # build allergy list using boolean string
        return [self.ALLERGY_LIST[index] for index, char in enumerate(bin_to_s) if int(char)]

    def __init__(self, number = 0):
        ''' stores allergy score and allergy list from score '''
        self.number = number
        self.lst = self.build_lst()

    def is_allergic_to(self, allergy = ''): #-> boolean
        ''' returns whether an allergy is in the instance allergy list '''
        return allergy in self.lst

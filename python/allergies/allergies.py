class Allergies(object):
    ALLERGY_LIST = ['eggs',
                    'peanuts',
                    'shellfish',
                    'strawberries',
                    'tomatoes',
                    'chocolate',
                    'pollen',
                    'cats']
                    
    def build_lst(self):
        bin_to_s = '{0:b}'.format(self.number)[::-1][:8]
        allergy_list = [self.ALLERGY_LIST[index] for index, char in enumerate(bin_to_s) if int(char)]
        return allergy_list

    def __init__(self, number = 0):
        self.number = number
        self.lst = self.build_lst()

    def is_allergic_to(self, allergy = ''):
        return allergy in self.lst

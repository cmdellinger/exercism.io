"""
Exercism.io assignment - hamming.py
written by (GitHub):     cmdellinger

Usage:
   hamming.py <sequence1> <sequence2>

Compares the nucleotides in sequence1 and sequence2 and reports differences
also known as the Hamming distance.
"""

## ------
## Exercism.io function
## ------

def distance(string1, string2): #->
    """returns the differences (Hamming distance) between string1 and string2"""
    differences = 0

    for i in range(len(string1)):
        if string1[i] != string2[i]:
            differences += 1

    return differences

## ------
## Command-line implementation
## ------
if __name__ == '__main__':
    from docopt import docopt

    sequence1 = docopt(__doc__)['<sequence1>']
    sequence2 = docopt(__doc__)['<sequence2>']

    hamming_distance = distance(sequence1, sequence2)
    print("Hamming distance: %d" % hamming_distance)

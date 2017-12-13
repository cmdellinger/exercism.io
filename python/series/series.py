"""
Exercism.io assignment: series.py
written by (GitHub):    cmdellinger
Python version:         2.7
    
Usage:
    series.py <"series"> <slice_length>
    
Outputs all contiguous slices of given length in the number series.
    
See README file for more detailed information.
"""

## ------
## Exercism.io solution
## ------

def slices(series = '', length = 0): #-> [[]...]
    ''' returns a list of slices of given length from the number series.
        slices are lists of integers taken contiguosly from series.'''
    if length > len(series) or length < 1:
        raise ValueError('Length of slices longer than series.')
    else:
        digits = map(int, list(series))
        return [digits[i:i+length] for i in xrange(len(series)-length+1)]

## ------
## Command-line implementation
## ------

if __name__ == '__main__':
    from docopt import docopt
    # gets series and length from parser
    # note: everything is stored by parser as string
    series = docopt(__doc__)['<"series">']
    length = int(docopt(__doc__)['<slice_length>'])
    print "Slices of length: {}\nContained in: {}".format(length, series)
    print slices(series, length)

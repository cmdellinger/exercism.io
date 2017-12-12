"""
Exercism.io assignment - gigasecond.py
written by (GitHub):     cmdellinger

Usage:
   gigasecond.py <initial datetime object>

Adds a gigasecond (10^9 seconds) to the initial datetime object passed.
"""

## ------
## Exercism.io function
## ------
from datetime import datetime
from datetime import timedelta

def add_gigasecond(time = datetime(1, 1, 1, 0, 0, 0)): # -> datetime() object
    """ returns initial passed time and a gigasecond (10^9 seconds) """
    time += timedelta(seconds = 10 ** 9)
    return time

## ------
## Command-line implementation
## ------
if __name__ == '__main__':
    from docopt import docopt

    print(docopt(__doc__))

'''
    # returns bash error on run
    start_time = docopt(__doc__)['<initial datetime object>']
    end_time = add_gigasecond(start_time)

    print("One gigasecond (10^9 seconds) from")
    print(" " * 5 + start_time.__str__())
    print("is")
    print(" " * 5 + end_time.__str__())
'''

"""
Exercism.io assignment - clock.py
Written by cmdellinger

Usage:
  None
  
Create a 24 hour Clock class that can add or subract minutes
"""

## ------
## Esxercism.io solution
## ------

class Clock:
    """ create a 24 hour clock that can add or subract minutes """

    # init and call behavior
    def __init__(self, hours, minutes):
        """ create list of hours and minutes changed to 24 hour time"""
        set_hr = (hours + int(minutes/60)) % 24
        if set_hr < 0:
            set_hr += 24
        set_min = minutes % 60
        if set_min < 0:
            set_min += 60
        self.time = [set_hr, set_min]

    def __str__(self):
        """ returns string of 24 clock time in XX:XX format """
        return str(self.time[0]).rjust(2, '0') + ":" + str(self.time[1]).rjust(2, '0')

    def __eq__(self, other):
        """ equal comparison of 24 hour clock time """
        return self.time == other.time

    def __ne__(self, other):
        """ not equal comparison of 24 hours clock time """
        return self.time != other.time

    # methods
    def add(self, minutes): # -> Clock
        """ returns clock with additional minutes """
        return Clock(self.time[0], self.time[1] + minutes)
    
    def subtract(self, minutes): # -> Clock
        """ returns clock minus minutes using add()"""
        add(-minutes)

## ------
## Command-line implementation
## ------

if __name__ == '__main__':
    print(__doc__)

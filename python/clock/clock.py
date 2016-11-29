"""
Exercism.io assignment - clock.py
Written by cmdellinger

Usage:
  None
  
Create a 24 hour Clock class that can add or subract minutes
"""

## ------
## import modules
## ------

# none

## ------
## function definitions
## ------

# none

## ------
## class definitions
## ------

class Clock:
    """ create a 24 hour clock that can add or subract minutes """

    # private functions
    def __clock_time(self, time = []): # -> Int [hours, minutes]
        """ expects list [hours, minutes] and returns 24 hr clock [hours, minutes] """
        # added vars for readability
        hours = time[0]
        minutes = time[1]
        
        set_hr = (hours + int(minutes/60)) % 24
        if set_hr < 0:
            set_hr += 24

        set_min = minutes % 60
        if set_min < 0:
            set_min += 60

        return [set_hr, set_min]

    def __clock_str(self, time = []): # -> String XX:XX
        """ takes time as [hours, minutes] and returns string XX:XX """
        # added vars for readability
        hours = time[0]
        minutes = time[1]
        
        return str(hours).rjust(2, '0') + ":" + str(minutes).rjust(2, '0')
    
    # init and call behavior
    def __init__(self, hours, minutes):
        """ create list of hours and minutes and change to 24 hour time"""
        self.time = [hours, minutes]
        self.time = self.__clock_time(self.time)

    def __str__(self):
        return self.__clock_str(self.time)

    def __eq__(self, other):
        """ compare 24 hour clock time """
        return self.time == other.time

    def __ne__(self, other):
        """ compare 24 hours clock time """
        return self.time != other.time

    # methods
    def add(self, minutes): # -> String (XX:XX)
        """ add minutes to time and return new 24 hour clock string in form XX:XX """
        self.time[1] += minutes
        self.time = self.__clock_time(self.time)
        return self.__clock_str(self.time)
    
    def subtract(self, minutes): # -> String (XX:XX)
        """ subtract minutes from time and return new 24 hour clock string in form XX:XX """
        self.time[1] -= minutes
        self.time = self.__clock_time(self.time)
        return self.__clock_str(self.time)

## ------
## main
## ------

if __name__ == '__main__':
    print(__doc__)

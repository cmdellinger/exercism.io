## exercism assignment:     clock.py
## description:
## use:
##
## written by (GitHub):     cmdellinger
## written on:              10.26.2016
## last revised:            10.31.2016

## ------
## module import calls
## ------

# none

## ------
## function definitions
## ------

# none

## ------
## class definitions
## ------

## ------
## class:       Clock
## purpose:     create a 24 hour clock that can add or subract minutes
## ------

class Clock:

    # helper functions
    def two_dig_str(self, x):
        if len(str(x)) < 2:
            return "0" + str(x)
        return str(x)

    def clock_time(self, hours, minutes):
        set_hr = (hours + int(minutes/60))%24
        if set_hr < 0:
            set_hr += 24

        set_min = minutes%60
        if set_min < 0:
            set_min += 60

        return self.two_dig_str(set_hr) + ":" + self.two_dig_str(set_min)
    
    # init and call behavior
    def __init__(self, hours, minutes):
        self.time = self.clock_time(hours, minutes)

    def __str__(self):
        return self.time

    def __repr__(self):
        return self.time

    def __eq__(self, other):
        return self.time == other.time

    def __ne__(self, other):
        return self.time != other.time

    # methods
    def add(self, minutes):
        self.time = self.clock_time(int(self.time[0:2]), int(self.time[3:]) + minutes)
        return self.time
    
    def subtract(self, minutes):
        self.time = self.clock_time(int(self.time[0:2]), int(self.time[3:]) - minutes)
        return self.time

## ------
## main
## ------

"""
Exercism.io assignment: robot_simulator.py
written by (GitHub):    cmdellinger
Python version:         2.7
    
Implementation of Robot class that moves a robot along coordinates according to
    a string of directions.
    
See README file for more detailed information.
"""

# Globals for the bearings
# Change the values as you see fit
EAST = (1,0)
NORTH = (0,1)
WEST = (-1,0)
SOUTH = (0,-1)

class Robot(object):
    ''' Robot class:
        functionality outlined in README
    '''
    
    BEARINGS = [NORTH, EAST, SOUTH, WEST]
    ''' list: bearings in compass order
        store bearings in compass order, so robot rotations can progress up and
            down the list.
    '''
    
    def __init__(self, bearing=NORTH, x=0, y=0):
        self.coordinates = (x,y)
        self.bearing = bearing

    def change_bearing(self, rotations = 0):
        ''' parent function for direction turns.
            rotates robot clockwise (+) and counterclockwise (-).
        '''
        current = self.BEARINGS.index(self.bearing)
        self.bearing = self.BEARINGS[(current + rotations) % 4]
        ''' modulus of calculated bearing accounts for index > 3.
            Python's negative index behavior allows for automatic wrap around.
        '''

    def turn_right(self, turns = 1):
        ''' rotates robot right or clockwise '''
        self.change_bearing(turns)

    def turn_left(self, turns = 1):
        ''' rotates robot left or counterclockwise '''
        self.change_bearing(-turns)

    def advance(self):
        ''' progresses robot in direction of bearing '''
        self.coordinates = tuple(x+y for x,y in zip(self.coordinates, self.bearing))

    def simulate(self, operations = ''):
        ''' translates string of instructions into movements '''
        instructions = {'R': self.turn_right,
                        'L': self.turn_left,
                        'A': self.advance}
        for operation in operations:
            instructions[operation]()

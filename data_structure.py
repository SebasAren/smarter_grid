# data_structure.py

import csv
import numpy as np
from binpackp import NumberBin, Fit

class Grid(object):

    # initialize the grid with a numpy 2d-array which consists of nodes 
    def __init__(self, x, y):
        matrix = [[Node() for i in range(x)] for j in range(y)]
        self.grid = np.array(matrix)


class Cable(object):
    def __init__(self, battery):

        # clockwise: 0 is up
        self.direction = {0: False, 1: False, 2: False, 3: False}
        self.battery = battery

    def add_direction(self, direction):
        self.direction[direction] = True

class Node(object):

# Grid point (if we decide to use this)
    def __init__(self):
        self.cable = []
        self.house = None
        self.battery = None

    def place_house(self, house):
        self.house = house

    def place_battery(self, battery):
        self.battery = battery

    def place_cable(self, cable):
        self.cable.append(cable)


class Battery(object):
    
    # battery has capacity, position and list of connected houses
    def __init__(self, x, y, capacity):
        self.id = None
        self.capacity_original = capacity
        self.capacity = capacity
        self.position = [x, y]
        self.houses = []

    def clear(self):
        self.capacity = self.capacity_original 
        self.houses = []

    # house should be a house object
    def c_house(self, house):
        self.houses.append(house)
        self.capacity -= house.power
        if self.capacity < 0:
            return False
        dis_x = abs(self.position[0] - house.position[0])
        dis_y = abs(self.position[1] - house.position[1])
        return dis_x + dis_y

    def dc_house(self, house):
        self.houses.remove(house)
        self.capacity += house.power
        dis_x = abs(self.position[0] - house.position[0])
        dis_y = abs(self.position[1] - house.position[1])
        return dis_x + dis_y

    def __repr__(self):
        return str(self.capacity_original)

class House(object):
    def __init__(self, x, y, power):
        self.position = (x, y)
        self.power = power

    def __repr__(self):
        return str(self.power)

# read data
def read_csv(f, house=False):
    reader = csv.reader(f)
    rv = []

    # skip headers
    next(reader, None)
    for row in reader:

        # create either a house or a battery
        if house:
            entry = House(int(row[0]), int(row[1]), float(row[2]))
        else:
            entry = Battery(int(row[0]), int(row[1]), float(row[2]))
        rv.append(entry)
    return rv

# this is mainly for testing purposes
if __name__ == '__main__':
    import sys

    # create a list of houses
    with open('data/{}_huizen.csv'.format(sys.argv[1])) as f:
        houses = read_csv(f, house=True)

    # and batteries
    with open('data/{}_batterijen.csv'.format(sys.argv[1])) as f:
        batteries = read_csv(f)

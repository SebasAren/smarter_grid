# data_structure.py

import csv
import numpy as np
from binpackp import NumberBin, Fit

class Grid(object):

    # initialize the grid with a numpy 2d-array which consists of nodes 
    def __init__(self, x, y):
        matrix = [[Node() for i in range(x)] for j in range(y)]
        self.grid = np.array(matrix)


    

class Node(object):
# grid point (if we decide to use this)
    def __init__(self, x, y):
        self.position = (x, y)
        self.capacity = 0
        self.structure = False
        self.connected_battery = None
        self.houses = []

    def place_house(self, house):
        self.structure = True
        self.capacity -= house.power
        self.houses.append(house)

    def place_battery(self, battery):
        self.structure = True
        self.capacity = battery.capacity
        self.connected_battery = battery.id

    def __repr__(self):
        return str(self.position)

    def connect_cable(self, cable):
        self.capacity = cable.capacity
        self.connected_battery = cable.connected_battery
        self.houses = cable.houses


class Battery(object):
    
    # battery has capacity, position and list of connected houses
    def __init__(self, x, y, capacity):
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

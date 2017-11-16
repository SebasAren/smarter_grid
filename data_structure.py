# data_structure.py

import csv
import numpy as np

class Grid(object):

    # initialize the grid with a numpy 2d-array which consists of nodes 
    def __init__(self, x, y):
        matrix = [[Node() for i in range(x)] for j in range(y)]
        self.grid = np.array(matrix)

    # path should be a list of consecutive directions
    # begin should be a list starting at a battery
    # TODO: Make it work when there is already a cable of the same battery
    def connect_nodes(self, begin, path):

        # first get a 'pointer' to the correct battery
        battery = self.grid[begin[0]][begin[1]].battery

        # go over all directions in the path
        for direction in path:

            # place cable at
            self.grid[begin[0]][begin[1]].place_cable(Cable(battery, direction))

            if direction == 0:
                begin[1] -= 1
            elif direction == 1:
                begin[0] += 1
            elif direction == 2:
                begin[1] += 1
            else:
                begin[0] -= 1


            if direction > 1:
                next_direction = direction - 2
            else: 
                next_direction = direction + 2

            self.grid[begin[0]][begin[1]].place_cable(Cable(battery, next_direction))


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


class Cable(object):
    def __init__(self, battery, direction):

        # clockwise: 0 is up
        self.directions = {0: False, 1: False, 2: False, 3: False}
        self.directions[direction] = True
        self.battery = battery

    def add_direction(self, direction):
        self.directions[direction] = True


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

if __name__ == '__main__':

    test = Grid(10, 10)
    test.connect_nodes()
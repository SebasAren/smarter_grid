# data_structure.py

import csv
import numpy as np

class Grid(object):

    # initialize the grid with a numpy 2d-array which consists of nodes 
    def __init__(self, x, y):
        matrix = [[Node() for i in range(x)] for j in range(y)]
        self.grid = np.array(matrix)

   
    def connect_nodes(self, x, y, direction):
        # create new cable object
        new_cable = Cable()
        self.grid[x][y].place_cable(new_cable)
        self.grid[x][y].cable[-1].directions[direction] = True

        # create cable object at neighbouring node
        # yes all these ifs are ugly but bear with me I'm trying
        if direction == 0:
            try:
                neighbour_cable = Cable()
                self.grid[x][y+1].place_cable(neighbour_cable)
                self.grid[x][y+1].cable[-1].directions[(direction + 2) % 4] = True
            except IndexError:
                pass

        elif direction == 1:
            try:
                neighbour_cable = Cable()
                self.grid[x+1][y].place_cable(neighbour_cable)
                self.grid[x+1][y].cable[-1].directions[(direction + 2) % 4] = True
            except IndexError:
                pass   

        elif direction == 2:
            try:
                neighbour_cable = Cable()
                self.grid[x][y-1].place_cable(neighbour_cable)
                self.grid[x][y-1].cable[-1].directions[(direction + 2) % 4] = True
            except IndexError:
                pass

        elif direction == 3:
            try:
                neighbour_cable = Cable()
                self.grid[x-1][y].place_cable(neighbour_cable)
                self.grid[x-1][y].cable[-1].directions[(direction + 2) % 4] = True
            except IndexError:
                pass
        


class Node(object):

# this is the object that is found on every grid point
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
    def __init__(self):

        # clockwise: 0 is up
        # every cable can only have one direction
        self.directions = {0: False, 1: False, 2: False, 3: False}
        self.battery = None

        def connect_battery(self, battery):
            self.battery = battery


class Battery(object):
    
    # battery has capacity, position and list of connected houses
    def __init__(self, x, y, capacity, i):
        self.id = i
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
    def __init__(self, x, y, power, i):
        self.id = i
        self.position = (x, y)
        self.power = power

    def __eq__(self, other):
        if isinstance(other, House):
            return self.power == other.power

    def __lt__(self, other):
        if isinstance(other, House):
            return self.power < other.power

    def __gt__(self, other):
        if isinstance(other, House):
            return self.power > other.power

    def __repr__(self):
        return str(self.power)

# read data
def read_csv(f, house=False):
    with open(f) as infile:
        reader = csv.reader(infile)
        rv = []

        # skip headers
        next(reader, None)
        for i, row in enumerate(reader):

            # create either a house or a battery
            if house:
                entry = House(int(row[0]), int(row[1]), float(row[2]), i)
            else:
                entry = Battery(int(row[0]), int(row[1]), float(row[2]), i)
            rv.append(entry)
        return rv

if __name__ == "__main__":
    grid = Grid(4,4)
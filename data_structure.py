# data_structure.py

import csv
import numpy as np
import networkx as nx

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
                self.grid[x][y+1].cable[-1].directions[2] = True
            except IndexError:
                self.grid[x][y].cable.pop(-1)
                pass

        elif direction == 1:
            try:
                neighbour_cable = Cable()
                self.grid[x+1][y].place_cable(neighbour_cable)
                self.grid[x+1][y].cable[-1].directions[3] = True
            except IndexError:
                self.grid[x][y].cable[-1].pop()
                pass   

        elif direction == 2:
            try:
                neighbour_cable = Cable()
                self.grid[x][y-1].place_cable(neighbour_cable)
                self.grid[x][y-1].cable[-1].directions[0] = True
            except IndexError:
                self.grid[x][y].cable[-1].pop()
                pass

        elif direction == 3:
            try:
                neighbour_cable = Cable()
                self.grid[x-1][y].place_cable(neighbour_cable)
                self.grid[x-1][y].cable[-1].directions[1] = True
            except IndexError:
                self.grid[x][y].cable[-1].pop()
                pass

    def calc_score(self):
    # intial score (not tested)
        score = 0

        for i in range(len(self.grid[0])):
            for j in range(len(self.grid)):
                if self.grid[i][j].battery != None:
                    score += 5000
                if self.grid[i][j].cable:
                    score += (9 * len(self.grid[i][j].cable)) / 2

        return score

class Node(object):

# this is the object that is found on every grid point
    def __init__(self, id):
        self.cable = []
        self.house = None
        self.battery = None 
        self.id = id

    def place_house(self, house):
        self.house = house

    def place_battery(self, battery):
        self.battery = battery

    def place_cable(self, cable):
        self.cable.append(cable)

    def __hash__(self):
        return hash(str(self.id))

    def __cmp__(self):
        if isinstance(other, Node):

            if self.id < other.id:
                return -1
            elif self.id == other.id:
                return 0
            else:
                return 1

        else:
            raise TypeError

    def __eq__(self):
        if isinstance(other, Node):
            if self.id == other.id:
                return True

            else:
                return False

        else:
            return False


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
    def __init__(self, x, y, capacity):
        self.capacity_original = capacity
        self.capacity = capacity
        self.position = [x, y]
        self.houses = []

    def give_id(self, i):
        self.id = i

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
        self.bat_id = 0

    def give_id(self, i):
        self.id = i


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

    def __add__(self, other):
        if isinstance(other, House):
            return self.power + other.power
        else:
            return self.power + other

# read data
def read_csv(f, house=False):
    with open(f) as infile:
        reader = csv.reader(infile)
        rv = []

        # skip headers
        next(reader, None)
        for row in reader:

            # create either a house or a battery
            if house:
                entry = House(int(row[0]), int(row[1]), float(row[2]))
                #entry.bat_id = int(row[3])
            else:
                entry = Battery(int(row[0]), int(row[1]), float(row[2]))
            rv.append(entry)
        return rv


# small grid for testing purposes only
# if __name__ == "__main__":
#     grid = Grid(4,4)
#     batt = Battery(2,2,150)
#     grid.grid[2][2].place_battery(batt)
#     house = House(3,3,50)
#     grid.grid[3][3].place_house(house)
# data_structure.py

import csv
import numpy as np
import matplotlib as plt
import sys


# https://stackoverflow.com/questions/8107313/isinstance-and-issubclass-behavior-differently
class Network(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return str(self.x) + " " + str(self.y)

    def distance(self, other):
        if isinstance(other, Network):
            return abs(self.x - other.x) + abs(self.y - other.y)
        if isinstance(other, House):
            return abs(self.x - other.x) + abs(self.y - other.y)
        else:
            raise TypeError


class Battery(object):
    
    # battery has capacity, position and list of connected houses
    def __init__(self, x, y, capacity):
        self.capacity_original = capacity
        self.capacity = capacity
        self.x = x
        self.y = y

    def give_id(self, i):
        self.id = i

    def __repr__(self):
        return str(self.capacity_original)

class House(object):
    def __init__(self, x, y, power):
        self.x = x
        self.y = y
        self.power = power
        self.bat_id = 0

    def give_id(self, i):
        self.id = i

    def distance(self, other):
        if isinstance(other, Network):
            return abs(self.x - other.x) + abs(self.y - other.y)
        if isinstance(other, House):
            return abs(self.x - other.x) + abs(self.y - other.y)
        else:
            raise TypeError

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
            else:
                entry = Battery(int(row[0]), int(row[1]), float(row[2]))
            rv.append(entry)
        return rv


# small grid for testing purposes only
if __name__ == "__main__":
    # make grid
    gridsize =  50

    gr = Graph(gridsize)

    nodelist = []
    for i in range(gridsize * gridsize):
        nodelist.append(Node(i))

    count = 0
    for x in range(gridsize):
        for y in range(gridsize):
            gr.add_nodes(x, y, nodelist[count])
            count += 1

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
        self.power = 0

    def distance(self, other):
        if isinstance(other, Network):
            return abs(self.x - other.x) + abs(self.y - other.y)
        else:
            raise TypeError

    def __repr__(self):
        return str(self.x) + " " + str(self.y)


    def __eq__(self, other):
        if isinstance(other, Network):
            return self.power == other.power

    def __lt__(self, other):
        if isinstance(other, Network):
            return self.power < other.power

    def __gt__(self, other):
        if isinstance(other, Network):
            return self.power > other.power

    def __repr__(self):
        return str(self.power)

    # def __add__(self, other):
    #     if isinstance(other, Network):
    #         return self.power + other.power
    #     elif isinstance(other, float):
    #         return self.power + other


class Battery(Network):
    
    # battery has capacity, position and list of connected houses
    def __init__(self, x, y, power):
        super().__init__(x, y)
        self.power = power
        self.capacity = power

    def give_id(self, i):
        self.id = i


class House(Network):
    def __init__(self, x, y, power):
        super().__init__(x, y)
        self.power = power

    def give_id(self, i):
        self.id = i

# read data
def read_csv(f, house=False):
    with open(f) as infile:
        reader = csv.reader(infile)
        rv = []

        # skip headers
        # next(reader, None)
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

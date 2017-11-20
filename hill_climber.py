# hill_climber.py

import data_structure
import numpy as np
import random

class ConstraintError(Exception):
    pass

def distance(pos1, pos2):
    return abs(pos1[0] - pos2[0]) + abs(pos1[1] - pos2[1])

# create a class for the Hill Climber
class HillClimber(object):
 
    def __init__(self, houses, batteries):
        self.houses = houses

        # lambda works like a JS 'callback' it returns a value buried 
        # within the data structure
        self.houses.sort(key = lambda x: x.power, reverse=True)

        self.batteries = batteries
        self.distance_houses = np.array([[distance(i.position, j.position) for\
            i in self.houses] for j in self.houses])

        # distance_batteries[battery][house]
        self.distance_batteries = np.array([[distance(i.position, j.position)\
            for i in self.houses] for j in self.batteries])

    def size_of_bin(self, bucket):
        rv = 0
        for el in bucket:
            rv += el.power
        return rv

    def contraint_check(self, bucket, b_type=0):
        if size_of_bin(bucket) > self.bin_size[b_type]:
            raise ConstraintError
        else:
            pass

    # function to start the optimization
    def first_fit(self):

        # define a bin_size (TODO: make it work with different batteries)
        self.bin_size = [self.batteries[0].capacity]

        # make a list of bins
        self.bins = [[] for i in range(len(self.batteries))]
        for house in self.houses:
            lowest = self.bin_size[0]
            for i, el in enumerate(self.bins):
                current = self.size_of_bin(el)
                if current < lowest:
                    lowest = current
                    bin_place = i
            self.bins[bin_place].append(house)


if __name__ == '__main__':
    CSV_HOUSES = 'data/wijk1_huizen.csv'
    CSV_BATTERIES = 'data/wijk1_batterijen.csv'

    houses = data_structure.read_csv(CSV_HOUSES, house=True)
    batteries = data_structure.read_csv(CSV_BATTERIES)

    hill = HillClimber(houses, batteries)
    hill.first_fit()
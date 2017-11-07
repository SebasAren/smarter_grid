# data_structure.py
import csv
from binpackp import NumberBin, Fit

class Grid(object):

    # potential matrix for a grid (unused thus far)
    def __init__(self, N, M):
        self.matrix = [[0 for i in range(M)] for j in range(N)]

class Battery(object):
    
    # battery has capacity, position and list of connected houses
    def __init__(self, x, y, capacity):
        self.capacity = capacity
        self.position = (x, y)
        self.houses = []

    # house should be a house object
    def connect_house(self, house):
        self.houses.append(house)
        self.capacity -= house.power

class House(object):

    # house has power and position
    def __init__(self, x, y, power):
        self.power = power
        self.position = (x, y)

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

    # define bin size for binpack module
    # multiplication is needed because of int requirement for bin packing
    # problem
    bin_size = int(batteries[0].capacity * 100000000)

    # create a list of houses to be fit
    fit_these = [int(house.power * 100000000) for house in houses]

    # get both results
    generic_results = Fit.fit(NumberBin, bin_size, fit_these)
    first_fit_results = Fit.ff(NumberBin, bin_size, fit_these)

    # print output
    print('General Function: ', generic_results)
    print('First Fit Function: ', first_fit_results)

    for el in first_fit_results._cache["bins"]:
        print(el)
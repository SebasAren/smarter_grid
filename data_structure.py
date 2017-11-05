# data_structure.py
import csv

class Grid(object):

    # potential matrix for a grid
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

    def __init__(self, x, y, power):
        self.power = power
        self.position = (x, y)

# read data
def read_csv(f, house=False):
    reader = csv.reader(f)
    rv = []
    for row in reader:
        if house:
            entry = House(int(row[0]), int(row[1]), float(row[2]))
        else:
            entry = Battery(int(row[0]), int(row[1]), float(row[2]))
        rv.append(entry)
    return rv

if __name__ == '__main__':
    
    # create a list of houses
    with open('data/wijk1_huizen.csv') as f:
        houses = read_csv(f, house=True)

    # and batteries
    with open('data/wijk1_batterijen.csv') as f:
        batteries = read_csv(f)

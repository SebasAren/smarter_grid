# data_structure.py
import csv

class Grid(object):

    # potential matrix for a grid
    def __init__(self, N, M):
        self.matrix = [[0 for i in range(M)] for j in range(N)]

class Battery(Grid):
    
    # battery has capacity, position and list of connected houses
    def __init__(self, capacity, position):
        self.capacity = capacity
        self.position = position
        self.houses = []

    # house should be a coordinate tuple
    def connect_house(self, house):
        self.houses.append(house)
        self.capacity -= house.capacity

class House(object):

    def __init__(self, x, y, power):
        self.power = power
        self.position = (x, y)

def read_houses(f):
    reader = csv.reader(f)
    houses = []
    for row in reader:
        house = House(row[0], row[1], row[2])
        houses.append(house)
    return houses

if __name__ == '__main__':
    
    # create a list of houses
    with open('data/wijk1_huizen.csv') as f:
        houses = read_houses(f)

    #print(houses)
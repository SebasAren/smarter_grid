# data_structure.py
import csv
import re

class Grid(object):

    # potential matrix for a grid
    def __init__(self, N, M):
        self.matrix = [[0 for i in range(M)] for j in range(N)]

class Battery(object):
    
    # battery has capacity, position and list of connected houses
    def __init__(self, capacity, x, y):
        self.capacity = capacity
        self.position = (x, y)
        self.houses = []

    # house should be a house object
    def connect_house(self, house):
        self.houses.append(house)
        self.capacity -= house.capacity

class House(object):

    def __init__(self, x, y, power):
        self.power = power
        self.position = (x, y)

# store batteries 
def read_batteries(f):
    batteries = []
    for row in f:
        x = int(re.sub("[^0-9]", "", row[:3]))
        y = int(re.sub("[^0-9]", "", row[5:9]))
        capacity = float(re.sub("[^0-9]", "", row[9:]))
        battery = Battery(capacity, x, y)
        batteries.append(battery)
    return batteries

# store houses
def read_houses(f):
    reader = csv.reader(f)
    houses = []
    for row in reader:
        house = House(int(row[0]), int(row[1]), float(row[2]))
        houses.append(house)
    return houses

if __name__ == '__main__':
    
    # create a list of houses
    with open('data/wijk1_huizen.csv') as f:
        houses = read_houses(f)

    with open('data/wijk1_batterijen.txt') as f:
        batteries = read_batteries(f)

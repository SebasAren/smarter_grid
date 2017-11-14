# data_structure.py
import csv
from binpackp import NumberBin, Fit


class Battery(object):
    
    # battery has capacity, position and list of connected houses
    def __init__(self, x, y, capacity):
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

class House(object):
    def __init__(self, x, y, power):
        self.position = (x, y)
        self.power = power

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

# class Cable(object):

#     # the amount of arguments gets ugly as hell quick
#     def __init__(self, x1, y1, x2, y2):

#         # if only points in grid can be accessed
#         self.position1 = [x1, y1]
#         self.position2 = [x2, y2]

#         # list of connected houses
#         self.houses = []
#         self.capacity = 0
#         self.connected = False
#         self.connected_battery = None

#     # battery should be battery object
#     def connect_battery(self, battery):
#         self.connected = True
#         self.connect_battery = battery
#         self.capacity = battery.capacity

#     # without this, it won't update when connecting a new house
#     def update_capacity(self, battery):
#         self.capacity = battery.capacity

#     # house should be a house object
#     def connect_house(self, house):
#         self.houses.append(house)
# data_structure.py

class Grid(object):
    
    # potential matrix for a grid
    def __init__(self, N, M):
        self.matrix = [[0 for i in range(M)] for j in range(N)]

class Battery(Grid):
    def __init__(self, capacity, position):
        self.capacity = capacity
        self.position = position
        self.houses = []

    def connect_house(self, house):
        self.houses.append(house)
        house.battery.append()
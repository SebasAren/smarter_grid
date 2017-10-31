# main.py

class House(object):
    def __init__(self, x, y, output):
        self.pos = (x, y)
        self.output = output

class Battery(object):
    def __init__(self, x, y, cap):
        self.pos = [x, y]
        self.capacity = cap

class Grid(Battery):
    def __init__(self, x, y):
        self.left = False
        self.up = False
        self.right = False
        self.down = False
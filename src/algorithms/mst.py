# minimum_tpanning_tree.py

import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.getcwd(), '.')))
sys.path.append(os.path.abspath(os.path.join(os.getcwd(), '..')))
from data_structure import Network
import csv

class Mst(object):
    def __init__(self, nodes):
        self.nodes = [nodes[i:i+1] for i in range(0, len(nodes), 1)]
        self.total_cost = 0
        self.lines = []

    def find_shortest_distance(self):
        shortest_distance = 10000
        shortest_pair = []

        for n, arr in enumerate(self.nodes):
            for m, item in enumerate(arr):
                for i in range(n + 1, len(self.nodes)):
                    for j, other_item in enumerate(self.nodes[i]):
                        dist = item.distance(other_item)
                        if dist <= shortest_distance:
                            shortest_distance = dist
                            shortest_pair = [(n, m), (i, j)]
        return (shortest_pair)

    def merge_networks(self, networkA, networkB, new_nodes):
        connected_list = []
        self.nodes[networkA[0]] = self.nodes[networkA[0]] + self.nodes[networkB[0]] + new_nodes
        self.nodes.pop(networkB[0])


    def create_path(self, begin_node, end_node):
        start = self.nodes[begin_node[0]][begin_node[1]]
        end = self.nodes[end_node[0]][end_node[1]]

        new_nodes = []
        width = start.x - end.x
        height = start.y - end.y
        length = abs(height) + abs(width)
        self.create_lines(start.x, start.y, end.x, end.y)

        if length < 1:
            return None

        # heuristics can be added here to decide wheter to equate x or y coordinates first
        else:
            self.equate_width(start, end, new_nodes)
            # print(new_nodes)
            self.equate_height(start, end, new_nodes)
            return new_nodes

    # lay cables untill target's x coordinate is reached
    def equate_width(self, start, end, new_nodes):

        width = start.x - end.x
        height = start.y - end.y
        length = abs(height) + abs(width)

        if width < 0:
            if abs(height) > 0:
                for i in range(1, abs(width) + 1):
                    new_nodes.append(Network((start.x + i), start.y))
            else:
                for i in range(1, abs(width)):
                    new_nodes.append(Network((start.x + i), start.y))

        elif width > 0:
            if abs(height) > 0:
                for i in range(1, abs(width) + 1):
                    new_nodes.append(Network((start.x - i), start.y))
            else:
                for i in range(1, abs(width)):
                    new_nodes.append(Network((start.x - i), start.y))

    # lay cables untill target's y coordinate is reached
    def equate_height(self, start, end, new_nodes):
        width = start.x - end.x
        height = start.y - end.y
        length = abs(height) + abs(width)

        if height < 0:
            for i in range(1, abs(height)):
                new_nodes.append(Network(end.x, (start.y + i)))
        elif height > 0:
            for i in range(1, abs(height)):
                new_nodes.append(Network(end.x, (start.y - i)))

    def randomize_direction(self):
        pass

    def run(self):
        while len(self.nodes) > 1:
            spots = self.find_shortest_distance()
            new_nodes = self.create_path(spots[0], spots[1])
            self.total_cost += len(new_nodes) + 1
            # print(self.total_cost)
            self.merge_networks(spots[0], spots[1], new_nodes)

    def create_lines(self, x_1, y_1, x_2, y_2):
        self.lines.append([(x_1, y_1), (x_2, y_1)])
        self.lines.append([(x_2, y_1), (x_2, y_2)])

# read data
def read_houses(f, house=False):
    with open(f) as infile:
        reader = csv.reader(infile)
        rv = [[],[],[],[],[]]

        # skip headers
        if not house:
            next(reader, None)
        for row in reader:
            entry = Network(int(row[0]), int(row[1]))
            battery = int(row[3])
            rv[battery].append(entry)
        return rv

def read_batteries(f, houses):
    with open(f) as infile:
        reader = csv.reader(infile)

        # skip headers
        next(reader, None)
        for i, row in enumerate(reader):
            houses[i].append(Network(int(row[0]), int(row[1])))
        return houses

# for test purposes only
if __name__ == "__main__":
    CSV_FILE_BATTERIES = '../../data/wijk1_batterijen.csv'
    CSV_FILE_HOUSES = '../../data/solutions/wijk1/solution_2952.csv'

    houses = read_houses(CSV_FILE_HOUSES, house=True)
    networklist = read_batteries(CSV_FILE_BATTERIES, houses)
    mst = Mst(networklist[0])
    mst.find_shortest_distance()
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

    def find_shortest_distance(self):
        shortest_distance = 10000
        shortest_pair = []

        for n, arr in enumerate(self.nodes):
            for m, item in enumerate(arr):
                for i in range(n + 1, len(self.nodes)):
                    for j, other_item in enumerate(self.nodes[i]):
                        dist = item.distance(other_item)
                        if dist < shortest_distance:
                            shortest_distance = dist
                            shortest_pair = [(n, m), (i, j)]
                            print(shortest_pair, shortest_distance)
        return (shortest_pair)

    def create_path(self, begin_node, end_node):
        start = self.nodes[begin_node[0]][begin_node[1]]
        end = self.nodes[end_node[0]][end_node[1]]

        new_nodes = []
        width = start.x - end.x
        height = start.y - end.y
        length = abs(height) + abs(width)

        if length < 1:
            return None

        if width < 0:
            if abs(height) > 0:
                for i in range(abs(width)):
                    new_nodes.append(Network((start.x + i), start.y))
            else:
                for i in range(abs(width) - 1):
                    new_nodes.append(Network((start.x + i), start.y))

        elif width > 0:
            if abs(height) > 0:
                for i in range(abs(width)):
                    new_nodes.append(Network((start.x - i), start.y))
            else:
                for i in range(abs(width) - 1):
                    new_nodes.append(Network((start.x - i), start.y))


        if height < 0:
            for i in range(abs(height) - 1):
                new_nodes.append(Network(end.x, (start.y + i)))
        elif height > 0:
            for i in range(abs(height) - 1):
                new_nodes.append(Network(end.x, (start.y - i)))

        return new_nodes

    def randomize_direction(self):
        pass

    def run(self):
        while len(self.nodes) > 1:
            spots = self.find_shortest_distance()
            new_nodes = self.create_path(spots[0], spots[1])
            self.merge_networks(spots[0], spots[1], new_nodes)


# read data
def read_csv(f, house=False):
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

    houses = read_csv(CSV_FILE_HOUSES, house=True)
    networklist = read_batteries(CSV_FILE_BATTERIES, houses)
    mst = Mst(networklist[0])
    mst.find_shortest_distance()
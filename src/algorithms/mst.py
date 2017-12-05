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


    def find_shortest_path(self):
        """
        Find shortest distance between network elements from different 
        sub-networks.

        These will then be used to merge them. 
        """
        pass

    def merge_networks(self):
        """
        Merge the network lists together.
        """

        pass

    def create_path(self):
        pass

    def randomize_direction(self):
        pass

    def run(self):
        pass

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
	CSV_FILE_HOUSES = '../../data/solutions/wijk1/solution_2587.csv'

	houses = read_csv(CSV_FILE_HOUSES, house=True)
	networklist = read_batteries(CSV_FILE_BATTERIES, houses)
	print(networklist)
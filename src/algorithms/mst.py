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


# read data
def read_csv(f, house=False):
    with open(f) as infile:
        reader = csv.reader(infile)
        rv = []

        # skip headers
        if not house:
	        next(reader, None)
        for row in reader:
            entry = Network(int(row[0]), int(row[1]))
            rv.append(entry)
        print(rv)
        return rv

# for test purposes only
if __name__ == "__main__":
	CSV_FILE_BATTERIES = '../../data/wijk1_batterijen.csv'
	CSV_FILE_HOUSES = '../../data/solutions/wijk1/solution_2587.csv'

	houses = read_csv(CSV_FILE_HOUSES, house=True)
	batteries = read_csv(CSV_FILE_BATTERIES)

	# variables to store coördinates
	x_houses= []
	y_houses=[]
	x_batteries=[]
	y_batteries=[]
# main.py


import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.getcwd(), '.')))
sys.path.append(os.path.abspath(os.path.join(os.getcwd(), '/algorithms')))

from itertools import combinations, chain
from data_structure import Battery, House, read_csv
# from propagation import Propagation
# from hill_climber import HillClimber
# from mst import Mst
from algorithms.simanneal import SimAnneal

WIDTH = 1
HEIGHT = 2

def create_file_path(i, type):
    return '../data/wijk{}_{}.csv'.format(i, type)



if __name__ == '__main__':

    if sys.argv[1] == 'climber':
        houses = read_csv(create_file_path(sys.argv[2], 'huizen'), house=True)
        batteries = read_csv(create_file_path(sys.argv[2], 'batterijen'))
        val = hill.climbing()
        hill.write_solution(hill.bins, val)
        solutions.append(val)

    elif sys.argv[1] == 'sim':
        houses = read_csv(create_file_path(sys.argv[2], 'huizen'), house=True)
        batteries = read_csv(create_file_path(sys.argv[2], 'batterijen'))
        anneal = SimAnneal(houses, batteries, sys.argv[2], cooling=sys.argv[3], max_iter=int(sys.argv[4]))
        try:
            anneal.anneal()
        finally:
            anneal.plot_visualization()
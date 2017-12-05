# main.py


import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.getcwd(), '.')))
sys.path.append(os.path.abspath(os.path.join(os.getcwd(), '/algorithms')))

from itertools import combinations, chain
from data_structure import Battery, House, read_csv
from algorithms.propagation import Propagation
from algorithms.hill_climber import HillClimber
from algorithms.mst import Mst, read_houses, read_batteries

WIDTH = 1
HEIGHT = 2


if __name__ == '__main__':

    # create a list of houses and batteries
    CSV_HOUSES = '../data/wijk1_huizen.csv'
    CSV_BATTERIES = '../data/wijk1_batterijen.csv'

    CSV_FILE_BATTERIES = '../data/wijk1_batterijen.csv'
    CSV_FILE_HOUSES = '../data/solutions/wijk1/solution_2952.csv'



    if sys.argv[1] == 'propagation':
        houses = read_csv(CSV_HOUSES, house=True)
        batteries = read_csv(CSV_BATTERIES)
        propagator = Propagation(houses, batteries, climbers=2)
        propagator.short_sequence(10)

    elif sys.argv[1] == 'climber':
        houses = read_csv(CSV_HOUSES, house=True)
        batteries = read_csv(CSV_BATTERIES)
        hill = HillClimber(houses, batteries)
        val = hill.climbing()
        hill.write_solution(hill.bins, val)
        solutions.append(val)
        
    elif sys.argv[1] == 'mst':
        houses = read_houses(CSV_FILE_HOUSES, house=True)
        networklist = read_batteries(CSV_FILE_BATTERIES, houses)
        mst = []
        for network in networklist: 
            mst.append(Mst(network))
            mst[-1].run()
            print(mst[-1].nodes)
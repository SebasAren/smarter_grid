# main.py


import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.getcwd(), '.')))
sys.path.append(os.path.abspath(os.path.join(os.getcwd(), '/algorithms')))

from itertools import combinations, chain
from data_structure import Battery, House, read_csv
from algorithms.propagation import Propagation
from algorithms.hill_climber import HillClimber

WIDTH = 1
HEIGHT = 2


if __name__ == '__main__':

    # create a list of houses and batteries
    CSV_HOUSES = '../data/wijk1_huizen.csv'
    CSV_BATTERIES = '../data/wijk1_batterijen.csv'

    houses = read_csv(CSV_HOUSES, house=True)
    batteries = read_csv(CSV_BATTERIES)

    if sys.argv[1] == 'propagation':
        propagator = Propagation(houses, batteries, climbers=2)
        propagator.short_sequence(10)

    elif sys.argv[1] == 'climber':
        hill = HillClimber(houses, batteries)
        val = hill.climbing()
        hill.write_solution(hill.bins, val)
        solutions.append(val)
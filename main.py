# main.py

from data_structure import Battery, House, read_csv
from itertools import combinations, chain
import data_generator
import hill_climber

WIDTH = 1
HEIGHT = 2


if __name__ == '__main__':
    import sys

    # create a list of houses and batteries
    houses = read_csv('data/{}_huizen.csv'.format(sys.argv[1]), house=True)
    batteries = read_csv('data/{}_batterijen.csv'.format(sys.argv[1]))

    if sys.argv[2] == 'hillclimber':
        hill = hill_climber.HillClimber(houses, batteries)
        hill.first_fit()
        tries = 0
        while tries < 10000:
            if not hill.swap_houses():
                tries += 1
            else:
                tries = 0
                print(hill.cost_values)
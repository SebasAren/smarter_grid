# main.py

from data_structure import Battery, House, read_csv
import data_generator
from itertools import combinations, chain

WIDTH = 1
HEIGHT = 2

def brute_force_solution(houses, batteries):
    cost = 0
    best_cost = 0


    for el in [x for l in range(1, len(houses) + 1) for x in combinations(houses, l)]:
        


if __name__ == '__main__':
    import sys

    # create a list of houses
    with open('data/test_wijk/{}_huizen.csv'.format(sys.argv[1])) as f:
        houses = read_csv(f, house=True)

    # and batteries
    with open('data/test_wijk/{}_batterijen.csv'.format(sys.argv[1])) as f:
        batteries = read_csv(f)

    # print(houses)
    # print(batteries)

    brute_force_solution(houses, batteries)
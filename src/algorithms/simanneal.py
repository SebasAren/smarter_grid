import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.getcwd(), '.')))
sys.path.append(os.path.abspath(os.path.join(os.getcwd(), '..')))

import math
from hill_climber import HillClimber
from mst import Mst
import data_structure
import numpy as np
import random
import csv
import copy
import itertools

class SimAnneal(HillClimber):

    def __init__(self, houses, batteries):
        super().__init__(houses, batteries)
        self.temperature = 10000
        self.cooling_rate = 5
        self.best = []


    def acceptance(self, new_value, old_value, ):
        if new_value < old_value:
            return 1.0

        # print(old_value - new_value)

        return math.exp((new_value - old_value) / self.temperature) - 1

    def mst_check(self, bin_1, bin_2):
        mst1 = Mst(self.bins[bin_1])
        mst2 = Mst(self.bins[bin_2])
        mst1.run()
        mst2.run()
        rv = mst1.total_cost + mst2.total_cost
        return mst1, mst2

    def climbing(self):
        for el in self.bins:
            mst = Mst(el)
            mst.run()
            self.best.append(mst)

        current = copy.copy(self.best)

        while self.temperature > 0:
            swap = self.pick_swap()
            
            old_value = current[swap[1]].total_cost + current[swap[3]].total_cost

            # print(old_value)
            self.swap_houses(swap[0], swap[1], swap[2], swap[3])

            if not self.constraint_check(self.bins[swap[1]]) or not self.constraint_check(self.bins[swap[3]]):
                self.swap_houses(swap[0], swap[1], swap[2], swap[3])

            else:
                solutions = self.mst_check(swap[1], swap[3])
                new_value = solutions[0].total_cost + solutions[1].total_cost

                chance = self.acceptance(new_value, old_value)
                self.temperature -= self.cooling_rate
                if chance >= random.random():
                    print(self.temperature, chance)
                    current[swap[1]] = solutions[0]
                    current[swap[3]] = solutions[1]
                    total_best = 0
                    total_current = 0
                    for i, el in enumerate(current):
                        total_current += el.total_cost
                        total_best += self.best[i].total_cost

                        
                else:
                    self.swap_houses(swap[0], swap[1], swap[2], swap[3])

if __name__ == '__main__':

    CSV_HOUSES = '../../data/wijk1_huizen.csv'
    CSV_BATTERIES = '../../data/wijk1_batterijen.csv'

    houses = data_structure.read_csv(CSV_HOUSES, house=True)
    batteries = data_structure.read_csv(CSV_BATTERIES)

    solutions = []
    for i in range(1):
        hill = SimAnneal(houses, batteries)
        val = hill.climbing()
        # hill.write_solution(hill.bins, val)
        # solutions.append(val)

    # print(solutions)
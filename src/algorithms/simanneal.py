import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.getcwd(), '.')))
sys.path.append(os.path.abspath(os.path.join(os.getcwd(), '..')))

import math
from hill_climber import HillClimber
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


    def acceptance(self, new_value, old_value, ):
        if new_value < old_value:
            return 1.0

        # print(old_value - new_value)

        return math.exp((new_value - old_value) / self.temperature) - 1

    def climbing(self):

        while self.temperature > 0:
            swap = self.pick_swap()
            
            old_value = self.mean_distance_check(self.bins[swap[1]], swap[1]) + self.mean_distance_check(self.bins[swap[3]], swap[3])
            # print(old_value)

            self.swap_houses(swap[0], swap[1], swap[2], swap[3])

            if not self.constraint_check(self.bins[swap[1]]) or not self.constraint_check(self.bins[swap[3]]):
                self.swap_houses(swap[0], swap[1], swap[2], swap[3])

            else:
                new_value = self.mean_distance_check(self.bins[swap[1]], swap[1]) +self.mean_distance_check(self.bins[swap[3]], swap[3])
                
                chance = self.acceptance(new_value, old_value)
                if chance >= random.random():
                    self.temperature -= self.cooling_rate
                    print(self.temperature, chance)
                else:
                    self.temperature -= self.cooling_rate
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
        hill.write_solution(hill.bins, val)
        solutions.append(val)

    print(solutions)
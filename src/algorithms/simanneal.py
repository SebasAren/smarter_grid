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
import matplotlib.pyplot as plt
from visualizations.cable_vis import CableVis


class SimAnneal(HillClimber):
    """
    Simulated annealing algorithm using the hill climber and the 'mst' greedy
    algorithm. 
    """

    def __init__(self, houses, batteries, temperature=1000, max_iter=10000):
        """
        
        """
        super().__init__(houses, batteries)
        self.temperature = temperature
        self.begin_temp = temperature
        self.best = []
        self.max_iter = max_iter
        self.x = []
        self.y = []

    def acceptance(self, new_value, old_value):
        if new_value < old_value:
            return 1.0

        return math.exp( -abs(new_value - old_value) / self.temperature)

    def dampened_cooling(self, i):

        iter_count = i / 10000

        self.temperature = self.begin_temp * math.exp(-iter_count) * math.cos(iter_count * 10) ** 2

    def mst_check(self, bin_1, bin_2):
        mst1 = Mst(self.bins[bin_1])
        mst2 = Mst(self.bins[bin_2])
        mst1.run()
        mst2.run()
        rv = mst1.total_cost + mst2.total_cost
        return mst1, mst2

    def anneal(self):
        for el in self.bins:
            mst = Mst(el)
            mst.run()
            self.best.append(mst)

        current = copy.copy(self.best)
        for iter_count in range(self.max_iter):
            swap = self.pick_swap()
            old_value = current[swap[1]].total_cost + current[swap[3]].total_cost
            self.swap_houses(swap[0], swap[1], swap[2], swap[3])

            # if not self.constraint_check(self.bins[swap[1]]) or not self.constraint_check(self.bins[swap[3]]):
            if not True:
                self.swap_houses(swap[0], swap[1], swap[2], swap[3])

            else:
                solutions = self.mst_check(swap[1], swap[3])
                new_value = solutions[0].total_cost + solutions[1].total_cost

                chance = self.acceptance(new_value, old_value)

                self.dampened_cooling(iter_count)

                # self.temperature = self.begin_temp / math.log1p(iter_count * 4)
                
                # self.temperature = self.begin_temp *  (1 / self.begin_temp ** (iter_count / self.max_iter))

                # self.temperature = self.begin_temp * 0.999 ** iter_count

                if chance >= random.random():
                    print(self.temperature, chance)
                    current[swap[1]] = solutions[0]
                    current[swap[3]] = solutions[1]
                    self.total_best = 0
                    total_current = 0
                    for i, el in enumerate(current):
                        total_current += el.total_cost
                        self.total_best += self.best[i].total_cost

                    if total_current <= self.total_best:
                        print(total_current)
                        self.best = copy.copy(current)
                        self.total_best = total_current
                else:
                    self.swap_houses(swap[0], swap[1], swap[2], swap[3])

                self.x.append(iter_count)
                y = 0
                for el in current:
                    y += el.total_cost
                self.y.append(y)

    def plot_result(self):
        plt.plot(self.x, self.y)
        plt.show()

    def plot_visualization(self, i=0):
        lines = []
        for el in self.best:
            lines.append(el.lines)
        self.vis = CableVis(lines, self.houses)
        self.vis.plot()
        self.vis.save_plot(i, 'damp', self.total_best)


if __name__ == '__main__':

    CSV_HOUSES = '../../data/wijk3_huizen.csv'
    CSV_BATTERIES = '../../data/wijk3_batterijen.csv'
    CSV_FILE_HOUSES = '../../data/solutions/wijk1/solution_2752.csv'

    houses = data_structure.read_csv(CSV_HOUSES, house=True)
    batteries = data_structure.read_csv(CSV_BATTERIES)

    solutions = []

    hill = SimAnneal(houses, batteries, temperature=10, max_iter=55000)
    try:
        hill.anneal()
    finally:
        hill.plot_visualization()

# simanneal.py

import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.getcwd(), '.')))
sys.path.append(os.path.abspath(os.path.join(os.getcwd(), '..')))

# import libraries
import math
from algorithms.hill_climber import HillClimber
from algorithms.mst import Mst
import data_structure
import random
import csv
import copy
import itertools
import matplotlib.pyplot as plt
import pylab as pl
from visualizations.cable_vis import CableVis


class SimAnneal(HillClimber):
    """
    Simulated annealing algorithm using the hill climber and the 'mst' greedy
    algorithm. 
    
    """

    def __init__(self, houses, batteries, wijk, temperature=10, max_iter=10000, cooling='lineair', interest=0.99):

        # create HillClimber
        super().__init__(houses, batteries)

        # set temps and max iterations
        self.temperature = temperature
        self.begin_temp = temperature
        self.max_iter = max_iter

        # create container for best MST objects
        self.best = []

        # used for later plot of variance
        self.x = []
        self.y = []

        # variables for plot
        self.cooling = cooling
        self.wijk = wijk

        # interest value for the interest cooling
        self.interest = interest

    def acceptance(self, new_value, old_value):
        """
        Acceptation chance for the simulated annealing algorithm.

        Variables:
        new_value = new value from hill climber
        old_value = old value from hill climber
        
        """

        if new_value < old_value:
            return 1.0

        return math.exp( -abs(new_value - old_value) / self.temperature)

    def hill_acceptance(self, new_value, old_value):
        if new_value < old_value:
            return 1.0
        else:
            return 0.0

    def lin_cooling(self, i):
        """
        Linear cooling scheme.

        Variables:
        i: number of iterations.
        
        """
        self.temperature = self.begin_temp - (i / self.max_iter) * self.begin_temp

    def damped_cooling(self, i):
        """
        "Damped oscillator" cooling scheme.

        Variables:
        i: number of iterations.
        
        """
        iter_count = i / 10000
        self.temperature = self.begin_temp * math.exp(-iter_count) * \
        math.cos(iter_count * 10) ** 2

    def log1p_cooling(self, i):
        """
        Logarithmic cooling scheme.

        Variables:
        i: number of iterations.
        
        """
        self.temperature = self.begin_temp / math.log1p(i * 4 + 1)

    def interest_cooling(self, i):
        """
        Exponential cooling scheme.

        Variables:
        i: number of iterations.
        
        """
        self.temperature = self.begin_temp * self.interest ** i

    def cool_choose(self, i):
        """
        Function to choose the cooling scheme needed based on user input.

        Variables:
        i: number of iterations.
        
        """
        if self.cooling == 'interest':
            self.interest_cooling(i)
        if self.cooling == 'ln':
            self.log1p_cooling(i)
        if self.cooling == 'damp':
            self.damped_cooling(i)
        if self.cooling == 'lin':
            self.lin_cooling(i)

    def mst_check(self, bin_1, bin_2):
        """
        Calculates score based on the MST algorithm.

        Variables:
        bin_1: network index.
        bin_2: network index.
        
        """
        
        mst1 = Mst(self.bins[bin_1])
        mst2 = Mst(self.bins[bin_2])
        mst1.run()
        mst2.run()
        rv = mst1.total_cost + mst2.total_cost
        return mst1, mst2

    def anneal(self):
        """
        This is the actual method to run the anealing process.
        
        """

        # determine score of first/random fit
        for el in self.bins:
            mst = Mst(el)
            mst.run()
            self.best.append(mst)

        # copy the best to the current to get started
        current = copy.copy(self.best)
        for iter_count in range(self.max_iter):

            # pick houses to try an swap
            swap = self.pick_swap()

            # get the old vlaue of those networks
            old_value = current[swap[1]].total_cost + current[swap[3]].total_cost

            # swap the the houses
            self.swap_houses(swap[0], swap[1], swap[2], swap[3])

            # check the constraints and swap back houses to the previous state if constraints failed
            if not self.constraint_check(self.bins[swap[1]]) or not \
            self.constraint_check(self.bins[swap[3]]):
                self.swap_houses(swap[0], swap[1], swap[2], swap[3])

            else:

                # calc new score and save it
                solutions = self.mst_check(swap[1], swap[3])
                new_value = solutions[0].total_cost + solutions[1].total_cost

                if sys.argv[1] == 'sim':

                    # calculate acceptance chance
                    chance = self.acceptance(new_value, old_value)

                    # cool the temperature of the annealing process
                    self.cool_choose(iter_count)
                elif sys.argv[1] == 'hill':

                    # returns 1 or 0 if better or worse
                    chance = self.hill_acceptance(new_value, old_value)

                # if change accepted
                if chance >= random.random():

                    # print some information
                    print(iter_count, self.temperature, chance)

                    # set new values for current state
                    current[swap[1]] = solutions[0]
                    current[swap[3]] = solutions[1]

                    # calculate new scores
                    self.total_best = 0
                    total_current = 0
                    for i, el in enumerate(current):
                        total_current += el.total_cost
                        self.total_best += self.best[i].total_cost

                    # make changes if new found value is actual best so far
                    if total_current <= self.total_best:
                        print(total_current) # print new best value
                        self.best = copy.copy(current)
                        self.total_best = total_current
                else:

                    # swap back if not accepted
                    self.swap_houses(swap[0], swap[1], swap[2], swap[3])

                # save data for plot
                self.x.append(iter_count)
                y = 0
                for el in current:
                    y += el.total_cost
                self.y.append(y)


    # not working at the moment, should return a plot of current value vs iterations
    def plot_result(self):
        plt.plot(self.x, self.y)
        pl.savefig('../sim_plots/{}_{}_{}.png'.format(self.max_iter, self.cooling, self.total_best))

    def plot_visualization(self):
        """
        Visualization of the end result.
        
        """
        
        lines = []
        for el in self.best:
            lines.append(el.lines)
        self.vis = CableVis(lines, self.houses)
        self.vis.plot()
        self.vis.save_plot(self.max_iter, self.cooling, self.total_best, self.wijk)
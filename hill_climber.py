# hill_climber.py

import data_structure
import numpy as np
import random
import csv

# custom error for contraint checking
class ConstraintError(Exception):
    pass

# manhattan distance between 2 tuples/lists
def distance(pos1, pos2):
    return abs(pos1[0] - pos2[0]) + abs(pos1[1] - pos2[1])

# create a class for the Hill Climber
class HillClimber(object):
 
    def __init__(self, houses, batteries):

        # init cost list for later price checking
        self.cost_values = np.array([0 for i in range(len(batteries))])
        self.houses = houses

        # lambda works like a JS 'callback' it returns a value buried 
        # within the data structure
        self.houses.sort(key = lambda x: x.power, reverse=True)
        self.houses = np.array(self.houses)

        # give houses id's
        for i, house in enumerate(self.houses):
            house.give_id(i)

        # give batteries id's
        self.batteries = np.array(batteries)
        for j, battery in enumerate(self.batteries):
            battery.give_id(j)

        # set distance of houses to other houses (house.id is index)
        self.distance_houses = np.array([[distance(i.position, j.position) for\
            i in self.houses] for j in self.houses])

        # distance_batteries[battery.id][house.id]
        self.distance_batteries = np.array([[distance(i.position, j.position)\
            for i in self.houses] for j in self.batteries])


    # check total value inside bin
    def size_of_bin(self, bucket):
        rv = 0
        for el in bucket:
            rv += el.power
        return rv

    # check contstraint
    def constraint_check(self, bucket, b_type=0):
        if self.size_of_bin(bucket) > self.bin_size[b_type]:
            raise ConstraintError
        else:
            pass

    def mean_distance_check(self, bucket, battery_id):
        cost_values = 0
        for i, house in enumerate(bucket):
            total_house = self.distance_batteries[battery_id][house.id]
            for count, j in enumerate(range(i + 1, len(bucket))):
                total_house += self.distance_houses[house.id][bucket[j].id]
            cost_values += total_house / (count + 1)
        return cost_values




    # check the total minimum distance of a bin
    def distance_check(self, bucket, battery_id):
        cost_values = 0
        for i, house in enumerate(bucket):
            smallest = self.distance_batteries[battery_id][house.id]
            for j in range(i + 1, len(bucket)):
                if self.distance_houses[house.id][bucket[j].id] < smallest:
                    smallest = self.distance_houses[house.id][bucket[j].id]
            cost_values += smallest
        return cost_values

    def swap_houses(self):
        bin_1 = random.randrange(len(self.bins))
        bin_2 = bin_1
        while bin_2 == bin_1:
            bin_2 = random.randrange(len(self.bins))

        house_1 = random.randrange(len(self.bins[bin_1]))
        house_2 = random.randrange(len(self.bins[bin_2]))        

        # swap houses
        self.bins[bin_1][house_1], self.bins[bin_2][house_2] = self.bins[bin_2][house_2], self.bins[bin_1][house_1]

        # check constraints, else swap them back and break function
        try:
            self.constraint_check(self.bins[bin_1])
            self.constraint_check(self.bins[bin_2])
        except ConstraintError:
            self.bins[bin_1][house_1], self.bins[bin_2][house_2] = self.bins[bin_2][house_2], self.bins[bin_1][house_1]
            return False

        check_1 = self.mean_distance_check(self.bins[bin_1], bin_1)
        check_2 = self.mean_distance_check(self.bins[bin_2], bin_2)
        if (check_1 + check_2) < (self.cost_values[bin_1] + self.cost_values[bin_2]):
            self.cost_values[bin_1] = check_1
            self.cost_values[bin_2] = check_2
            return True
        else:
            self.bins[bin_1][house_1], self.bins[bin_2][house_2] = self.bins[bin_2][house_2], self.bins[bin_1][house_1]
            return False


    # function to start the optimization
    def first_fit(self):

        # define a bin_size (TODO: make it work with different batteries)
        self.bin_size = [self.batteries[0].capacity]

        # make a list of bins
        self.bins = [[] for i in range(len(self.batteries))]
        try:
            for house in self.houses:
                lowest = self.bin_size[0]
                for i, el in enumerate(self.bins):
                    current = self.size_of_bin(el)
                    if current < lowest:
                        lowest = current
                        bin_place = i
                self.bins[bin_place].append(house)
                self.constraint_check(self.bins[bin_place])
        except ConstraintError:
            exit('First fit failed!')

        self.bins = np.array(self.bins)
        for i, el in enumerate(self.bins):
            self.cost_values[i] = self.mean_distance_check(el, i)

    # run the simulation iterations times and save best values
    def run_simulation(self, iterations=25, best_value=10000):
        best_solution = []
        for i in range(iterations):
            self.first_fit()
            tries = 0
            while tries < 10000:
                if not self.swap_houses():
                    tries += 1
                else:
                    tries = 0
            current = 0
            for el in self.cost_values:
                current += el
            if current < best_value:
                best_value = current
                best_solution = self.bins
                self.write_solution(best_solution, best_value)
            print('Iteration count: {} of {}.'.format(i + 1, iterations))

    # save the solution to a csv
    def write_solution(self, best_solution, best_value):
        with open('data/solutions/wijk1/solution_{}.csv'.format(best_value), 'a') as outfile:
            writer = csv.writer(outfile)
            for i, el in enumerate(best_solution):
                for row in el:
                    writer.writerow([row.position[0], row.position[1], row.power, i])



if __name__ == '__main__':

    CSV_HOUSES = 'data/wijk1_huizen.csv'
    CSV_BATTERIES = 'data/wijk1_batterijen.csv'

    houses = data_structure.read_csv(CSV_HOUSES, house=True)
    batteries = data_structure.read_csv(CSV_BATTERIES)

    hill = HillClimber(houses, batteries)
# hill_climber.py

import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.getcwd(), '.')))
sys.path.append(os.path.abspath(os.path.join(os.getcwd(), '..')))

import data_structure
import numpy as np
import random
import csv
import copy
import itertools


TRIES = 100
# custom error for contraint checking
class FitError(Exception):
    pass

# manhattan distance between 2 tuples/lists
def distance(pos1, pos2):
    return abs(pos1[0] - pos2[0]) + abs(pos1[1] - pos2[1])

# create a class for the Hill Climber
class HillClimber(object):

    # global
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

        # define a bin_size (TODO: make it work with different batteries)
        self.bin_size = [self.batteries[0].capacity]
        while True:
            try:
                self.bins = self.random_fit()
                break
            except FitError:
                pass

        for i, el in enumerate(self.bins):
            self.cost_values[i] = self.mean_distance_check(el, i)



    # check total value inside bin
    def size_of_bin(self, bucket):
        rv = 0
        for el in bucket:
            rv += el.power
        return rv

    # check contstraint
    def constraint_check(self, bucket, b_type=0):
        if self.size_of_bin(bucket) > self.bin_size[b_type]:
            return False
        else:
            return True

    def mean_distance_check(self, bucket, battery_id):
        cost = 0
        for i, house in enumerate(bucket):
            total_house = self.distance_batteries[battery_id][house.id]
            for count, j in enumerate(range(i + 1, len(bucket))):
                total_house += self.distance_houses[house.id][bucket[j].id]
            cost += total_house / (count + 1)
        
        return cost

    # check the total minimum distance of a bin, NIET GEBRUIKT
    def distance_check(self, bucket, battery_id):
        cost_values = 0
        for i, house in enumerate(bucket):
            smallest = self.distance_batteries[battery_id][house.id]
            for j in range(i + 1, len(bucket)):
                if self.distance_houses[house.id][bucket[j].id] < smallest:
                    smallest = self.distance_houses[house.id][bucket[j].id]
            cost_values += smallest
        return cost_values

    
    def improvement_check(self, bin_1, bin_2):    
         
        # check if distance decreases
        check_1 = self.mean_distance_check(self.bins[bin_1], bin_1)
        check_2 = self.mean_distance_check(self.bins[bin_2], bin_2)
        
        if (check_1 + check_2) < (self.cost_values[bin_1] + self.cost_values[bin_2]):
            self.cost_values[bin_1] = check_1
            self.cost_values[bin_2] = check_2
            return True
        else:
            return False

    def pick_swap(self):
        # pick random houses to swap 
        bin_1 = random.randrange(len(self.bins))
        bin_2 = bin_1
        while bin_2 == bin_1:
            bin_2 = random.randrange(len(self.bins))

        house_1 = random.randrange(len(self.bins[bin_1]))
        house_2 = random.randrange(len(self.bins[bin_2]))        

        return house_1, bin_1, house_2, bin_2
        
    def try_loose_swap(self, house_1, bin_1, house_2, bin_2):

        self.swap_houses(house_1, bin_1, house_2, bin_2)
        if self.improvement_check(bin_1, bin_2):
            for el in range(len(self.bins)):
                if self.constraint_check(self.bins[el]):
                    self.swap_houses(house_1, bin_1, house_2, bin_2)
                    return False
            return True
        else:
            return False

            

    def try_swap(self, house_1, bin_1, house_2, bin_2):
        self.swap_houses(house_1, bin_1, house_2, bin_2)

        # dit stuk bij constraints check 
        # check constraints, else swap them back and break function
        if self.constraint_check(self.bins[bin_1]) == True and self.constraint_check(self.bins[bin_2]) == True:

            # checks for improvement
            if self.improvement_check(bin_1, bin_2):
                return True

            else:
                self.swap_houses(house_1, bin_1, house_2, bin_2)
                return False

        else:
            self.swap_houses(house_1, bin_1, house_2, bin_2)
            return False          

    def swap_houses(self, house_1, bin_1, house_2, bin_2):
        self.bins[bin_1][house_1], self.bins[bin_2][house_2] = self.bins[bin_2][house_2], self.bins[bin_1][house_1]

    # function to start the optimization
    def first_fit(self):

        # make a list of bins
        bins = [[] for i in range(len(self.batteries))]
        try:
            for house in self.houses:
                lowest = self.bin_size[0]
                for i, el in enumerate(bins):
                    current = self.size_of_bin(el)
                    if current < lowest:
                        lowest = current
                        bin_place = i
                bins[bin_place].append(house)
                self.constraint_check(bins[bin_place])
        except ConstraintError:
            exit('First fit failed!')

        bins = np.array(bins)

        return bins

    def random_fit(self):

        temp_houses = copy.copy(self.houses)

        bins = [[] for i in range(len(self.batteries))]

        smallest_bin = self.bin_size[0]

        for n in range(len(self.houses) - 1):
            house_index = random.randrange(len(temp_houses))
            lowest = self.bin_size[0]
            for i, el in enumerate(bins):
                current = self.size_of_bin(el)
                if current < lowest:
                    lowest = current
                    bin_place = i
            bins[bin_place].append(temp_houses[house_index])
            np.delete(temp_houses, house_index)

        for bucket in range(len(bins)):
            if not self.constraint_check(bins[bucket]):
                raise FitError
        return np.array(bins)

    # def reset(self):



    def re_random_fit(self): 

        # create copy of houses
        temp_houses = copy.copy(self.houses)
            
        # create bins list
        bins = [[] for i in range(len(self.batteries))]
        
        # define initial lowest capacity left
        lowest = self.bin_size[0]

        for n in range(len(self.houses)):
            # pick a random house
            house_1 = random.randrange(len(temp_houses))

            for i, el in enumerate(bins):

                # check if current bin is lower than first bin
                current = self.size_of_bin(el)
                if current < lowest:
                    lowest = current
                    bin_place = i
            bins[bin_place].append(temp_houses[house_1])
            np.delete(temp_houses, house_1)

        if self.constraint_check(bins[bin_place]):
            return True
        else:

            self.random_fit()

        bins = np.array(bins)

        return bins
      

    # run the simulation iterations times and save best values , DOES NOT WORK 
    def run_simulation(self, iterations=25, best_value=10000):
        best_solution = []
        for i in range(iterations):
            self.bins = self.random_fit()
            tries = 0
            while tries < 10000:
                if not self.pick_swap():
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

    

    def climbing(self):
        """
        Runs the hill climber only once. Adds the current cost of distribution of the houses
        and returns the cost. 
        
        """    
        max_tries = TRIES
        tries = 0 
        while tries < max_tries:
            # print(tries)
            if tries == max_tries - 1:
                permutation = self.test_bins()
                # print(permutation)
                if len([i for i, j in zip(permutation, [0, 1, 2, 3, 4]) if i == j]) == 5:
                    tries += 1
                else:
                    new_bins = [[] for i in range(5)]
                    for i, el in enumerate(permutation):
                        new_bins[i] = self.bins[el]
                    self.bins = new_bins 
                    tries = 0

            else:
                swap = self.pick_swap()
                if self.try_swap(swap[0], swap[1], swap[2], swap[3]):
                    tries = 0
                else:
                    tries += 1 
        self.current_value = 0
        for el in self.cost_values:
            self.current_value += el
        return self.current_value               

    def loose_climbing(self):
        tries = 0 
        while tries < TRIES:
            swap = self.pick_swap()
            if self.try_loose_swap(swap[0], swap[1], swap[2], swap[3]):
                for el in self.cost_values:
                    self.current_value += el
                return True
            else:
                tries += 1
        for el in self.cost_values:
            self.current_value += el
        return False

    def test_bins(self):
        best_swap = copy.copy(self.cost_values)
        best_permutation = [0, 1, 2, 3, 4]
        for el in itertools.permutations(range(5), len(range(5))):
            current = []
            for i, bucket in enumerate(self.bins):
                current.append(self.mean_distance_check(bucket, el[i]))
                # kijken welke waarde je krijgt en dan de beste steeds opslaan, die waarde returnen en oproepen in climbing function
            if sum(current) < sum(best_swap):
                best_swap = current
                best_permutation = el

        return best_permutation

    def __lt__(self, other):
        if isinstance(other, HillClimber):
            if self.current_value < other.current_value:
                return True
            else:
                return False
        elif other == None:
            return True

        else:
            raise TypeError

        # else:
            # raise TypeError

    def __gt__(self, other):
        if isinstance(other, HillClimber):
            if self.current_value > other.current_value:
                return True
            else:
                return False
        elif other == None:
            return True

        else:
            raise TypeError

    # save the solution to a csv
    def write_solution(self, best_solution, best_value):
        with open('../../data/solutions/wijk1/solution_{}.csv'.format(best_value), 'a') as outfile:
            writer = csv.writer(outfile)
            for i, el in enumerate(best_solution):
                for row in el:
                    writer.writerow([row.position[0], row.position[1], row.power, i])


if __name__ == '__main__':

    CSV_HOUSES = '../../data/wijk1_huizen.csv'
    CSV_BATTERIES = '../../data/wijk1_batterijen.csv'

    houses = data_structure.read_csv(CSV_HOUSES, house=True)
    batteries = data_structure.read_csv(CSV_BATTERIES)

    solutions = []
    for i in range(1):
        hill = HillClimber(houses, batteries)
        val = hill.climbing()
        hill.write_solution(hill.bins, val)
        solutions.append(val)

    print(solutions)
# main.py

import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.getcwd(), '.')))
sys.path.append(os.path.abspath(os.path.join(os.getcwd(), '/algorithms')))

from data_structure import Battery, House, read_csv
from algorithms.simanneal import SimAnneal
import pickle
import random

def create_file_path(i, type):
    """
    Simple function to create a file path.
    """
    return '../data/wijk{}_{}.csv'.format(i, type)

if __name__ == '__main__':

    if sys.argv[1] == 'hill':
        houses = read_csv(create_file_path(sys.argv[2], 'huizen'), house=True)
        batteries = read_csv(create_file_path(sys.argv[2], 'batterijen'))
        anneal = SimAnneal(houses, batteries, sys.argv[2], cooling='lin', max_iter=int(sys.argv[3]))
        try:
            anneal.anneal()
        finally:
            anneal.plot_visualization()
            file = random.randrange(500)
            with open('../objects/{}.obj'.format(file), 'wb') as f:
                pickle.dump(anneal, f)
                print(file)


    elif sys.argv[1] == 'sim':
        houses = read_csv(create_file_path(sys.argv[2], 'huizen'), house=True)
        batteries = read_csv(create_file_path(sys.argv[2], 'batterijen'))
        if sys.argv[3] is not 'interest':
            anneal = SimAnneal(houses, batteries, sys.argv[2], cooling=sys.argv[3], max_iter=int(sys.argv[4]))

        else:
            anneal = SimAnneal(houses, batteries, sys.argv[2], cooling=sys.argv[3], max_iter=int(sys.argv[4], interest=float(sys.argv[5])))            
        try:
            anneal.anneal()
        finally:
            anneal.plot_visualization()
            file = random.randrange(500)
            with open('../objects/{}.obj'.format(file), 'wb') as f:
                pickle.dump(anneal, f)
                print(file)
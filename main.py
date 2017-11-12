# main.py

import data_structure
import data_generator
from binpackp import NumberBin, Fit

if __name__ == '__main__':
    matrix = data_generator.generate_grid(150, 5, 50, 50)

    batteries = []
    houses = []
    for row in matrix:
        for el in row:
            if el > 0:
                houses.append(el)
            elif el < 0:
                batteries.append(el)

    bin_size = batteries[0] * -1

    generic_results = Fit.fit(NumberBin, bin_size, houses)
    first_fit_results = Fit.ff(NumberBin, bin_size, houses)

    print('General function: ', generic_results)
    print('First Fit Function', first_fit_results)
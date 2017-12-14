# data_generator.py
#
# Will generate randomized input data for the smart grid problem
# Not actually used

import random
import sys
import math

# CONSTANTS
MAXPOWER = 1000
MINPOWER = 10
ERROR_MARGIN = 1.01

# grid generator
def generate_grid(num_h, num_b, x, y):
    
    # create an empty grid
    matrix = [[0 for i in range(x)] for j in range(y)]
    counter_h = 0
    counter_b = 0
    battery_power = 0

    # first add houses
    while counter_h < num_h:
        x_try = random.randrange(x)
        y_try = random.randrange(y)

        # check if random spot is still empty
        if matrix[y_try][x_try] == 0:

            # get random power
            matrix[y_try][x_try] += random.randint(MINPOWER, MAXPOWER)
            battery_power += matrix[y_try][x_try]
            counter_h += 1

    # determine amount of battery power needed and fill up batteries 
    battery_power = math.ceil((battery_power / num_b) * ERROR_MARGIN)
    while counter_b < num_b:
        x_try = random.randrange(x)
        y_try = random.randrange(y)

        # place battery
        if matrix[y_try][x_try] == 0:
            matrix[y_try][x_try] -= battery_power
            counter_b += 1

    return matrix

if __name__ == '__main__':

    # error messages
    try:
        if (int(sys.argv[1]) + int(sys.argv[2]) <= int(sys.argv[3]) * int(sys.argv[4])):
            matrix = generate_grid(int(sys.argv[1]), int(sys.argv[2]),\
            int(sys.argv[3]), int(sys.argv[4]))
        else:
            sys.exit('grid will be too small')
    except IndexError:
        sys.exit('usage: python3 data_generator.py num_houses num_batteries x y')
        
    # output
    print(matrix)
    sum_total = 0
    for row in matrix:
        for el in row:
            sum_total += el
    print(sum_total)
import csv
import random
import sys
import math

BASE_PATH = 'data/self_created/'

MAXPOWER = 10
ERROR_MARGIN = 1.1

def generate_grid(num_h, num_b, x, y):
    matrix = [[0 for i in range(x)] for j in range(y)]
    counter_h = 0
    counter_b = 0
    battery_power = 0
    while counter_h < num_h:
        x_try = random.randrange(x)
        y_try = random.randrange(y)
        if matrix[y_try][x_try] == 0:
            matrix[y_try][x_try] += random.randint(1, MAXPOWER)
            battery_power += matrix[y_try][x_try]
            counter_h += 1

    battery_power = math.ceil((battery_power / num_b) * ERROR_MARGIN)  
    while counter_b < num_b:
        x_try = random.randrange(x)
        y_try = random.randrange(y)
        if matrix[y_try][x_try] == 0:
            matrix[y_try][x_try] -= battery_power
            counter_b += 1
            
    return matrix

if __name__ == '__main__':

    matrix = generate_grid(int(sys.argv[1]), int(sys.argv[2]),\
    int(sys.argv[3]), int(sys.argv[4]))
    print(matrix)
    sum_total = 0
    for row in matrix:
        for el in row:
            sum_total += el
    print(sum_total)
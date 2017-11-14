# main.py

from data_structure import Grid, Battery, House
import data_generator

WIDTH = 1
HEIGHT = 2

if __name__ == '__main__':

    matrix = data_generator.generate_grid(1, 1, WIDTH, HEIGHT)
    print(matrix)
    grid = Grid(WIDTH, HEIGHT)

    for i, row in enumerate(matrix):
        for j, el in enumerate(row):
            if el > 0:
                house = House(i, j, el)
                grid.append_structure(house)
            elif el < 0:
                battery = Battery(i, j, -el)
                grid.append_structure(battery)
    print(grid)
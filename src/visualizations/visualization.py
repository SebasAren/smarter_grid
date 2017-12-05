
from data_structure import Battery, House
import data_generator 
import numpy as np
import sys 
import matplotlib.pyplot as plt
import csv

class visualization(object):
    # read data
    def read_csv(f, house=False):
        with open(f) as infile:
            reader = csv.reader(infile)
            rv = []

            # skip headers
            if not house:
    	        next(reader, None)
            for row in reader:

                # create either a house or a battery
                if house:
                    entry = House(int(row[0]), int(row[1]), float(row[2]))
                    entry.bat_id = int(row[3])
                else:
                    entry = Battery(int(row[0]), int(row[1]), float(row[2]))
                rv.append(entry)
            return rv

    CSV_FILE_BATTERIES = 'data/wijk1_batterijen.csv'
    CSV_FILE_HOUSES = 'data/solutions/wijk1/solution_5669.csv'

    houses = read_csv(CSV_FILE_HOUSES, house=True)
    batteries = read_csv(CSV_FILE_BATTERIES)

    # variables to store coördinates
    x_houses= []
    y_houses=[]
    x_batteries=[]
    y_batteries=[]

    for house in houses:
    	x_houses.append(house.position[0])
    	y_houses.append(house.position[1])

    for batterie in batteries:
    	x_batteries.append(batterie.position[0])
    	y_batteries.append(batterie.position[1])

    # lists for colours and numbers of the different batteries
    colours = ["red", "green", "blue", "black", "purple"]
    battery_number= ["battery 0", "battery 1", "battery 2", "battery 3", "battery 4"]

    # plot the houses 
    for i in range(len(x_houses)):
    	plt.scatter(x_houses[i], y_houses[i], color= colours[houses[i].bat_id], marker = '^', s = 50)

    # plot the batteries
    for i in range(len(x_batteries)):
    	plt.scatter(x_batteries[i], y_batteries[i], color= colours[i], marker = 'x', s = 50) #label = battery_number[i])
    	

    # add grid to graph
    plt.grid(b = True, axis = 'both')

    # scale the x and y axis
    plt.xticks(np.arange(0, 51, 1))
    plt.yticks(np.arange(0, 51, 1))

    # lables for x and y axis and title
    plt.ylabel('y')
    plt.xlabel('x')

    plt.title('Wijk 1 (5669)')
    plt.legend()
    plt.show()



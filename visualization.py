from data_structure import Battery, House, read_csv
import data_generator 
import numpy as np
import sys 
import matplotlib.pyplot as plt

CSV_FILE_BATTERIES = 'data/wijk1_batterijen.csv'
CSV_FILE_HOUSES = 'data/wijk1_huizen.csv'

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
battery_number= ["batterie 0", "batterie 1", "batterie 2", "batterie 3", "batterie 4"]

# plot the houses 
plt.scatter(x_houses, y_houses, color= 'k', marker = '^', s = 50, label = 'houses')

# plot the batteries
for i in range(len(x_batteries)):
	plt.scatter(x_batteries[i], y_batteries[i], color= colours[i], marker = 'x', s = 50, label = battery_number[i])
	

# add grid to graph
plt.grid(b = True, axis = 'both')

# scale the x and y axis
# dit moet ook nog afhankelijk worden van welke grid je kiest
plt.xticks(np.arange(0, 51, 1))
plt.yticks(np.arange(0, 51, 1))

# # lables for x and y axis and title
plt.ylabel('y')
plt.xlabel('x')
# # TITEL MOET AFHANKELIJK ZIJN VAN DE WIJK, DUS MOET NOG AANGEPAST WORDEN
# # waarschijnlijk iets van plt.title(sys.argv[1]) ofzoiets
plt.title('test_wijk1')
plt.legend()
plt.show()



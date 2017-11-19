import data_structure
import data_generator
import numpy as np
import sys 
import matplotlib.pyplot as plt

# lists of coördinates of the houses
x = []
y= []

# lists of coördinates of the batteries
x1 = []
y1 = []


# append x coördinates of the houses in list
for house in houses:
	x.append('TODO')

# append y coördinates of the houses in list
for house in houses: 
	y.append('TODO')

# append x coördinates of the batteries in list
for batterie in batteries:
	x1.append('TODO')

# append y coördinates of the batteries in list
for batterie in batteries:
	y1.append('TODO')	

# plot the houses 
plt.scatter(x, y, color= 'k', marker = '^', s = 50, label = 'houses')
# plot the batteries
plt.scatter(x1, y1, color= 'k', marker = 'x', s = 50, label = 'batteries')

# add grid to graph
plt.grid(b = True, axis = 'both')

# scale the x and y axis
# dit moet ook nog afhankelijk worden van welke grid je kiest
plt.xticks(np.arange(0, 50, 1))
plt.yticks(np.arange(0, 50, 1))

# lables for x and y axis and title
plt.ylabel('y')
plt.xlabel('x')
# TITEL MOET AFHANKELIJK ZIJN VAN DE WIJK, DUS MOET NOG AANGEPAST WORDEN
# waarschijnlijk iets van plt.title(sys.argv[1]) ofzoiets
plt.title('test_wijk1')
plt.legend()
plt.show()



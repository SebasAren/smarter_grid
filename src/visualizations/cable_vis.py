import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.getcwd(), '.')))
sys.path.append(os.path.abspath(os.path.join(os.getcwd(), '..')))
from data_structure import Battery, House
import data_generator 
import numpy as np
import matplotlib.pyplot as plt
import csv
import pylab as pl 
from matplotlib import collections as mc


def draw_cable(lines):


	lc = mc.LineCollection(lines, linewidths=2)
	fig, ax = pl.subplots()
	ax.add_collection(lc)
	ax.autoscale()
	ax.margins(1.0)

	plt.show()
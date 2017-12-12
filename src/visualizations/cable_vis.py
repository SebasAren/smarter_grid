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

class CableVis(object):
    def __init__(self, lines, houses):
        self.lines = lines
        self.fig, self.ax = pl.subplots()
        self.ax.margins(1.0)
        self.ax.set_xlim([0, 50])
        self.ax.set_ylim([0, 50])
        self.colors = ["red", "green", "blue", "black", "purple"]
        plt.ylabel('y')
        plt.xlabel('x')
        plt.xticks(np.arange(0, 51, 5))
        plt.yticks(np.arange(0, 51, 5))

    def draw_cable(self, battery_id):
        lc = mc.LineCollection(self.lines[battery_id], colors=self.colors[battery_id] ,linewidths=2)
        self.ax.add_collection(lc)

    def make_scatter(self):
        pass

    def plot(self):
        for i in range(len(self.lines)):
            self.draw_cable(i)
        plt.show()
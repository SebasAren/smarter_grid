#  This file plots the
#  different networks
#

# import the right files
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.getcwd(), '.')))
sys.path.append(os.path.abspath(os.path.join(os.getcwd(), '..')))

import numpy as np
import matplotlib.pyplot as plt
import pylab as pl 
from matplotlib import collections as mc

class CableVis(object):
    """
    Creates a visualization of the different networks.
    
    """
    
    def __init__(self, lines, houses):
        """
        Initializes the graph.
        
        Variables:
        lines: array of tuples containing line segments.
        houses: list of house objects.

        """
        
        self.lines = lines
        self.fig, self.ax = pl.subplots()
        self.ax.margins(1.0)
        
        # sets limits to x and y axis
        self.ax.set_xlim([0, 50])
        self.ax.set_ylim([0, 50])
        
        # gives colors to different networks
        self.colors = ["red", "green", "blue", "black", "purple"]
        
        # gives labels to x and y axis and create ticks
        plt.ylabel('y')
        plt.xlabel('x')
        plt.xticks(np.arange(0, 51, 5))
        plt.yticks(np.arange(0, 51, 5))

    def draw_cable(self, battery_id):
        """
        Draws cables between the two elements in the network.
        
        Variable:
        battery_id: id of the five different batteries.

        """
        
        lc = mc.LineCollection(self.lines[battery_id], colors=self.colors[battery_id] ,linewidths=2)
        self.ax.add_collection(lc)

    def make_scatter(self):
        pass

    def plot(self):
        """
        Draws the cable for all the networks.
        
        """
        
        for i in range(len(self.lines)):
            self.draw_cable(i)

    def show_plot(self):
        """
        Shows plot of the networks

        """
        plt.show()

    def save_plot(self, max_iter, cooling, score, wijk):
        """
        Saves plot of the networks in the appropriate file.
        
        Variables:
        max_iter: number of iterations.
        cooling: defines which cooling scheme is used.
        score: total score after running the algorithm.
        wijk: in order to define which 'wijk' is used.

        """
        pl.savefig('../grids/wijk{}/{}_{}_{}.png'.format(wijk, max_iter, cooling, score))
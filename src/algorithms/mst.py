# mst.py

# import right files 
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.getcwd(), '.')))
sys.path.append(os.path.abspath(os.path.join(os.getcwd(), '..')))
from data_structure import Network
import csv

class Mst(object):
    """
    Mst algotrithm which makes sure that cables will be placed
    on the right places.

    """
    def __init__(self, nodes):
        
        self.nodes = [nodes[i:i+1] for i in range(0, len(nodes), 1)]
        self.total_cost = 0
        self.lines = []

    def find_shortest_distance(self):
        """
        Finds the shortest distance between two network elements.

        """
        shortest_distance = 10000
        shortest_pair = []

        # iterates over the nodes and finds the shortest distance
        for n, arr in enumerate(self.nodes):
            for m, item in enumerate(arr):
                for i in range(n + 1, len(self.nodes)):
                    for j, other_item in enumerate(self.nodes[i]):
                        dist = item.distance(other_item)
                        if dist <= shortest_distance:
                            shortest_distance = dist
                            shortest_pair = [(n, m), (i, j)]
        return (shortest_pair)

    def merge_networks(self, networkA, networkB, new_nodes):
        """
        Merges the different networks into one network.

        """
        # merges the different networks into one network 
        connected_list = []
        self.nodes[networkA[0]] = self.nodes[networkA[0]] + self.nodes[networkB[0]] + new_nodes
        self.nodes.pop(networkB[0])


    def create_path(self, begin_node, end_node):
        """
        Creates a path between the two networks with 
        the shortest distances.

        First equate the x value of the coordinates, then equate
        the y value of the coordinates. 

        Adds the coordinates of the points over which the cables goes.

        Sends info to create a plot of all the cable networks.

        """
        start = self.nodes[begin_node[0]][begin_node[1]]
        end = self.nodes[end_node[0]][end_node[1]]

        new_nodes = []

        
        length = start.distance(end)

        # saves all the lines between two coordinates in order to plot the networks
        self.create_lines(start.x, start.y, end.x, end.y)

        if length < 1:
            # wijk3 haa two houses on the same spot
            return []

        # cable will be created by equating the x coordinates first and then
        # the y coordinates will be equated
        else:
            width = start.x - end.x
            height = start.y - end.y
            self.equate_width(start, end, new_nodes, width, height, length)
            self.equate_height(start, end, new_nodes, width, height, length)
            return new_nodes

    
    def equate_width(self, start, end, new_nodes, width, height, length):
        """
        When x coordinates differ, equates x coordinates and adds network elements to network. 

        """
        
        # if x coordinates differ, equate x coordinate and add network elements to network
        if width < 0:
            if abs(height) > 0:
                for i in range(1, abs(width) + 1):
                    new_nodes.append(Network((start.x + i), start.y))
            else:
                for i in range(1, abs(width)):
                    new_nodes.append(Network((start.x + i), start.y))

        elif width > 0:
            if abs(height) > 0:
                for i in range(1, abs(width) + 1):
                    new_nodes.append(Network((start.x - i), start.y))
            else:
                for i in range(1, abs(width)):
                    new_nodes.append(Network((start.x - i), start.y))

 
    def equate_height(self, start, end, new_nodes, width, height, length):
        """
        When y coordinates differ, equates y coordinates and adds network elements to network. 

        """

        # if y coordinates differ, equate y coordinates and add network elements to network
        if height < 0:
            for i in range(1, abs(height)):
                new_nodes.append(Network(end.x, (start.y + i)))
        elif height > 0:
            for i in range(1, abs(height)):
                new_nodes.append(Network(end.x, (start.y - i)))

    def run(self):
        """
        This function actually runs the whole algotrithm.
        
        """
        while len(self.nodes) > 1:
            spots = self.find_shortest_distance()
            new_nodes = self.create_path(spots[0], spots[1])
            self.total_cost += len(new_nodes) + 1
            
            self.merge_networks(spots[0], spots[1], new_nodes)

    def create_lines(self, x_1, y_1, x_2, y_2):
        """
        Saves all the lines between two coordinates in order to plot the networks
        
        """
        self.lines.append([(x_1, y_1), (x_2, y_1)])
        self.lines.append([(x_2, y_1), (x_2, y_2)])

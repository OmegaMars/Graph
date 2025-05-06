from ..diGraph import DiGraph
from ..graph import Graph
from typing import Union
import numpy as np

class Dijkstra:
    def __init__(self, graph:Graph):
        self.graph = graph
        self.start_node = self.graph.node_ids[0]
        for node in self.graph.node_list:
            if node[0] < self.start_node:
                self.start_node = node
        self.nodes = self.graph.node_ids
        # _, self.nodes = self.graph.get_sorted_node_lists() <------------ TODO
        self.weight_list = [float('inf')] * len(self.nodes)

    def calculate(self):
        explored = [self.nodes[0]]
        not_explored = self.nodes
        not_explored.pop(0)
        self.weight_list[0] = 0
        for node in not_explored:
            explored.append(node)
            neighbors = self.graph.get_neighboring_nodes(node)
            for neighbor in neighbors:
                if neighbor[0] in explored:
                    continue
                else:
                    self.weight_list[neighbor[0]] = self.weight_list[neighbor[0]] + neighbor[1]\
                         if self.weight_list[neighbor[0]] == float('inf') else neighbor[1]

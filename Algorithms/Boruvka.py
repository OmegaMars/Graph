from ..diGraph import DiGraph
from ..graph import Graph
from typing import Union
import numpy as np

class Boruvka:
    def __init__(self, graph:Graph):
        self.graph = graph
        self.start_node = self.graph.node_ids[0]

    def calculate(self):
        result = []
        for node in self.graph.node_ids:
            pass
        return result

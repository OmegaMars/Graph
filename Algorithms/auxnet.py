from ..diGraph import DiGraph
from ..graph import Graph
import numpy as np

class AuxNet:
    def __init__(self, graph:DiGraph):
        self.graph = graph
        self.start_node = self.graph.node_ids[0]

    def calculate(self):
        result = []
        for node in self.graph.node_ids:
            pass
        return result

from ..graph import Graph
from ..diGraph import DiGraph


class Hierholzer:
    def __init__(self, graph):
        self.graph = graph
        self.edge_ids = self.graph.get_edge_ids()
        self.explored = []

    def hierholzer(self):
        start = self.graph.node_list[0]
        
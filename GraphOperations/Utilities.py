from typing import Union
from ..diGraph import DiGraph
from ..graph import Graph


class Utilities:
    def __init__(self, graph:Union[Graph, DiGraph]):
        self.graph = graph

    def distance(self, node1, node2):
        pass
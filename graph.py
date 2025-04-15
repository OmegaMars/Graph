# import networkx
# import graphx
from typing import Union
import sys
if "pytest" in sys.modules:
    from .diGraph import DiGraph
else:
    from diGraph import DiGraph

class Graph(DiGraph):
    def __init__(self):
        super().__init__()

    def add_edge(self, edge:list):
        """
        Adds both edges from 1 to 2 and 2 to 1.

        Args:
            edge (tuple): A tuple that represents the edge between node 1 and node 2.
        """
        super().check_edge(edge)
        super().add_edge(edge)
        # super().add_edge(tuple(edge))
        # super().add_edge((edge[1], edge[0]))

    def delete_edge(self, edge:list):
        """
        Removes both edges from 1 to 2 and 2 to 1.

        Args:
            edge (tuple): A tuple that represents the edge between node 1 and node 2.
        """
        super().check_edge(edge)
        super().delete_edge(edge)
        # super().delete_edge(tuple(edge))
        # super().delete_edge((edge[1], edge[0]))

    def get_degree(self, vertex:Union[tuple, int]) -> int:
        """
        Returns:
            int: The degree of the given vertex.
        """
        super().check_vertex(vertex)
        degree = 0
        explored = []
        for edge in self.edge_list:
            if vertex in edge:
                if not ((edge[1], edge[0]) in explored or edge in explored):
                    degree += 1
                    explored.append(edge)
        return degree

    def get_number_off_nodes_with_odd_degree(self) -> int:
        """
        Returns:
            int: Number of nodes with odd degree.
        """
        node_count = 0
        for node in self.node_list:
            degree = self.get_degree(node[0])
            if (degree % 2) != 0:
                node_count += 1
        return node_count
    
    def check_if_graph_is_regular(self) -> bool:
        """
        Returns:
            bool: True if the graph is a regular graph.
        """
        last_degree = -1
        for node in self.node_list:
            degree = self.get_degree(node[0])
            if last_degree == -1:
                last_degree = degree
            elif last_degree != degree:
                return False
        return True

    def calculate_eigenvalue_centrality(self):
        """
        Not for DiGraph.
        TODO
        """
        pass
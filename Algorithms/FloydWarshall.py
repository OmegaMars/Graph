from typing import Union
from ..diGraph import DiGraph
from ..graph import Graph

class FloydWarshall:
    def __init__(self, graph:Union[Graph, DiGraph]):
        self.graph = graph
        self.start_node = self.graph.node_ids[0]
        for node in self.graph.node_list:
            if node[0] < self.start_node:
                self.start_node = node
        self.nodes = self.graph.node_ids
        # _, self.nodes = self.graph.get_sorted_node_lists() <------------ TODO
        self.solution_matrix = [[float('inf')] * len(self.nodes) for _ in range(len(self.nodes))]

    def calculate(self):
        self.predecessor_matrix = [[float('inf')] * len(self.nodes) for _ in range(len(self.nodes))]
        number_shortest_paths_through_node = [[]] # [[Start Node, End Node, Intermediate Node, Count]]
        number_shortest_paths = [[]] # [[Start Node, End Node, Count]]
        for edge in self.graph.edge_list:
            print(edge)
            self.solution_matrix[edge[0] - 1][edge[1] - 1] = edge[2]
        for edgei in self.graph.node_ids:
            edgei -= 1
            for edgej in self.graph.node_ids:
                edgej -= 1
                if edgei != edgej:
                    edge = self.graph.get_edge_between_two_node_indices(edgei, edgej)
                    if edge:
                        self.solution_matrix[edgei][edgej] = edge[2]
                else:
                    self.solution_matrix[edgei][edgej] = 0
                if edgei == edgej and self.solution_matrix[edgei][edgej] == float('inf'):
                    self.predecessor_matrix[edgei][edgej] = 0
                else:
                    self.predecessor_matrix[edgei][edgej] = edgei
        for edgek in self.graph.node_ids:
            edgek -= 1
            for edgei in self.graph.node_ids:
                edgei -= 1
                if self.solution_matrix[edgei][edgek] + self.solution_matrix[edgek][edgei] < 0:
                    return # TODO CYCLE
                else:
                    for edgej in self.graph.node_ids:
                        edgej -= 1
                        calc = self.solution_matrix[edgei][edgek] + self.solution_matrix[edgek][edgej]
                        if calc < self.solution_matrix[edgei][edgej]:
                            self.solution_matrix[edgei][edgej] = calc
                            self.predecessor_matrix[edgei][edgej] = self.predecessor_matrix[edgek][edgej]
                        if calc == self.solution_matrix[edgei][edgej]:
                            pass
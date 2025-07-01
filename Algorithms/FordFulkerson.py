from ..diGraph import DiGraph


class FordFulkerson:
    def __init__(self, graph:DiGraph):
        self.graph = graph
        self.start_node = self.graph.node_ids[0]
        self.end_node = self.graph.node_ids[-1]
        for index, node in enumerate(self.graph.node_list):
            if node[0] < self.start_node:
                self.start_node = node
            if node[0] > self.end_node:
                self.end_node = node
            # self.graph.node_list[index][1] =  # set node labels to (-, inf)
        self.sorce = (self.start_node[0], ('-', float('inf')))
        for index, edge in enumerate(self.graph.edge_list):
            self.graph.edge_list[index] = (edge[0], edge[1], 0, edge[3]) # weight represents flow
        self.nodes = self.graph.node_ids
        # self.solution_matrix = [0.0 for _ in range(len(self.nodes))]

    def calculate(self):
        explored = []
        explored.append(self.start_node)
        explored.append(self.end_node)
        not_explored = self.nodes.copy()
        while len(explored) < len(self.nodes):
            vertex = not_explored.pop(0)
            adjacent_edges = self.graph.get_adjacent_edges()
            for edge in adjacent_edges:
                target_node = edge[1]
                if edge[2] < edge[3] and self.graph.node_list[target_node][1] == 0:
                    d = min(edge[3] - edge[2], self.graph.node_list[vertex][1][2])
                    label = (target_node, "+", d)
                    self.graph.node_list[target_node][1] = label
            for edge in adjacent_edges:
                target_node = edge[0]
                if self.graph.node_list[target_node][1] == 0 and edge[1] > 0:
                    d = min(edge[1], self.graph.node_list[vertex][1][2])
                    label = (target_node, "-", d)
                    self.graph.node_list[target_node][1] = label
            if vertex not in explored:
                explored.append(vertex)
            w = vertex[1][2]
            for node in self.graph.node_list:
                if node == self.start_node:
                    continue
                v = node[1][0]
                if node[1][1] == '+':
                    for edge in self.graph.get_edge_between_two_node_indices(v, w):
                        edge[2] += node[1][2]
                if node[1][1] == '-':
                    for edge in self.graph.get_edge_between_two_node_indices(v, w):
                        edge[2] -= node[1][2]
            for index, node in enumerate(self.graph.node_list):
                self.graph.node_list[index][1] = 0
        return explored
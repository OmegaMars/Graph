from ..graph import Graph

class PriemAndJanik:
    def __init__(self, graph:Graph):
        self.graph = graph
        self.start_node = self.graph.node_ids[0]
        for node in self.graph.node_list:
            if node[0] < self.start_node:
                self.start_node = node
        self.nodes = self.graph.node_ids
        # _, self.nodes = self.graph.get_sorted_node_lists() <------------ TODO
        # self.solution_matrix = [[float('inf')] * len(self.nodes) for _ in range(len(self.nodes))]
        self.solution_matrix = [float('inf') for _ in range(len(self.nodes))]

    def calculate(self):
        not_explored = self.nodes
        explored = []
        next_node = self.start_node
        self.solution_matrix[next_node - 1] = 0
        edge_list = []
        while len(not_explored) > 0:
            node = next_node
            weight_list = []
            for edge in self.graph.edge_list:
                node2 = edge[0] if edge[1] == node else edge[1]
                if (edge[0] == node or edge[1] == node) and node2 not in explored:
                    weight_list.append(edge)
                    if edge[2] < self.solution_matrix[node2 - 1]:
                        self.solution_matrix[node2 - 1] = edge[2]
            if len(weight_list) <= 0:
                break
            last_edge = weight_list[0]
            for edge in weight_list:
                if edge[2] < last_edge[2]:
                    last_edge = edge
            next_node = last_edge[1] if last_edge[0] == node else last_edge[0]
            explored.append(node)
            edge_list.append(self.graph.get_edge_between_two_node_indices(node, next_node))
            # print(f'{edge_list}, , {node}, , {next_node}, , {self.graph.get_edge_between_two_node_indices(node, next_node)}')
            not_explored.remove(node)
        return self.solution_matrix, edge_list

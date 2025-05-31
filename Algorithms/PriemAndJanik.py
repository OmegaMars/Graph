from ..graph import Graph

class PriemAndJanik:
    def __init__(self, graph:Graph):
        self.graph = graph
        self.start_node = self.graph.node_ids[0]
        for node in self.graph.node_list:
            if node[0] < self.start_node:
                self.start_node = node
        self.nodes = self.graph.node_ids
        self.solution_matrix = [[float('inf'), ()] for _ in range(len(self.nodes))]

    def calculate(self):
        """
        Calculate the minimum spanning tree using Prim's algorithm.
        Returns:
            tuple: A tuple containing the list of weights for each node and the list of edges in the minimum spanning tree.
        """
        not_explored = len(self.nodes) - 1
        explored = []
        next_node = self.start_node
        self.solution_matrix[self.start_node - 1][0] = 0
        edge_list = []
        while not_explored > 0:
            node = next_node
            explored.append(node)
            adjancent_edges = self.graph.get_adjacent_edges(node)
            print(explored)
            print(edge_list)
            for edge in adjancent_edges:
                target_node = edge[0] if edge[1] == node else edge[1]
                if (edge[0] == node or edge[1] == node) and target_node not in explored:
                    if edge[2] < self.solution_matrix[target_node - 1][0]:
                        self.solution_matrix[target_node - 1][0] = edge[2]
                        self.solution_matrix[target_node - 1][1] = edge
            lowest_weight = float('inf')
            lowest_weight_edge = None
            for index, weight in enumerate(self.solution_matrix):
                index += 1
                if index in explored: continue
                elif weight[0] < lowest_weight:
                    lowest_weight = weight[0]
                    lowest_weight_edge = weight[1]
            next_node = lowest_weight_edge[1] if lowest_weight_edge[0] in explored else lowest_weight_edge[0]
            edge_list.append(lowest_weight_edge)
            not_explored -= 1
        return self.convert_solution_matrix_to_weight_list(), edge_list

    def convert_solution_matrix_to_weight_list(self):
        """
        Convert the solution matrix to a list of weights.
        Returns:
            list: A list of weights corresponding to the nodes in the solution matrix.
        """
        weight_list = []
        for node in self.solution_matrix:
            weight_list.append(node[0])
        return weight_list
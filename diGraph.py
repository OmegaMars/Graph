from typing import Union

class DiGraph:
    def __init__(self):
        self.edge_list = [] # [(v1, v2, weight, capacity)]
        self.node_list = [] # [(id, label)]
        self.node_ids = []

    def get_edge_list(self):
        return self.edge_list

    def get_node_list(self):
        return self.node_list

    def get_node_ids(self):
        return self.node_ids

    def get_edge_ids(self):
        edge_ids = []
        for index, edge in enumerate(self.edge_list):
            edge_ids.append(index)
            return edge_ids

    def add_edge(self, edge:Union[tuple, list]):
        """
        Args:
            edge (tuple): A tuple or list that represents the edge between node 1 and node 2,
                          the cost and weight of the connection. Use list for undirected and tupe for directed edges.
        """
        input_type = type(edge)
        edge = self.check_edge(edge)
        if input_type == list:
            edge = list(edge)
        if not edge in self.edge_list:
            self.edge_list.append(edge)

    def add_vertex(self, vertex:Union[tuple, int]):
        """
        """
        if type(vertex) != int and type(vertex) != tuple:
            raise TypeError("vertex should be of type int or tuple")
        if type(vertex) == int:
            vertex = (vertex, "")
        if not vertex in self.node_list:
            self.node_list.append(vertex)
            self.node_ids.append(vertex[0])

    def delete_edge(self, edge:Union[tuple, list]):
        """
        Deletes an edge of the graph.

        Args:
            edge (tuple): A tuple or list that represents the edge between node 1 and node 2.
                          Oriented from 1 to 2 if it is a tuple.
        """
        self.check_edge(edge)
        for graph_edge in self.edge_list:
            if edge[0] == graph_edge[0]:
                if edge[1] == graph_edge[1]:
                    self.edge_list.remove(graph_edge)

    def delete_vertex(self, vertex:Union[tuple, int]):
        """
        Deletes an vertex and all edges, that connect to it.

        Args:
            vertex (tuple, int): The vertex to delete as tuple of (index, label) or just index.
        """
        if type(vertex) == int:
            vertex = (vertex, "")
        if vertex in self.node_list:
            self.node_list.remove(vertex)
            self.node_ids.remove(vertex[0])
        new_edge_list = []
        vertex_id = vertex[0]
        for edge in self.edge_list:
            if edge[0] != vertex_id and edge[1] != vertex_id:
                new_edge_list.append(edge)
        self.edge_list = new_edge_list

    def check_edge(self, edge:Union[tuple, list]):
        """
        Checks the types and length of the edge tuple.
        Also checks if the referenced edges exists.

        Args:
            edge (tuple): A tuple that represents the edge between node 1 and node 2.
                          Oriented from 1 to 2.
        """
        edge_type = type(edge)
        if type(edge) != tuple and type(edge) != list:
            raise TypeError("edge should be of type tuple for directed or list for undirected")
        if len(edge) not in [2, 3, 4]:
            raise ValueError("edge tuple should be of length 2 or 3 with cost.")
        else:
            if len(edge) == 3:
                edge = (edge[0], edge[1], edge[2], 0)
            elif len(edge) == 2:
                edge = (edge[0], edge[1], 0, 0)
            for vertex in edge[:1]:
                if not vertex in self.node_ids:
                    raise ValueError(f"vertex {vertex} does not exist")
            if edge_type == tuple:
                return edge
            else:
                return list(edge)

    def check_vertex(self, vertex:Union[tuple, int]):
        if type(vertex) != int and type(vertex) != tuple:
            raise TypeError("vertex should be of type int or tuple")
        if type(vertex) == int:
            vertex = (vertex, "")
        if not vertex in self.node_list:
            raise ValueError("vertex does not exist")

    def check_vertex_structure(self, vertex:Union[tuple, int]):
        if type(vertex) != tuple and type(vertex) != int:
            raise TypeError("vertex should be of type tuple or int")
        elif type(vertex) == tuple:
            if len(vertex) != 2:
                raise  ValueError("vertex tuple should be of length 2.")
            if type(vertex[0]) != int:
                raise TypeError("first element of vertex should be of type int")
            if type(vertex[1]) != str:
                raise TypeError("second element of vertex should be of type str.")
            return vertex
        elif type(vertex) == int:
            return tuple([vertex, None])

    def get_similar_oriented_edges(self) -> list:
        """
        Returns:
            list: Returns an list of undirected edges.
        """
        result = []
        for edge in self.edge_list:
            if edge not in result and (edge[1], edge[0], edge[2], edge[3]) not in result:
                result.append(edge)
        return result

    def get_in_degree(self, vertex:tuple) -> int:
        """
        Args:
            vertex (tuple, int): Fertex to get the incoming degree.

        Returns:
            int: Number of incoming edges.
        """
        if type(vertex) == int:
            vertex = self.check_vertex(vertex)
        number = 0
        for edge in self.edge_list:
            if edge[1] == vertex:
                number += 1
        return number

    def get_out_degree(self, vertex:Union[tuple, int]) -> int:
        """
        Args:
            vertex (tuple, int): Fertex to get the outgoing degree.

        Returns:
            int: Number of outgoing edges.
        """
        if type(vertex) == int:
            vertex = self.check_vertex(vertex)
        number = 0
        for edge in self.edge_list:
            if edge[0] == vertex:
                number += 1
        return number


    def get_number_of_nodes_where_incoming_not_equals_outgoing_degree(self):
        """
        Returns:
            int: Number of Nodes that have not the same amount of incoming and outgoing edges.
        """
        node_count = 0
        for node in self.node_list:
            in_degree = self.get_in_degree(node[0])
            out_degree = self.get_out_degree(node[0])
            if in_degree != out_degree:
                node_count += 1
        return node_count

    def check_if_graph_has_singelton(self):
        """
        Cecks if the graph is connected.

        Returns:
            bool: True if there is a vertex that has no edge aligned.
        """
        nodes = self.node_ids
        for edge in self.edge_list:
            for node in self.node_ids:
                if node == edge[0] or node == edge[1]:
                    nodes.remove(node)
        if nodes != []:
            return True
        else:
            return False

# import networkx
# import graphx
from typing import Union

class Vertex:
    def __init__(self, index:int, label:str=None):
        self.index = index
        self.label = label

class Edge:
    def __init__(self, vertex1:Vertex, vertex2:Vertex, cost:int=None):
        self.vertex1 = vertex1
        self.vertex2 = vertex2
        self.cost = cost

class DiGraph:
    def __init__(self):
        self.edge_list = [] # [(v1, v2, weight, capacity)]
        self.node_list = [] # [(id, label)]
        self.node_ids = []

    def add_edge(self, edge:tuple):
        """
        Args:
            edge (tuple): A tuple that represents the edge between node 1 and node 2 and the cost of the connection.
        """
        self.check_edge(edge)
        if len(edge) == 3:
            edge = (edge[0], edge[1], edge[2], 0)
        elif len(edge) == 2:
            edge = (edge[0], edge[1], 0, 0)
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

    def delete_edge(self, edge:Union[tuple]):
        """
        Deletes an edge of the graph.

        Args:
            edge (tuple): A tuple that represents the edge between node 1 and node 2.
                          Oriented from 1 to 2.
        """
        if edge in self.edge_list:
            self.edge_list.remove(edge)

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
        self.edge_list = [edge for edge in self.edge_list if vertex not in edge]

    def check_edge(self, edge:Union[tuple, list]):
        """
        Checks the types and length of the edge tuple.
        Also checks if the referenced edges exists.

        Args:
            edge (tuple): A tuple that represents the edge between node 1 and node 2.
                          Oriented from 1 to 2.
        """
        if type(edge) != tuple and type(edge) != list:
            raise TypeError("edge should be of type tuple for directed or list for undirected")
        if len(edge) != 2 and len(edge) != 3:
            raise ValueError("edge tuple should be of length 2 or 3 with cost.")
        for vertex in edge:
            if not vertex in self.node_ids:
                raise ValueError(f"vertex {vertex} does not exist")

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



class Graph(DiGraph):
    def __init__(self):
        super().__init__()

    def add_edge(self, edge:list):
        """
        Adds both edges from 1 to 2 and 2 to 1.

        Args:
            edge (tuple): A tuple that represents the edge between node 1 and node 2.
        """
        super().check_edge(tuple(edge))
        # super().add_edge(edge)
        super().add_edge(tuple(edge))
        super().add_edge((edge[1], edge[0]))

    def delete_edge(self, edge:list):
        """
        Removes both edges from 1 to 2 and 2 to 1.

        Args:
            edge (tuple): A tuple that represents the edge between node 1 and node 2.
        """
        super().check_edge(tuple(edge))
        super().delete_edge(tuple(edge))
        super().delete_edge((edge[1], edge[0]))

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

    def get_nodes_with_odd_degree(self) -> int:
        """
        Returns:
            int: Number of nodes with odd degree.
        """
        node_count = 0
        for node in self.node_list:
            degree = self.get_degree(node)
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
            degree = self.get_degree(node)
            if last_degree == -1:
                last_degree = degree
            elif last_degree != degree:
                return False
        return True

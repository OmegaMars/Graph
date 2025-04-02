from graph import Graph

class LineGraph:
    def __init__(self, graph):
        self.graph = graph
        self.line_graph = Graph()
        self.edge_list = []
        self.convert_edges_to_line_nodes()
        self.vertexes = []
        # Wenn 2 edges im original Graph am selben Knoten anliegen, sind sie mit einer edge im Linegraph verbunden.

    def convert_edges_to_line_nodes(self):
        self.edges = self.graph.get_similar_oriented_edges()
        for vertex in self.edges:
            self.line_graph.add_vertex(vertex)

    def add_edges_to_line_graph(self):
        connections = []
        explored = []
        discovered_nodes = []
        for edge in self.edges:
            edge = (edge[0], edge[1])
            for node in edge:
                if node not in discovered_nodes:
                    discovered_nodes.append(node)
            explored.append(edge)
        for node in discovered_nodes:
            candidates = []
            for edge in explored:
                if node == edge[0] or node == edge[1]:
                    candidates.append(edge)
            if len(candidates) > 1:
                connections.append(edge)
        for edge in connections:
            self.line_graph.add_edge(edge)
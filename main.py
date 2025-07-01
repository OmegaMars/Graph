from graph import Graph, DiGraph
from GraphOperations.line_graph import LineGraph
from Visualization.plot_graph import GraphPlotter
from Algorithms.PriemAndJanik import PriemAndJanik

if __name__ == "__main__":
    # graph = Graph()
    # vertices = [1, 2, 3, 4, 5]
    # edges = [[1, 2], [1, 3], [1, 4], [1, 5], [2, 3], [2, 4], [2, 5], [3, 4], [3, 5], [4, 5]]
    graph = Graph()
    vertices = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    edges = [(1, 2, 6), (1, 5, 8), (1, 7, 3), (1, 10, 7),
             (2, 5, 2), (2, 7, 5), (2, 8, 7), (2, 10, 7), (2, 3, 6),
             (3, 6, 4), (3, 7, 5), (3, 10, 0),
             (4, 5, 2), (4, 7, 3), (4, 8, 1), (4, 9, 4),
             (5, 6, 6), (5, 7, 6), (5, 8, 3), (5, 10, 3),
             (6, 7, 4), (7, 8, 7), (8, 9, 4)]
    for vertex in vertices:
        graph.add_vertex(vertex)

    for edge in edges:
        graph.add_edge(edge)

    line_graph = LineGraph(graph)

    print(line_graph.edge_list)
    print(line_graph.node_list)

    print(graph.edge_list)
    print(graph.node_list)
    print(graph.get_degree(1))
    print(graph.get_number_off_nodes_with_odd_degree())
    print(graph.check_if_graph_is_regular())

    # print("DELETE")
    # graph.delete_edge([1, 2])
    # graph.delete_vertex(2)

    # print(graph.edge_list)
    # print(graph.node_list)

    algorithm = PriemAndJanik(graph)
    spanning_tree_weights, spanning_tree_edges = algorithm.calculate()
    plotter = GraphPlotter()
    plotter.plot_graph(graph, spanning_tree_edges, edge_color='blue', show_weights=True)
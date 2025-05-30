from graph import Graph, DiGraph
from GraphOperations.line_graph import LineGraph
from Visualization.plot_graph import GraphPlotter

if __name__ == "__main__":
    graph = Graph()
    vertexes = [1, 2, 3, 4, 5]
    edges = [[1, 2], [1, 3], [1, 4], [1, 5], [2, 3], [2, 4], [2, 5], [3, 4], [3, 5], [4, 5]]
    for vertex in vertexes:
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

    print("DELETE")
    graph.delete_edge([1, 2])
    graph.delete_vertex(2)

    print(graph.edge_list)
    print(graph.node_list)

    plotter = GraphPlotter()
    plotter.plot_graph(graph)
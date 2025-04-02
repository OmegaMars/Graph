import pytest
from ...graph import Graph
from ...GraphOperations.line_graph import LineGraph

@pytest.fixture
def graph_f():
    graph = Graph()
    vertexes = [1, 2, 3, 4, 5]
    edges = [[1, 2], [1, 4], [2, 3], [2, 4], [4, 5]]
    for vertex in vertexes:
        graph.add_vertex(vertex)
    for edge in edges:
        graph.add_edge(edge)
    return graph

@pytest.fixture
def regular_graph(graph_f):
    graph = graph_f
    edges = [[1, 2], [1, 3], [1, 4], [1, 5], [2, 3], [2, 4], [2, 5], [3, 4], [3, 5], [4, 5]]
    for edge in edges:
        graph.add_edge(edge)
    return graph

def test_create_line_graph(graph_f):
    line_graph = LineGraph(graph_f)
    assert line_graph.node_list == [(1, ''), (2, ''), (3, ''), (4, ''), (5, '')]
    print(line_graph.edge_list)
    assert line_graph.edge_list == [[1, 2, 0, 0], [2, 3, 0, 0], [2, 4, 0, 0], [4, 5, 0, 0]]
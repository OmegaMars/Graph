import pytest
from ...graph import Graph
from ...Algorithms.Boruvka import Boruvka

@pytest.fixture
def graph():
    graph = Graph()
    vertexes = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    edges = [(1, 2, 25), (1, 5, 22), (1, 7, 14), (1, 10, 20),
             (2, 5, 21), (2, 7, 12), (2, 8, 24), (2, 10, 18), (2, 3, 10),
             (3, 6, 9), (3, 7, 7), (3, 10, 8),
             (4, 5, 3), (4, 7, 5), (4, 8, 4), (4, 9, 1),
             (5, 8, 23), (5, 6, 16), (5, 10, 17),
             (6, 7, 13), (8, 9, 6)]
    for vertex in vertexes:
        graph.add_vertex(vertex)
    for edge in edges:
        graph.add_edge(edge)
    return graph

def test_calculate(graph):
    algorithm = Boruvka(graph)
    edge_target = [(1, 7), (2, 3), (3, 7), (4, 9), (5, 4), (6, 4), (7, 4), (8, 4), (9, 4), (10, 3)]
    edge_result = algorithm.calculate()
    print()
    print(algorithm.solution_matrix)
    assert edge_result == edge_target
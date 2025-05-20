import pytest
from ...diGraph import DiGraph
from ...Algorithms.PriemAndJanik import PriemAndJanik

@pytest.fixture
def graph():
    graph = DiGraph()
    vertexes = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    edges = [(1, 2, 6), (1, 5, 8), (1, 7, 3), (1, 10, 7),
             (2, 5, 2), (2, 8, 7), (2, 10, 7), (2, 3, 6),
             (3, 6, 4), (3, 7, 5), (3, 10, 0),
             (4, 5, 2), (4, 7, 3), (4, 8, 1), (4, 9, 4),
             (5, 8, 3), (5, 6, 6), (5, 10, 3),
             (6, 7, 4), (8, 9, 4)]
    for vertex in vertexes:
        graph.add_vertex(vertex)
    for edge in edges:
        graph.add_edge(edge)
    return graph


def test_calculate(graph):
    algorithm = PriemAndJanik(graph)
    node_target = [0, 2, 0, 3, 2, 4, 3, 1, 4, 3]
    edge_target = [(1,7), (7,4), (4,8), (4,5), (5,2), (8,10), (10,3), (7,6), (4,9)]
    result, edge_result = algorithm.calculate()
    print()
    print(algorithm.solution_matrix)
    assert result == node_target
    assert edge_result == edge_target

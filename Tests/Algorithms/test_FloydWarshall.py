import pytest
from ...graph import Graph
from ...Algorithms.FloydWarshall import FloydWarshall

@pytest.fixture
def graph():
    graph = Graph()
    vertexes = [1, 2, 3, 4, 5]
    edges = [(1, 2, 3), (2, 1, 1.3), (5, 1, 2), (2, 3, -1), (2, 4, 7), (5, 2, -1), (3, 4, -1), (4, 5, 1.2)]
    for vertex in vertexes:
        graph.add_vertex(vertex)
    for edge in edges:
        graph.add_edge(edge)
    return graph


def test_calculate(graph):
    algorithm = FloydWarshall(graph)
    assert algorithm.calculate() is None
    print()
    for row in algorithm.solution_matrix:
        print(row)
    print()
    assert algorithm.solution_matrix is None

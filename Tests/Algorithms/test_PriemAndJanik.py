import pytest
from ...graph import Graph
from ...Algorithms.PriemAndJanik import PriemAndJanik

@pytest.fixture
def graph():
    graph = Graph()
    vertexes = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    edges = [(1, 2, 6), (1, 5, 8), (1, 7, 3), (1, 10, 7),
             (2, 5, 2), (2, 7, 5), (2, 8, 7), (2, 10, 7), (2, 3, 6),
             (3, 6, 4), (3, 7, 5), (3, 10, 0),
             (4, 5, 2), (4, 7, 3), (4, 8, 1), (4, 9, 4),
             (5, 6, 6), (5, 7, 6), (5, 8, 3), (5, 10, 3),
             (6, 7, 4), (7, 8, 7), (8, 9, 4)]
    for vertex in vertexes:
        graph.add_vertex(vertex)
    for edge in edges:
        graph.add_edge(edge)
    return graph


def test_calculate(graph):
    algorithm = PriemAndJanik(graph)
    node_target = [0, 2, 0, 3, 2, 4, 3, 1, 4, 3]
    edge_target = [(1,7,3,0), (4,7,3,0), (4,8,1,0), (4,5,2,0), (2,5,2,0), (5,10,3,0), (3,10,0,0), (6,7,4,0), (4,9,4,0)]
    result, edge_result = algorithm.calculate()
    print()
    print(f'Target: {node_target}')
    print(f'Result: {result}')
    print(f'Target: {edge_target}')
    print(f'Result: {edge_result}')
    assert result == node_target
    assert edge_result == edge_target

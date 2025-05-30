import pytest
from ...graph import Graph
from ...Algorithms.BreadthFirstSearch import BFS

@pytest.fixture
def graph():
    graph = Graph()
    graph.add_vertex_list([1,2,3,4,5,6,7,8,9])
    graph.add_edge_list([(1,2), (1,5), (2,6), (2,7), (2,3), (3,5), (3,8), (7,8), (7,9), (9,4)])
    return graph

def test_calculate(graph):
    algorithm = BFS()
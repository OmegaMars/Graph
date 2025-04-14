import pytest
from ...graph import Graph
from ...GraphOperations.trail_operations import TrailOperations

@pytest.fixture
def graph_f():
    graph = Graph()
    vertexes = [1, 2, 3, 4, 5]
    edges = [[1, 2], [1, 4], [2, 3], [2, 4], [3, 4], [4, 5]]
    for vertex in vertexes:
        graph.add_vertex(vertex)
    for edge in edges:
        graph.add_edge(edge)
    return graph

@pytest.fixture
def mini_graph():
    graph = Graph()
    vertexes = [1, 2, 3]
    edges = [[1, 2], [2, 3], [1, 3]]
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

@pytest.mark.parametrize("trail, result", [
    # ([[1, 2], [1, 3], [1, 4], [1, 5], [2, 3], [2, 4], [2, 5], [3, 4], [3, 5], [4, 5]], False),
    ([[1, 2], [2, 3], [3, 4], [4, 5]], True),
])
def test_check_if_trail_is_a_trail(graph_f, trail, result):
    trail_operations = TrailOperations(trail, graph_f)
    assert trail_operations.check_if_trail_is_a_trail() == result


@pytest.mark.parametrize("trail, result", [
    # ([[1, 2], [1, 3], [1, 4], [1, 5], [2, 3], [2, 4], [2, 5], [3, 4], [3, 5], [4, 5]], False),
    ([[1, 2], [2, 3], [3, 4], [4, 5]], False),
    ([[1, 4], [4, 2], [2, 1]], True)
])
def test_check_if_trail_is_a_cycle(graph_f, trail, result):
    trail_operations = TrailOperations(trail, graph_f)
    assert trail_operations.check_if_trail_is_a_cycle() == result


@pytest.mark.parametrize("trail, result", [
    # ([[1, 2], [2, 3], [3, 4], [4, 5]], False),
    # ([[1, 4], [4, 2], [2, 1]], False),
    # ([[1, 2], [1, 3], [1, 4], [1, 5], [2, 3], [2, 4], [2, 5], [3, 4], [3, 5], [4, 5]], False),
    ([[1, 2], [2, 3], [3, 1]], True),
    ([[1, 2], [2, 3]], False),
])
def test_check_cycle_for_Euler_Tour(mini_graph, trail, result):
    trail_operations = TrailOperations(trail, mini_graph)
    assert trail_operations.check_cycle_for_Euler_Tour() == result


@pytest.mark.parametrize("trail, result", [
    # ([[1, 2], [2, 3], [3, 4], [4, 5]], False),
    # ([[1, 4], [4, 2], [2, 1]], False),
    # ([[1, 2], [1, 3], [1, 4], [1, 5], [2, 3], [2, 4], [2, 5], [3, 4], [3, 5], [4, 5]], False),
    ([[1, 2], [2, 3], [3, 1]], True),
    ([[1, 2], [2, 3]], False),
])
def test_check_cycle_is_Hamiltonian_cycle_mini_graph(mini_graph, trail, result):
    trail_operations = TrailOperations(trail, mini_graph)
    assert trail_operations.check_cycle_is_Hamiltonian_cycle() == result


@pytest.mark.parametrize("trail, result", [
    ([[1, 2], [2, 3], [3, 4], [4, 5]], False),
    ([[1, 4], [4, 2], [2, 1]], False),
    ([[1, 2], [1, 3], [1, 4], [1, 5], [2, 3], [2, 4], [2, 5], [3, 4], [3, 5], [4, 5], [5, 1]], True),
    ([[1, 2], [2, 3], [3, 1]], False),
    ([[1, 2], [2, 3]], False),
])
def test_check_cycle_is_Hamiltonian_cycle(regular_graph, trail, result):
    trail_operations = TrailOperations(trail, regular_graph)
    assert trail_operations.check_cycle_is_Hamiltonian_cycle() == result

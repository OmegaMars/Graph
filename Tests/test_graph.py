import pytest
from ..graph import Graph

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

def test_create_graph(graph_f):
    graph = graph_f
    assert graph == graph_f

def test_create_regular_graph(regular_graph):
    graph = regular_graph
    assert graph == regular_graph

@pytest.mark.parametrize("edge, result", [
    ([1, 3], [[1, 2, 0, 0], [1, 4, 0, 0], [2, 3, 0, 0], [2, 4, 0, 0], [4, 5, 0, 0], [1, 3, 0, 0]]),
    ([1, 5], [[1, 2, 0, 0], [1, 4, 0, 0], [2, 3, 0, 0], [2, 4, 0, 0], [4, 5, 0, 0], [1, 5, 0, 0]]),
    ([5 ,3], [[1, 2, 0, 0], [1, 4, 0, 0], [2, 3, 0, 0], [2, 4, 0, 0], [4, 5, 0, 0], [5, 3, 0, 0]]),
])
def test_add_edge(graph_f, edge, result):
    graph_f.add_edge(edge)
    assert graph_f.edge_list == result

@pytest.mark.parametrize("edge, result", [
    ([4, 5], [[1, 2, 0, 0], [1, 4, 0, 0], [2, 3, 0, 0], [2, 4, 0, 0]]),
    ([1, 2], [[1, 4, 0, 0], [2, 3, 0, 0], [2, 4, 0, 0], [4, 5, 0, 0]]),
])
def test_delete_edge(graph_f, edge, result):
    graph_f.delete_edge(edge)
    assert graph_f.edge_list == result

@pytest.mark.parametrize("vertex, node_list, node_ids", [
    (6, [(1, ''), (2, ''), (3, ''), (4, ''), (5, ''), (6, '')], [1, 2, 3, 4, 5, 6]),
    (42, [(1, ''), (2, ''), (3, ''), (4, ''), (5, ''), (42, '')], [1, 2, 3, 4, 5, 42]),
])
def test_add_vertex(graph_f, vertex, node_list, node_ids):
    graph_f.add_vertex(vertex)
    assert graph_f.node_list == node_list
    assert graph_f.node_ids == node_ids

@pytest.mark.parametrize("vertex, node_list, node_ids, edge_list", [
    (1, [(2, ''), (3, ''), (4, ''), (5, '')], [2, 3, 4, 5], [[2, 3, 0, 0], [2, 4, 0, 0], [4, 5, 0, 0]]),
    (5, [(1, ''), (2, ''), (3, ''), (4, '')], [1, 2, 3, 4], [[1, 2, 0, 0], [1, 4, 0, 0], [2, 3, 0, 0], [2, 4, 0, 0]]),
])
def test_delete_vertex(graph_f, vertex, node_list, node_ids, edge_list):
    graph_f.delete_vertex(vertex)
    assert graph_f.node_list == node_list
    assert graph_f.node_ids == node_ids
    assert graph_f.edge_list == edge_list

@pytest.mark.parametrize("vertex, result", [
    (1, 2),
    (5, 1),
])
def test_get_degree(graph_f, vertex, result):
    assert graph_f.get_degree(vertex) == result

@pytest.mark.parametrize("result", [
    (4),
])
def test_get_number_off_nodes_with_odd_degree(graph_f, result):
    assert graph_f.get_number_off_nodes_with_odd_degree() == result

def test_check_if_graph_is_regular(graph_f):
    assert graph_f.check_if_graph_is_regular() == False

def test_check_if_graph_is_regular(regular_graph):
    assert regular_graph.check_if_graph_is_regular() == True

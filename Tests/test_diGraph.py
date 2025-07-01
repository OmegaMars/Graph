import pytest
import sys
from ..diGraph import DiGraph




@pytest.fixture
def di_graph():
    pass



@pytest.mark.parametrize("vertex, result", [
    (1, [(1, '')]),
])
def test_add_vertex_DiGraph(vertex, result):
    graph = DiGraph()
    graph.add_vertex(vertex)
    assert result == graph.node_list

@pytest.mark.parametrize("vertex", [
    ([1,2,3]),
    ('1'),
])
def test_add_vertex_DiGraph_raise_TypeError(vertex):
    graph = DiGraph()
    with pytest.raises(TypeError):
        graph.add_vertex(vertex)


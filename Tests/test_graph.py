import pytest
from ..graph import Graph, DiGraph

@pytest.mark.parametrize("vertex", "result", [
    (1, [1]),
])
def test_add_vertex_DiGraph(vertex, result):
    graph = DiGraph()
    graph.add_vertex(vertex)
    assert result == graph.node_list
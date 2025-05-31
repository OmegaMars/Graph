import graphviz as gv
from typing import Union, Optional, List, Tuple, Dict
import sys
if "pytest" in sys.modules:
    from ..graph import Graph
    from ..diGraph import DiGraph
else:
    from graph import Graph
    from diGraph import DiGraph

class GraphPlotter:
    def __init__(self):
        self.graph = None

    def plot_graph(
        self,
        graph: Union[Graph, DiGraph],
        highlight_edges: Optional[List[Tuple[int, int]]] = None,
        edge_color: str = 'red',
        show_weights: bool = False,
        show_capacities: bool = False,
        node_labels: Optional[Dict[int, str]] = None
    ):
        """
        Plots a Graph or DiGraph using graphviz.

        Supports edge weights and capacities in the format:
            (u, v), (u, v, weight), or (u, v, weight, capacity)

        Args:
            graph (Union[Graph, DiGraph]): The graph to plot.
            highlight_edges (Optional[List[Tuple[int, int]]]): Edges to highlight.
            edge_color (str): Color for highlighted edges.
            show_weights (bool): Whether to show edge weights.
            show_capacities (bool): Whether to show capacities (implies weights).
        """
        self.graph = graph
        g = gv.Graph(format='png') if isinstance(graph, Graph) else gv.Digraph(format='png')

        highlight_edges = highlight_edges or []

        def node_name(n):
            return node_labels.get(n, str(n)) if node_labels else str(n)

        # Add nodes
        for node in graph.node_ids:
            g.node(node_name(node))

        # Add edges with optional labels and highlighting
        for edge in graph.edge_list:
            u, v = edge[0], edge[1]
            label = ""

            if show_capacities and len(edge) >= 4:
                label = f"{edge[2]}/{edge[3]}"
            elif show_weights and len(edge) >= 3:
                label = str(edge[2])

            attrs = {}
            if label:
                attrs["label"] = label
            highlight_edges = [(e[0], e[1]) for e in highlight_edges]
            if (u, v) in highlight_edges or ((v, u) in highlight_edges and isinstance(graph, DiGraph)):
                attrs.update({"color": edge_color, "penwidth": "2"})
            g.edge(node_name(u), node_name(v), **attrs)

        g.render('graph', view=True)

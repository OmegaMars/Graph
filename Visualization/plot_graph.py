# import networkx
import graphviz as gv
# Networkx aus eigenem Objekt erzeugen.
# Gaphthis das exportierte von graphx darstellen.
from typing import Union
from graph import Graph
from diGraph import DiGraph

class GraphPlotter:
    def __init__(self):
        pass

    def plot_graph(self, graph:Union[Graph, DiGraph]):
        if isinstance(graph, Graph):
            g = gv.Graph(format='png')
        else:
            g = gv.Digraph(format='png')
        for node in graph.node_ids:
            g.node(str(node))
        for edge in graph.edge_list:
            g.edge(str(edge[0]), str(edge[1]))
        g.render('graph', view=True)

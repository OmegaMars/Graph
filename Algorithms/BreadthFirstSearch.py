
from ..diGraph import DiGraph
from ..graph import Graph
from typing import Union
import numpy as np

class BFS:
    def __init__(self, graph:Graph):
        self.graph = graph
        self.start_node = self.graph.node_ids[0]

    def calculate(self):
        result = []
        for node in self.graph.node_ids:
            # self.bfs()
            pass
        return result

    def bfs(self):
        pass
# 7.2
# In jeder itteration bekommt jede neue Node die id der itteration.
# Wenn ich in der BFS auf eine Node stoße, die bereits exploriert wurde, wurde ein cycle gefunden.
# ItterationsIDs stellt die Anzahl an Kanten da, die zwischen der Node und dem Start Node liegt.
# Wert der aktuellen Node + Wert der bereits erkundeten Node + Kante zwischen der aktuellen und der bereits erkannten Node.
# BFS von jeden Knoten aus. -> Kleinsten Cycle suchen.
# Itteration muss fertig gemacht werden, sonst können kleinere Cycles übersehen werden.
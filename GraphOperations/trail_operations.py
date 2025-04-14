from ..graph import Graph
from ..diGraph import DiGraph


class TrailOperations:
    def __init__(self, trail, graph):
        self.graph = graph
        self.trail = trail
        for index, edge in enumerate(self.trail):
            self.trail[index] = self.graph.check_edge(edge)
        if not self.check_if_all_edges_are_in_graph():
            raise ValueError("Not all given edges exist")
        self.check_if_trail_is_a_trail()

    def check_if_trail_is_a_trail(self):
        last_edge = []
        for edge in self.trail:
            if last_edge == []:
                last_edge = edge
            elif last_edge[1] != edge[0]:
                return False
            else:
                last_edge = edge
        return True

    def check_if_trail_is_a_cycle(self):
        first_node = self.trail[0][0]
        last_node = self.trail[len(self.trail) - 1][1]
        if first_node != last_node:
            return False
        return True

    def check_if_all_edges_are_in_graph(self) -> bool:
        for edge in self.trail:
            if edge not in self.graph.edge_list:
                if [edge[1], edge[0], edge[2], edge[3]] not in self.graph.edge_list:
                    return False
        return True

    def check_cycle_for_Euler_Tour(self) -> bool:
        """
        Checks if the trail is a closed cycle and passes every edge exactly once.
        """
        if not self.check_if_trail_is_a_cycle() or not self.check_if_all_edges_are_in_graph():
            return False
        used_edges = []
        all_edges = self.graph.edge_list
        result = False
        if type(self.graph) == Graph:
            if self.graph.get_number_off_nodes_with_odd_degree() > 0:
                return False
        else:
            if self.graph.get_number_of_nodes_where_incoming_not_equals_outgoing_degree() > 0:
                return False
        if self.trail[0][0] == self.trail[len(self.trail) - 1][1]:
            for edge in self.trail:
                if edge not in used_edges:
                    used_edges.append(edge)
                    try:
                        all_edges.remove(edge)
                    except ValueError:
                        try:
                            if type(self.graph) == Graph:
                                all_edges.remove([edge[1], edge[0], edge[2], edge[3]])
                        except ValueError:
                            pass
            if all_edges == []:
                result = True
        return result

    def check_cycle_is_Hamiltonian_cycle(self) -> bool:
        """
        Checks if the trail is a closed cycle and passes every edge at least once.
        """
        result = False
        if not self.check_if_trail_is_a_cycle() or not self.check_if_all_edges_are_in_graph():
            return False
        if self.check_cycle_for_Euler_Tour():
            return True
        used_nodes = []
        if self.trail[0][0] == self.trail[len(self.trail) - 1][2]:
            for edge in self.trail:
                if edge[0] not in used_nodes:
                    used_nodes.append(edge[0])
                if edge[1] not in used_nodes:
                    used_nodes.append(edge[1])
            used_nodes.sort()
            if used_nodes == self.graph.node_ids:
                result = True
        return result


# Global check if Graph is connected.
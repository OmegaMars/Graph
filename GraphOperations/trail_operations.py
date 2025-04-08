


class TrailOperations:
    def __init__(self, trail):
        self.trail = trail
        self.check_if_trail_is_a_trail()

    def check_if_trail_is_a_trail(self):
        last_edge = []
        for edge in self.trail:
            if last_edge == []:
                last_edge = edge
            elif last_edge[2] != edge[1]:
                raise ValueError("Giffen trail is not connected, so it is not a trail.")
            else:
                last_edge = edge

    def check_if_trail_is_a_cycle(self):
        first_edge = self.trail[0]
        last_edge = self.trail[len(self.trail) - 1]
        if first_edge != last_edge:
            raise ValueError("Giffen trail is not a cycle.")

    def check_cycle_for_Euler_Tour(self):
        self.check_if_trail_is_a_cycle()

    def check_cycle_is_Hamiltonian_cycle(self):
        self.check_if_trail_is_a_cycle()


# Global check if Graph is connected.
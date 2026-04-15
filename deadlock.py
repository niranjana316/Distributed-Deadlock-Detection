import networkx as nx

class WaitForGraph:
    def __init__(self):
        self.graph = nx.DiGraph()

    def add_edge(self, from_p, to_p):
        self.graph.add_edge(from_p, to_p)

    def detect_deadlock(self):
        try:
            cycle = nx.find_cycle(self.graph, orientation='original')
            return True, cycle
        except:
            return False, None

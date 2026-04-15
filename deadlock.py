import simpy
import networkx as nx
import random

class DistributedSystem:
    def __init__(self, env, num_processes):
        self.env = env
        self.num_processes = num_processes
        self.graph = nx.DiGraph()

    def process(self, pid):
        yield self.env.timeout(random.randint(1, 3))

        # randomly wait for another process
        wait_for = random.randint(0, self.num_processes - 1)

        if pid != wait_for:
            self.graph.add_edge(f"P{pid}", f"P{wait_for}")

    def run(self):
        for i in range(self.num_processes):
            self.env.process(self.process(i))

        self.env.run()

    def detect_deadlock(self):
        try:
            cycle = nx.find_cycle(self.graph, orientation='original')
            return True, cycle
        except:
            return False, None

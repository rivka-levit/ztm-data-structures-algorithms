class Graph:
    def __init__(self):
        self.count_nodes = 0
        self.adjacency = dict()

    def add_vertex(self, node):
        self.adjacency[node] = list()



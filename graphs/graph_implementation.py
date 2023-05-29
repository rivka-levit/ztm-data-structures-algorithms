class Graph:
    def __init__(self):
        self.count_nodes = 0
        self.adjacency = dict()

    def add_vertex(self, node):
        self.adjacency[node] = list()

    def add_edge(self, node_1, node_2):
        for node in (node_1, node_2):
            if node not in self.adjacency:
                self.add_vertex(node)

        self.adjacency[node_1].append(node_2)
        self.adjacency[node_2].append(node_1)



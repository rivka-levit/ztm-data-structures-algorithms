class Graph:
    def __init__(self):
        self.count_nodes = 0
        self.adjacency = dict()

    def add_vertex(self, node):
        self.adjacency[node] = list()
        self.count_nodes += 1

    def add_edge(self, node_1, node_2):
        self.adjacency[node_1].append(node_2)
        self.adjacency[node_2].append(node_1)

    def show_connections(self):
        all_nodes = self.adjacency.keys()
        for node in all_nodes:
            node_connections = self.adjacency[node]
            connections = ''
            for vertex in node_connections:
                connections += str(vertex) + ' '
            print(f'{str(node)} --> {connections}')


my_graph = Graph()
my_graph.add_vertex(0)
my_graph.add_vertex(1)
my_graph.add_vertex(2)
my_graph.add_vertex(3)
my_graph.add_vertex(4)
my_graph.add_vertex(5)
my_graph.add_vertex(6)
my_graph.add_edge(3, 1)
my_graph.add_edge(3, 4)
my_graph.add_edge(4, 2)
my_graph.add_edge(4, 5)
my_graph.add_edge(1, 2)
my_graph.add_edge(1, 0)
my_graph.add_edge(0, 2)
my_graph.add_edge(6, 5)

my_graph.show_connections()

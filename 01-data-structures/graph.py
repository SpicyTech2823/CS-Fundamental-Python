class Graph:
    def __init__(self):
        self.graph = {}

    # Add a node to the graph
    def add_node(self, node):
        if node not in self.graph:
            self.graph[node] = []

    # Add an undirected edge
    def add_edge(self, node1, node2):

        self.add_node(node1)
        self.add_node(node2)

        self.graph[node1].append(node2)
        self.graph[node2].append(node1)

    # Display graph
    def display(self):
        for node in self.graph:
            print(node, "Connect to", self.graph[node])


# Test
graph = Graph()

graph.add_edge("A", "B")
graph.add_edge("A", "C")
graph.add_edge("B", "D")
graph.add_edge("C", "D")

graph.display()
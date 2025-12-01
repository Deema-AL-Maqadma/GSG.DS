from Edge import Edge
# Represents a location (vertex) in the city map
class Vertex:
    def __init__(self, label):
        self.label = label
        self.edges = []  # List of outgoing edges

    # Adds a road to another location
    def add_edge(self, target_vertex, weight):
        self.edges.append(Edge(target_vertex, weight))

    # Removes a road to a specific location
    def remove_edge(self, target_vertex):
        self.edges = [e for e in self.edges if e.target != target_vertex]

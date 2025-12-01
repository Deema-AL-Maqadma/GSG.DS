# Represents a directed edge with a weight (travel time)
class Edge:
    def __init__(self, target, weight):
        self.target = target
        self.weight = weight
from Vertex import Vertex
# Represents the entire city map as a directed weighted graph
class Graph:
    def __init__(self):
        self.vertices = []  # List of all locations

    # Adds a new location to the map
    def add_vertex(self, label):
        if not any(v.label == label for v in self.vertices):
            self.vertices.append(Vertex(label))

    # Finds a location by its name
    def find_vertex(self, label):
        for v in self.vertices:
            if v.label == label:
                return v
        return None

    # Adds a road between two locations with travel time
    def add_edge(self, from_label, to_label, weight):
        from_vertex = self.find_vertex(from_label)
        to_vertex = self.find_vertex(to_label)
        if from_vertex and to_vertex:
            from_vertex.add_edge(to_vertex, weight)

    # Removes a road between two locations
    def remove_edge(self, from_label, to_label):
        from_vertex = self.find_vertex(from_label)
        to_vertex = self.find_vertex(to_label)
        if from_vertex and to_vertex:
            from_vertex.remove_edge(to_vertex)

    # Removes a location and all roads connected to it
    def remove_vertex(self, label):
        target_vertex = self.find_vertex(label)
        if target_vertex:
            self.vertices = [v for v in self.vertices if v != target_vertex]
            for v in self.vertices:
                v.remove_edge(target_vertex)

    # Breadth-First Search: returns all reachable locations from a starting point
    def bfs(self, start_label):
        start_vertex = self.find_vertex(start_label)
        if not start_vertex:
            return []

        visited = set()
        queue = [start_vertex]
        reachable = []

        while queue:
            vertex = queue.pop(0)
            if vertex.label not in visited:
                visited.add(vertex.label)
                reachable.append(vertex.label)
                for edge in vertex.edges:
                    if edge.target.label not in visited:
                        queue.append(edge.target)

        return reachable
    

    # Dijkstra without heap: finds shortest travel time from start to all other locations
    def dijkstra(self, start_label):
        # Find the starting vertex
        start_vertex = self.find_vertex(start_label)
        if start_vertex is None:
            return {}

        # Step 1: Initialize distances to infinity, except start vertex = 0
        distances = {}
        for vertex in self.vertices:
            distances[vertex.label] = float('inf')
        distances[start_label] = 0

        # Step 2: Create a set to track visited locations
        visited = set()

        # Step 3: Repeat until all vertices are visited
        while len(visited) < len(self.vertices):
            # Find the unvisited vertex with the smallest distance
            min_distance = float('inf')
            current_vertex = None
            for vertex in self.vertices:
                if vertex.label not in visited and distances[vertex.label] < min_distance:
                    min_distance = distances[vertex.label]
                    current_vertex = vertex

            # If no reachable vertex is found, break
            if current_vertex is None:
                break

            # Step 4: Visit neighbors and update their distances
            for edge in current_vertex.edges:
                neighbor = edge.target
                if neighbor.label not in visited:
                    new_distance = distances[current_vertex.label] + edge.weight
                    if new_distance < distances[neighbor.label]:
                        distances[neighbor.label] = new_distance

            # Step 5: Mark current vertex as visited
            visited.add(current_vertex.label)

        return distances
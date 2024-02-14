# project 2

class Graph:
    def __init__(self):
        """
        Initializes an empty graph.
        """
        self.vertices = {}

    def add_vertex(self, vertex):
        """
        This adds a vertex to the graph.
        """
        if vertex not in self.vertices:
            self.vertices[vertex] = set()
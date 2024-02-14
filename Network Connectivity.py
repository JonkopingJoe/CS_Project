# project 2

class Graph:
    def __init__(self):
        """
        Initialize an empty graph.
        """
        self.vertices = {}

    def add_vertex(self, vertex):
        """
        Add a vertex to the graph.
        """
        if vertex not in self.vertices:
            self.vertices[vertex] = set()
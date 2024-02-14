# project 2

class Graph:
    def __init__(self):
        """
        Initializes an empty graph.
        """
        self.vertices = {}

    

    def add_edge(self, vertex1, vertex2):
        if vertex1 not in self.vertices[vertex2] and vertex2 not in self.vertices[vertex1]:
            self.vertices[vertex1].append(vertex2)
            self.vertices[vertex2].append(vertex1)
        else:
            print('Edge already exists between the vertices.')

    def remove_edge(self, vertex1, vertex2):
        if vertex1 in self.vertices[vertex2] and vertex2 in self.vertices[vertex1]:
            self.vertices[vertex1].remove(vertex2)
            self.vertices[vertex2].remove(vertex1)
        else:
            print('Edge does not exist between the vertices.')





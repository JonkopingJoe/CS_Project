# project 2

class Graph:
    def __init__(self):
        self.adjacency_matrix = {}
        
    def add_vertex(self, vertex):
        if vertex not in self.adjacency_matrix:
            self.adjacency_matrix[vertex] = []
    
    def add_edge(self, vertex1, vertex2):
        if vertex1 in self.adjacency_matrix and vertex2 in self.adjacency_matrix:
            self.adjacency_matrix[vertex1].append(vertex2)
            self.adjacency_matrix[vertex2].append(vertex1)
    
    def get_adjacency_matrix(self):
        return self.adjacency_matrix
    

def is_network_connected(graph) -> bool:
    
    visited = set()
    stack = [next(iter(graph.adjacency_matrix))]
    while stack:
        vertex = stack.pop()
        if vertex not in visited:
            visited.add(vertex)
            stack.extend([v for v in graph.adjacency_matrix[vertex] if v not in visited])
    
    return len(visited) == len(graph.adjacency_matrix)

def connection_of_node(self, vertex) -> list: 
    keys_list = list(self.adjacency_matrix.keys()).sort()
    connections_of_vertex = self.adjacency_matrix[vertex].sort()
    
    connection_row = []

    for key in keys_list: 
        if key in connections_of_vertex: 
            connection_row.append(1)
        else: 
            connection_row.append(0)
    
    return connection_row




def get_adj_matrix(self) -> list:
    adj_matrix = []
    vertices_list = list(self.adjacency_matrix.keys()).sort()

    for vertex in vertices_list: 
        adj_matrix.append(self.connection_of_node(vertex))

    return adj_matrix







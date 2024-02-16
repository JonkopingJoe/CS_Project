# project 2

class Graph:
    def __init__(self):
        self.adjacency_matrix = {}

    # method to add a computer to the network
    def add_vertex(self, vertex):
        if vertex not in self.adjacency_matrix:
            self.adjacency_matrix[vertex] = []

    # method to add a path between two computers in the network
    def add_edge(self, vertex1, vertex2):
        if vertex1 in self.adjacency_matrix and vertex2 in self.adjacency_matrix:
            self.adjacency_matrix[vertex1].append(vertex2)
            self.adjacency_matrix[vertex2].append(vertex1)

    # method to sign a connection between individual computers as 1, otherwise as 0
    def connection_of_node(self, vertex) -> list:
        keys_list = sorted(list(self.adjacency_matrix.keys()))
        connections_of_vertex = sorted(self.adjacency_matrix[vertex])
        connection_row = []

        # looping through the list containing the nodes, appends 1 for every connection between nodes
        for key in keys_list:
            if key in connections_of_vertex:
                connection_row.append(1)
            else:
                connection_row.append(0)

        return connection_row
    
    # method to represent the adjacency matrix as a 2D array
    def get_adj_matrix(self) -> list:
        adj_matrix = []
        vertices_list = sorted(list(self.adjacency_matrix.keys()))

        for vertex in vertices_list:
            adj_matrix.append(self.connection_of_node(vertex))

        return adj_matrix

    """
    Function to check if all the nodes in the network are connected to each other
    Arg: Takes the network as the argument
    Returns: True if all the nodes are connected, False otherwise
    """
def is_network_connected(graph) -> bool:
    visited = set()
    stack = [next(iter(graph.adjacency_matrix))]
    while stack:
        vertex = stack.pop()
        if vertex not in visited:
            visited.add(vertex)
            stack.extend([v for v in graph.adjacency_matrix[vertex] if v not in visited])

    return len(visited) == len(graph.adjacency_matrix)


def is_network_connected2(graph) -> bool:
    num_of_connections = []
    for vertex in sorted(list(graph.adjacency_matrix.keys())):
        num_of_connections.append(graph.connection_of_node(vertex).count(1))

    return num_of_connections.count(1) <= 2 and num_of_connections.count(0) == 0




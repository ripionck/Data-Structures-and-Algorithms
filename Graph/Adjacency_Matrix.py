"""
An adjacency matrix is a 2D array of size V×V, where Vis the number of vertices. The element at row iii and column j is 1 if there is an edge from vertex i to vertex j, and 0 otherwise.
"""


# Adjacency Matrix representation
class Graph:
    def __init__(self, num_vertices):
        self.num_vertices = num_vertices
        self.adj_matrix = [[0] * num_vertices for _ in range(num_vertices)]

    def add_edge(self, u, v):
        self.adj_matrix[u][v] = 1
        # self.adj_matrix[v][u] = 1  # For undirected graph

    def display(self):
        for row in self.adj_matrix:
            print(row)


g = Graph(5)
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 2)
g.add_edge(1, 3)
g.display()

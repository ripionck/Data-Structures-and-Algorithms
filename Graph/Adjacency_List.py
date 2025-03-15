# Adjacency List representation

"""
An adjacency list is an array of lists. The index of the array represents a vertex, and each element in the list represents the vertices adjacent to that vertex.
"""


class Graph:
    def __init__(self, num_vertices):
        self.num_vertices = num_vertices
        self.adj_list = [[] for _ in range(num_vertices)]

    def add_edge(self, u, v):
        self.adj_list[u].append(v)
        # self.adj_list[v].append(u)  # For undirected graph

    def display(self):
        for i in range(self.num_vertices):
            print(f"{i}: {self.adj_list[i]}")


g = Graph(5)
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 2)
g.add_edge(1, 3)
g.display()

"""
Kruskal's Algorithm is another method for finding the minimum spanning tree of a weighted undirected graph. Instead of starting from a node, it initially treats each node as a separate tree and then iteratively merges the most diminutive trees.

Algorithm:

1. Initialize a forest where each node is a separate tree.

2. While there are more than one tree in the forest:

    - Find the most minor edge that connects two distinct trees.
    - Merge the two trees into one.
    
3. Continue this process until only one tree remains in the forest.
"""


def kruskal(graph, num_vertices):
    # Initialize parent array for disjoint set (each vertex is its own set)
    parent = list(range(num_vertices))
    # Initialize rank array for union by rank optimization
    rank = [0] * num_vertices

    def find(v):
        # Find set representative with path compression
        if parent[v] != v:
            parent[v] = find(parent[v])  # Recursively find and compress path
        return parent[v]

    def union(u, v):
        # Find roots of both vertices
        root_u = find(u)
        root_v = find(v)
        # If vertices are in different sets
        if root_u != root_v:
            # Union by rank: attach smaller rank tree under root of higher rank tree
            if rank[root_u] > rank[root_v]:
                parent[root_v] = root_u
            else:
                parent[root_u] = root_v
                # If ranks are same, increment rank of the root
                if rank[root_u] == rank[root_v]:
                    rank[root_v] += 1

    # Create sorted list of edges: (weight, source, destination)
    edges = sorted((weight, u, v)
                   for u in graph for v, weight in graph[u].items())
    # Initialize minimum spanning tree result
    mst = []

    # Process each edge in sorted order
    for weight, u, v in edges:
        # If including this edge doesn't create a cycle
        if find(u) != find(v):
            # Union the sets of vertices
            union(u, v)
            # Add edge to minimum spanning tree
            mst.append((u, v, weight))

    # Return the minimum spanning tree
    return mst


graph = {
    0: {1: 1, 2: 4},
    1: {0: 1, 2: 2, 3: 5},
    2: {0: 4, 1: 2, 4: 1},
    3: {1: 5, 4: 3},
    4: {2: 1, 3: 3}
}
print(kruskal(graph, 5))


"""
Time Complexity: O(E log E) or O(E log V)
Where:
    E = number of edges
    V = number of vertices

Breakdown:
1. Sorting edges: O(E log E)
2. Union-Find operations: O(E α(V)) where α is the inverse Ackermann function
(practically constant)
3. Overall complexity dominated by sorting: O(E log E)

Space Complexity: O(V + E)
Breakdown:
1. Parent array: O(V)
2. Rank array: O(V)
3. Edges list: O(E)
4. MST result: O(V-1)
"""

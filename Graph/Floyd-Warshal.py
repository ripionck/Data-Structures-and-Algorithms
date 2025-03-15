"""
Floyd-Warshall Algorithm finds the shortest paths between all pairs of vertices in a weighted directed graph, including graphs with negative edge weights (but no negative cycles).
This algorithm uses dynamic programming  to find shortest paths between all pairs of vertices. It can handle negative edge weights but not negative cycles . The algorithm is particularly efficient when the graph is dense (many edges) and we need all-pairs shortest paths.

Algorithm:
1. Initialize the distance matrix:
    - Set all direct edges from the input graph
    - Set distance from vertex to itself as 0
    - Set all other distances as infinity
2. Consider all vertices as intermediate vertices:
    - For each vertex k as intermediate
    - For each pair of vertices (i,j)
    - If path through k is shorter than direct path from i to j
    - Update distance[i][j] with the shorter path
3. The final matrix shows shortest distances between all pairs of vertices

Use cases:
- Network Routing - Finding all shortest paths in a network
- Geographic Information Systems (GIS)
- Traffic Flow Optimization
- Computer Networks - Router path calculation

Key Differences from Dijkstra's  algorithm:
- Works with negative edges (but no negative cycles)
- Finds all-pairs shortest paths in one execution
- Uses dynamic programming approach
- Time complexity is O(V³)
"""


def floyd_warshall(graph):
    # Get the number of vertices in the graph
    n = len(graph)
    # Create a 2D matrix filled with infinity for storing shortest distances
    dist = [[float('inf')] * n for _ in range(n)]

    # Initialize the distance matrix
    for i in range(n):
        for j in range(n):
            if i == j:
                # Distance from a vertex to itself is 0
                dist[i][j] = 0
            elif graph[i][j] is not None:
                # Copy direct edges from input graph
                dist[i][j] = graph[i][j]

    # Main Floyd-Warshall algorithm
    for k in range(n):  # For each vertex as intermediate
        for i in range(n):  # For each source vertex
            for j in range(n):  # For each destination vertex
                # If path through vertex k is shorter than current path
                if dist[i][k] + dist[k][j] < dist[i][j]:
                    # Update with the shorter path
                    dist[i][j] = dist[i][k] + dist[k][j]

    # Return the matrix of shortest distances
    return dist


inf = float('inf')
graph = [
    [0, 3, inf, 7],
    [8, 0, 2, inf],
    [5, inf, 0, 1],
    [2, inf, inf, 0]
]

all_pairs_shortest_paths = floyd_warshall(graph)
for row in all_pairs_shortest_paths:
    print(row)


"""
Time Complexity: O(V³)
Breakdown:
1. Initialization: O(V²)
2. Main triple nested loop: O(V³)
    • Each loop iterates V times
    • Total iterations = V * V * V

Space Complexity: O(V²)
Breakdown:
1. Distance matrix (dist): O(V²)
2. Input graph (not counted in auxiliary space): O(V²)
"""

"""
Bellman-Ford Algorithm finds the shortest paths in weighted graphs, even with opposing weight edges. It works by iteratively relaxing the edges in the chart.

Algorithm:
1. Initialize distance values to all nodes as infinity and set the distance to the starting node as 0.

2. Relax all edges (repeat |V| - 1 times):
    - For each edge (u,v) with weight w, if dist[u] + w < dist[v], update dist[v] = dist[u] + w

3. Check for negative-weight cycles:
    - If any relaxation step further reduces the distance, a negative-weight cycle exists.

###Use cases: Routing in Networks, Arbitrage Detection, Traffic Engineering

Key differences from Dijkstra's algorithm  (shown in context):
1. Can handle negative edge weights
2. Can detect negative cycles
3. Higher time complexity (O(V * E) vs O((V + E) log V))
4. Simpler implementation (no priority queue  needed)

"""


def bellman_ford(graph, num_vertices, start):
    # Initialize distances to all vertices as infinity
    distances = {i: float('infinity') for i in range(num_vertices)}
    # Set distance to start vertex as 0
    distances[start] = 0

    # Relax all edges |V| - 1 times
    for _ in range(num_vertices - 1):
        # For each vertex in the graph
        for u in range(num_vertices):
            # For each neighbor and its edge weight of current vertex
            for v, weight in graph[u].items():
                # If we can find a shorter path
                if distances[u] + weight < distances[v]:
                    # Update the shorter distance
                    distances[v] = distances[u] + weight

    # Check for negative weight cycles
    for u in range(num_vertices):
        # For each neighbor and its edge weight
        for v, weight in graph[u].items():
            # If we can still relax edges, there's a negative cycle
            if distances[u] + weight < distances[v]:
                raise ValueError("Graph contains a negative weight cycle")

    # Return the dictionary of shortest distances
    return distances


graph = {
    0: {1: 1, 2: 4},
    1: {2: 2, 3: 5},
    2: {3: 1},
    3: {4: 3},
    4: {2: -6}
}
print(bellman_ford(graph, 5, 0))


"""
Time Complexity: O(V * E)
Where:
    V = number of vertices
    E = number of edges

Breakdown:
1. Initialization: O(V)
2. Main relaxation loop: O(V * E)
    • Outer loop runs V-1 times
    • Inner loops check all edges
3. Negative cycle detection: O(E)
    • Total: O(V * E)

Space Complexity: O(V)
Breakdown:
1. Distances dictionary: O(V)
2. Input graph (not counted in auxiliary space): O(V + E)
"""

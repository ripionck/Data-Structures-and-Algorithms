"""
Dijkstra's Algorithm is a widely used and efficient algorithm for finding the shortest path between nodes in a weighted graph. It works by maintaining a set of tentative (not fixed) distances to every node and iteratively updating these distances based on the actual distances found.

Algorithm:
1. Initialize a distance table with tentative distances to all nodes, setting the space to the starting node as 0 and all others as infinity.
2. Set the starting node as the current node.
3. For each neighbor of the current node, calculate its tentative distance and update the distance table if a shorter path is found.
4. Mark the current node as visited.
5. Select the unvisited node with the smallest tentative distance, set it as the new current node, and repeat steps 3-5.
6. Continue this process until the destination node is marked as visited or until all nodes have been called.

Use cases: Navigation and Maps, Networking and Routing, Transportatin and Logistics
"""

import heapq


def dijkstra(graph, start):
    # Initialize priority queue with start vertex and distance 0
    pq = [(0, start)]
    # Create dictionary to store distances, initialize all vertices with infinity
    distances = {vertex: float('infinity') for vertex in graph}
    # Set distance to start vertex as 0
    distances[start] = 0

    # Continue while priority queue is not empty
    while pq:
        # Get vertex with minimum distance from priority queue
        current_distance, current_vertex = heapq.heappop(pq)

        # Skip if we've found a better path already
        if current_distance > distances[current_vertex]:
            continue

        # Examine all neighbors of current vertex
        for neighbor, weight in graph[current_vertex].items():
            # Calculate potential new distance through current vertex
            distance = current_distance + weight

            # If new distance is shorter than known distance
            if distance < distances[neighbor]:
                # Update distance to this neighbor
                distances[neighbor] = distance
                # Add neighbor to priority queue with new distance
                heapq.heappush(pq, (distance, neighbor))

    # Return dictionary of shortest distances to all vertices
    return distances


graph = {
    0: {1: 1, 2: 4},
    1: {0: 1, 2: 2, 3: 5},
    2: {0: 4, 1: 2, 4: 1},
    3: {1: 5, 4: 3},
    4: {2: 1, 3: 3}
}
print(dijkstra(graph, 0))

"""
Time Complexity: O((V + E) log V)
    • V = number of vertices
    • E = number of edges

Breakdown:
1. Initialization: O(V)
2. Main loop:
    • Each vertex can be processed once: O(V)
    • Each edge can be processed once: O(E)Heap operations cost O(log V)
    • Total: O((V + E) log V)

Space Complexity: O(V)
Breakdown:
    • Priority queue (pq): O(V)
    • Distances dictionary: O(V)
    • Input graph (not counted in auxiliary space): O(V + E)
"""

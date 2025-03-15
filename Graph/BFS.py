"""
Breath-First Search (BFS) is a fundamental graph traversal algorithm that explores all the vertices of a graph in breadthward motion. It starts from a selected node (or vertex) and explores all its neighbors at the present depth before moving on to nodes at the next depth level.
BFS can be represented using a queue data structure. 

Algorithm:
1. Begin with a starting node, mark it as visited, and enqueue it in a queue.
2. While the queue is not empty:
    - Dequeue a node from the queue.
    - Visit and process the node.
    - Enqueue all unvisited neighbors of the node.
3. Continue this process until all nodes are visited.

Use Cases: Shortest Path, Network Broadcasting, Web Crawling
"""

from collections import deque


def bfs(graph, start):
    # Initialize set to keep track of visited vertices
    visited = set()
    # Initialize queue with start vertex using collections.deque
    queue = deque([start])
    # Mark start vertex as visited
    visited.add(start)

    # Continue while there are vertices to process in queue
    while queue:
        # Get next vertex from front of queue
        vertex = queue.popleft()
        # Process current vertex (in this case, print it)
        print(vertex, end=' ')

        # Examine all neighbors of current vertex
        for neighbor in graph[vertex]:
            # If neighbor hasn't been visited yet
            if neighbor not in visited:
                # Mark neighbor as visited
                visited.add(neighbor)
                # Add neighbor to queue for later processing
                queue.append(neighbor)


graph = {
    0: [1, 2],
    1: [0, 2, 3],
    2: [0, 1, 4],
    3: [1, 4],
    4: [2, 3]
}
bfs(graph, 0)

"""
Time Complexity: O(V + E)
Where:
    V = number of vertices
    E = number of edges

Breakdown:
1. Each vertex is visited once: O(V)
2. Each edge is examined once: O(E)
3. Queue operations (append/popleft) are O(1)

Space Complexity: O(V)
Breakdown:
1. Visited set: O(V)
2. Queue: O(V) - at worst, can contain all vertices
3. Input graph (not counted in auxiliary space): O(V + E)
"""

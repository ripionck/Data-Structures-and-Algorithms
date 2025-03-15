"""
Prim’s Algorithm is a widely used algorithm for finding the minimum spanning tree of a weighted undirected graph. It starts from an arbitrary node and iteratively adds the closest unvisited node to the tree, ensuring that it forms a minimum-spanning tree.

Algorithm:

1. Initialize a tree with a single node (any arbitrary node).
2. While there are still nodes not in the tree:
    - Find the minimum-weight edge that connects a node in the tree to a node outside the tree.
    - Add the node with the minimum-weight edge to the tree.
3. Continue this process until all nodes are in the tree.
"""

import heapq


def prim(graph, start):
    # List to store MST edges in format (parent, vertex, weight)
    mst = []
    # Set to keep track of vertices already included in MST
    visited = set()
    # Initialize min heap with start vertex (weight, vertex, parent)
    min_heap = [(0, start, None)]

    # Continue until heap is empty
    while min_heap:
        # Get vertex with minimum edge weight from heap
        weight, vertex, parent = heapq.heappop(min_heap)

        # Process vertex if not already in MST
        if vertex not in visited:
            # Add vertex to visited set
            visited.add(vertex)
            # If not the start vertex, add edge to MST
            if parent is not None:
                mst.append((parent, vertex, weight))

            # Process all adjacent vertices
            for neighbor, edge_weight in graph[vertex].items():
                # Add unvisited neighbors to heap
                if neighbor not in visited:
                    heapq.heappush(min_heap, (edge_weight, neighbor, vertex))

    # Return the minimum spanning tree
    return mst


graph = {
    0: {1: 1, 2: 4},
    1: {0: 1, 2: 2, 3: 5},
    2: {0: 4, 1: 2, 4: 1},
    3: {1: 5, 4: 3},
    4: {2: 1, 3: 3}
}
print(prim(graph, 0))


"""
Time Complexity: O((V + E) log V)
    • V = number of vertices
    • E = number of edges

Breakdown:
1. Initialization: O(1)
2. Main loop:
    • Each vertex is processed once: O(V)
    • Each edge can be processed once: O(E)
    • Heap operations cost O(log V)
    • Total: O((V + E) log V)

Space Complexity: O(V + E)
Breakdown:
1. MST list: O(V) (stores V-1 edges)
2. Visited set: O(V)
3. Min heap: O(E) worst case
4. Input graph (not counted in auxiliary space): O(V + E)
"""

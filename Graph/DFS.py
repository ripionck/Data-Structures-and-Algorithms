"""
Depth-first Search (DFS) explores all the vertices of a graph by going as deep as possible along each branch before backtracking. It starts from a selected node and explores as far as possible along each branch before moving back.
DFS can be represented using a stack data structure. 

Algorithm:
1. Begin with a starting node and mark it as visited.
2. For each unvisited neighbor of the node:
    - Recur with the neighbor as the new starting node.
3. Continue this process until all nodes are visited.

Use cases: Cycle Detection, Topological Sorting, Maze Solving, Strongly Connected Components
"""


def dfs(graph, start, visited=None):
    # Initialize visited set if not provided (happens only in first call)
    if visited is None:
        visited = set()

    # Add current vertex to visited set
    visited.add(start)

    # Process current vertex (in this case, print it)
    print(start, end=' ')

    # Examine all neighbors of current vertex
    for neighbor in graph[start]:
        # Recursively visit unvisited neighbors
        if neighbor not in visited:
            dfs(graph, neighbor, visited)


graph = {
    0: [1, 2],
    1: [0, 2, 3],
    2: [0, 1, 4],
    3: [1, 4],
    4: [2, 3]
}
dfs(graph, 0)


"""
Time Complexity: O(V + E)
Where:
    V = number of vertices
    E = number of edges

Breakdown:
1. Each vertex is visited exactly once: O(V)
2. Each edge is examined exactly once: O(E)
3. Set operations (add, lookup) are O(1) (Time complexity )

Space Complexity: O(V)
Breakdown:
1. Visited set: O(V)
2. Recursion stack: O(V) in worst case (for a linear graph) (Call stack )
3. Input graph (not counted in auxiliary space): O(V + E)
"""

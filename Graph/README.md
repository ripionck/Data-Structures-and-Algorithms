A graph is a non-linear data structure consisting of **nodes (vertices)** and **edges** that represent relationships between entities. It is formally defined as a pair of sets $$ (V, E) $$, where $$ V $$ is the set of vertices and $$ E $$ is the set of edges connecting vertex pairs. Graphs are widely used in fields like computer networks, social systems, and route optimization due to their ability to model complex relational data.

---

## **Types of Graphs**

### **1. Based on Direction**

- **Directed Graph (Digraph):**

  - Edges have a direction, represented by arrows.
  - Example: Web links where one page links to another.
  - Representation: Adjacency matrix or list with directional information.

- **Undirected Graph:**
  - Edges have no direction; connections are bidirectional.
  - Example: Social networks where friendships are mutual.

---

### **2. Based on Edge Properties**

- **Weighted Graph:**

  - Edges have weights or costs associated with them (e.g., distances in maps).
  - Representation: Adjacency matrix with weights or a weighted adjacency list.

- **Unweighted Graph:**

  - All edges have equal weight or no weight.

- **Simple Graph:**

  - No self-loops or parallel edges.
  - Example: A triangle graph with three vertices and three edges.

- **Multigraph:**

  - Contains parallel edges (multiple edges between two vertices).
  - Example: Multiple roads connecting two cities.

- **Pseudo Graph:**
  - Contains self-loops (edges starting and ending at the same vertex).

---

### **3. Based on Cycles**

- **Cyclic Graph:**

  - Contains at least one cycle (a path that starts and ends at the same vertex).
  - Example: A triangle graph.

- **Acyclic Graph:**

  - Contains no cycles.
  - Example: Trees are acyclic graphs.

- **Directed Acyclic Graph (DAG):**
  - A directed graph with no cycles.
  - Used in scheduling problems, topological sorting, etc.

---

### **4. Based on Connectivity**

- **Connected Graph:**
  - All vertices are reachable from any other vertex.
- **Disconnected Graph:**

  - Some vertices cannot be reached from others.

- **Complete Graph:**
  - Every pair of vertices is connected by an edge.
- **Null Graph:**
  - Contains only vertices and no edges.

---

### **5. Special Types**

- **Bipartite Graph:**
  - Vertices can be divided into two distinct sets such that no two vertices within the same set are adjacent.
- **Planar Graph:**
  - Can be drawn on a plane without any edges crossing.
- **Cycle Graph:**

  - Each vertex is connected to exactly two other vertices, forming a single cycle.

- **Infinite Graph:**
  - Contains an infinite number of vertices or edges.

---

## **Graph Representations**

### Logical Structure

- **Linear structures**: Elements follow sequential order (e.g., arrays, linked lists).
- **Non-linear structures**:
  - **Trees**: Hierarchical relationships (parent-child nodes).
  - **Graphs**: Arbitrary connections between nodes, including cycles and multiple paths.

### Physical Implementation

- **Contiguous memory**: Uses arrays for storage (e.g., adjacency matrices).
- **Non-contiguous memory**: Uses linked lists or pointers (e.g., adjacency lists).

Most graph implementations combine arrays and linked lists. For example:  
| Representation | Description | Pros/Cons |
|------------------|-----------------------------------------------------------------------------|---------------------------------------------------------------------------|
| **Adjacency Matrix** | 2D array where `matrix[i][j] = 1` if an edge exists between nodes i and j. | Fast lookup ($$O(1)$$) but space-inefficient ($$O(V^2)$$) for sparse graphs. |
| **Adjacency List** | Array of linked lists, where each list stores a node’s neighbors. | Space-efficient ($$O(V + E)$$) but slower edge existence checks ($$O(V)$$). |

---

## Advanced Representations

Modern applications use specialized techniques for graph data:

- **Graph Databases**: Store nodes, edges, and properties (e.g., triple stores with subject-predicate-object relationships).
- **Machine Learning Models**:
  - **Graph Embeddings**: Map nodes/edges to low-dimensional vectors (e.g., DeepWalk, GraphSAGE).
  - **Graph Neural Networks (GNNs)**: Capture structural patterns using deep learning.

---

## Applications

- **Computer Networks**: Modeling device connections.
- **Transport Systems**: Shortest-path algorithms (e.g., Dijkstra’s).
- **Social Networks**: Analyzing user interactions.

Graphs provide unparalleled flexibility in modeling real-world systems, with ongoing research focused on improving their scalability and representation in AI applications.

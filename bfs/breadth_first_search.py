"""
Breadth-First Search:
- Imagine a graph as a social network, A BFS starting at you would first visit
  all of your immediate, direct friends (1 hop away), then all of their friends
  (2 hops away), then their friends (3 hops away), and so on.
- It explores the graph layer by layer, fanning out evenly from the starting point.


  Core Concept:
  - BFS uses a Queue data structure (First-In, First-Out or FIFO) to keep track
    of the nodes to visit next, and a visited Set to ensure it doesn't get stuck
    in an infinite loop by revisiting the same node twice.


Example Graph:

    A
   / \
  B   C
 /   / \
D   E   F


Complexity:
- Time Complexity: O(V + E) where:
    -> V is the number of vertices (nodes)
    -> E is the number of edges
- Space Complexity: O(V)
    -> because in the worst-case scenario (like a star-shaped graph), you might
    have to store almost all the nodes in the queue at the exact same time.


Use BFS if you want the shorted path, or if you know the target is relatively
close to the starting point
"""

from collections import deque


def bfs(graph: dict[str, list[str]], start_node: str) -> None:
    visited = set()
    queue = deque([start_node])

    visited.add(start_node)

    while queue:
        # pop the element from the front of the queue
        curr = queue.popleft()
        print(f"Visting node: {curr}")
        # check all neighbors of the current node
        for neighbor in graph[curr]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)


if __name__ == "__main__":
    graph = {
        "A": ["B", "C"],
        "B": ["A", "D"],
        "C": ["A", "E", "F"],
        "D": ["B"],
        "E": ["C"],
        "F": ["C"],
    }

    bfs(graph, "A")

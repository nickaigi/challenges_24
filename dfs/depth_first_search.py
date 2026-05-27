"""
Depth-First Search (DFS)
- Imagine exploring a maze by chosing one path and spriting down it as far as
  you can possibly can until you hit a dead end, bactracking only when you
  absolutely have to.
- Instead of working layer-by-layer like BFS, DFS dives deep into the graph first


Core Concept:

- DFS uses a Stack (Last-In, First-Out) because a stack processes the most recently
  discovered nodes first, it naturally dives the search downward before outward.
- DFS is often implemented recursively. At each node, DFS calls itself on its child
  nodes until there are no more to visit, and then it backtracks.
- We don't build a stack explicitly, instead we use recursion. Everytime a function
  calls itself, Python pushes that call onto its internal stack, which perfectly mimics
  the LIFO behavior we need.

  Step-by-step recursive DFS
  1. Visit the current node and mark it as visit
  2. Iterate through all of its unvisited neighbors
  3. Recursively call the DFS function on each neighbor immediately
"""


def dfs_recursive(graph: dict[str, list[str]], node: str, visited=None) -> None:
    if visited is None:
        visited = set()

    # step 1: Mark the current node as visited
    visited.add(node)
    print(f"Visiting node: {node}")

    # Step 2: Recursively visit all unvisited neighbors
    for neighbor in graph[node]:
        if neighbor not in visited:
            dfs_recursive(graph, neighbor, visited)


def dfs_iterative(graph: dict[str, list[str]], node: str) -> None:
    visited = set()  # Track visited nodes
    stack = [node]  # stack for DFS

    while stack:  # loop until stack is empty
        node = stack.pop()
        if node not in visited:
            visited.add(node)  # Mark node as visited
            print(f"Visiting node: {node}")  # print the current node
            stack.extend(reversed(graph[node]))


if __name__ == "__main__":
    # Define the decision tree as a dictionary
    graph = {
        "A": ["B", "C"],
        "B": ["D", "E"],
        "C": ["F", "G"],
        "D": ["H", "I"],
        "E": ["J", "K"],
        "F": ["L", "M"],
        "G": ["N", "O"],
        "H": [],
        "I": [],
        "J": [],
        "K": [],
        "L": [],
        "M": [],
        "N": [],
        "O": [],
    }

    print("DFS Traversal: ")
    dfs_recursive(graph, "A")

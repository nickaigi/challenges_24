from collections import deque


def bfs(tree: dict[str, list[str]], start: str) -> None:
    visited = set()
    queue = deque([start])
    while queue:
        curr = queue.popleft()
        print(curr, end=" ")
        for node in tree[curr]:
            if node not in visited:
                visited.add(node)
                queue.append(node)


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

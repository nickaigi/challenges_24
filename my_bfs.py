from collections import deque


def bfs(tree: dict[str, list[str]], start: str) -> None:
    visited = set()
    queue = deque([start])

    while queue:
        node = queue.popleft()

        if node not in visited:
            visited.add(node)
            print(node, end=" ")

            for n in tree[node]:
                if n not in visited:
                    queue.append(n)


if __name__ == "__main__":
    tree = {
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
        "N": [],
        "M": [],
        "O": [],
    }
    bfs(tree, "A")

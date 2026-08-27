def adjacency_matrix():
    V = 5
    matrix = [[0] * V for _ in range(V)]

    edges = [
        (0, 1),
        (0, 2),
        (1, 2),
        (1, 3),
        (2, 4),
        (3, 4),
    ]

    # undirected edge: mark both directions
    for u, v in edges:
        matrix[u][v] = 1
        matrix[v][u] = 1

    for row in matrix:
        print(row)


def adjacency_list():
    V = 5

    adj = [[] for _ in range(V)]

    edges = [
        (0, 1),
        (0, 2),
        (1, 2),
        (1, 3),
        (2, 4),
        (3, 4),
    ]

    for u, v in edges:
        adj[u].append(v)
        adj[v].append(u)

    for i in range(V):
        print(f"{i} -> {adj[i]}")


if __name__ == "__main__":
    print("adjacency_matrix")
    adjacency_matrix()
    print("adjacency_list")
    adjacency_list()

import heapq

GraphDict = dict[str, dict[str, int]]
Distances = dict[str, int | float]


def get_shortest_path(previous_nodes, destination):
    path = []
    current_node = destination
    while current_node is not None:
        path.append(current_node)
        current_node = previous_nodes[current_node]

    path.reverse()
    return path


def dijkstra(graph: GraphDict, start_node: str) -> tuple:
    distances_from_source: Distances = {node: float("inf") for node in graph}
    distances_from_source[start_node] = 0
    previous_nodes = {node: None for node in graph}
    visited = set()

    to_visit = [(0, start_node)]  # min-heap
    while to_visit:
        current_distance, current_node = heapq.heappop(to_visit)
        if current_node in visited:
            continue

        for neighbor, weight in graph[current_node].items():
            if neighbor in visited:
                continue

            distance = current_distance + weight
            if distance < distances_from_source[neighbor]:
                distances_from_source[neighbor] = distance
                previous_nodes[neighbor] = current_node
                heapq.heappush(to_visit, (distance, neighbor))
            visited.add(current_node)

    return distances_from_source, previous_nodes


def main() -> None:
    graph: GraphDict = {
        "A": {"B": 2, "C": 6},
        "B": {"A": 2, "C": 9, "D": 5},
        "C": {"A": 6, "B": 9, "D": 8},
        "D": {"B": 5, "C": 8},
    }
    # Expected:
    # (
    #   {'A': 0, 'B': 2, 'C': 6, 'D', 7}
    #   {'A': None, 'B': 'A', 'C': 'A', 'D': 'B'}
    # )
    assert (
        {"A": 0, "B": 2, "C": 6, "D": 7},
        {"A": None, "B": "A", "C": "A", "D": "B"},
    ) == dijkstra(graph, "A")


if __name__ == "__main__":
    main()

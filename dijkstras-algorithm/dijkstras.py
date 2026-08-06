def dijkstras_algorithm():

    def find_lowest_cost_node(costs):
        lowest_cost = float("inf")
        lowest_cost_node = None
        for node in costs:
            cost = costs[node]
            if cost < lowest_cost and node not in processed:
                lowest_cost = cost
                lowest_cost_node = node
        return lowest_cost_node

    graph, costs, parents = set_up()
    processed = set()

    node = find_lowest_cost_node(costs)
    while node:
        cost = costs[node]
        neighbors = graph[node]
        for n in neighbors.keys():
            new_cost = cost + neighbors[n]
            if costs[n] > new_cost:
                costs[n] = new_cost
        processed.add(node)
        node = find_lowest_cost_node(costs)


def set_up() -> tuple:
    graph = {}
    costs = {}
    parents = {}

    graph["start"] = {}
    graph["start"]["a"] = 6
    graph["start"]["b"] = 2

    graph["a"] = {}
    graph["a"]["fin"] = 1

    graph["b"] = {}
    graph["b"]["a"] = 3
    graph["b"]["fin"] = 5

    graph["fin"] = {}

    costs["a"] = 6
    costs["b"] = 2
    costs["fin"] = float("inf")

    parents["a"] = "start"
    parents["b"] = "start"
    parents["fin"] = None

    return graph, costs, parents


if __name__ == "__main__":
    graph, costs, parents = set_up()

# coding: utf-8

def bellman_ford(graph, start, goal):
    inf = 100
    cost = [inf for _ in range(len(graph))]
    cost[start] = 0
    prev = [None for _ in range(len(graph))]

    for edge_from, from_nodes in enumerate(graph):
        update = False
        for edge_to, edge_cost in enumerate(from_nodes):
            if cost[edge_from] != inf and edge_cost > 0 and cost[edge_to] > cost[edge_from] + edge_cost:
                cost[edge_to] = cost[edge_from] + edge_cost
                prev[edge_to] = edge_from

    path = [goal]
    while goal > start:
        goal = prev[goal]
        path.append(goal)

    return sorted(path)

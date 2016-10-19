# coding: utf-8

def dijkstras(graph, start, goal):
    max_cost = 100
    cost = [max_cost for _ in range(len(graph))]
    prev = [None for _ in range(len(graph))]
    visited = [False for _ in range(len(graph))]

    cost[start] = 0
    prev[start] = start
    node = start
    while True:
        min_cost = max_cost
        visited[node] = True
        next_node = -1
        for i in range(len(graph)):
            if visited[i] == True: continue
            if graph[node][i]:
                d = cost[node] + graph[node][i]
                if cost[i] > d:
                    cost[i] = d
                    prev[i] = node
            if min_cost > cost[i]:
                min_cost = cost[i]
                next_node = i
        node = next_node
        if next_node == -1: break

    path = [goal]
    while goal > start:
        goal = prev[goal]
        path.append(goal)

    return sorted(path)

# coding: utf-8

def breadth_first_search(graph, start, goal):
    queue = [start]
    path_list = [[start]]
    res = []
    min_len = goal

    while len(queue) > 0:
        node = queue.pop(0)
        path = path_list.pop(0)

        for x, i in enumerate(graph[node]):

            if i != 1 or x == node or x in path: continue

            temp_path = path[:]
            queue.append(x)
            temp_path.append(x)
            path_list.append(temp_path)

            if x != goal: continue

            if min_len > len(temp_path):
                res = [temp_path]
                min_len = len(temp_path)
            elif min_len == len(temp_path):
                res.append(temp_path)

    return res

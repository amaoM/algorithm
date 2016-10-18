# coding: utf-8

def depth_first_search(graph, node, goal, prev, path, path_list, min_len):
    for x, i in enumerate(graph[node]):
        temp_path = path[:]
        if i != 1 or x == prev or x in path: continue
        temp_path.append(x)
        path_list, min_len = depth_first_search(graph, x, goal, node, temp_path, path_list, min_len)

    if goal in path:
        if min_len > len(path):
            path_list = [path]
            min_len = len(path)
        elif min_len == len(path):
            path_list.append(path)

    return path_list, min_len

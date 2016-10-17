# coding: utf-8

def depth_first_search(graph, node = 0, prev = 0, path = [0]):
    for x, i in enumerate(graph[node]):
        temp_path = path[:]
        if i != 1 or x == prev or x in path: continue
        temp_path.append(x)
        depth_first_search(graph, x, node, temp_path)
    if 10 in path:
        print(path)

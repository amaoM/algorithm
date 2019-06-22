'''
input example:
20 7
0 1 2
0 2 5
1 2 4
1 3 6
1 4 10
2 3 2
3 5 1
4 5 3
4 6 5
5 6 9
1 0 2
2 0 5
2 1 4
3 1 6
4 1 10
3 2 2
5 3 1
5 4 3
6 4 5
6 5 9
'''

N, M = map(int, input().split())
G = [list(map(int, input().split())) for _ in range(N)]


def dijkstras(start, goal):
    cost = [[float('INF')] * M for _ in range(M)]
    for i, j, c in G:
        cost[i][j] = c
    v = [False] * M
    d = [float('INF')] * M
    d[start] = 0

    while True:
        k = -1
        for i in range(M):
            if v[i] is True:
                continue
            if k > -1 and d[i] >= d[k]:
                continue
            k = i
        if k == -1:
            break
        v[k] = True
        for i in range(M):
            if d[i] > d[k] + cost[k][i]:
                d[i] = d[k] + cost[k][i]


dijkstras(0, M - 1)

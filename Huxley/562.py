from heapq import *


def initGraphUndirected(v):
    graph = []
    for _ in range(v):
        graph.append([])
    return graph


def addEdge(graph, source, destiny, weight):
    graph[source].append((destiny, weight))
    graph[destiny].append((source, weight))


def dijkstra(graph, origin, destiny):
    pq = []
    visited = [False] * len(graph)
    dist = [float('inf')] * len(graph)
    dist[origin] = 0
    heappush(pq, (origin, 0))

    while len(pq) != 0:
        v = heappop(pq)
        e = v[0]

        if visited[e]:
            continue
        else:
            visited[e] = True

        for i in range(len(graph[e])):
            v = graph[e][i]
            if dist[e] + v[1] < dist[v[0]]:
                dist[v[0]] = dist[e] + v[1]
                heappush(pq, (v[0], dist[v[0]]))

    return dist[destiny]


for case in range(int(input())):
    n, m = [int(x) for x in input().split()]
    graph = initGraphUndirected(n + 1)

    for _ in range(m):
        u, v, c = [int(x) for x in input().split()]
        addEdge(graph, u, v, c)
    k = int(input())

    deliveries = [int(x) for x in input().split()]
    total = 0

    for deliver in deliveries:
        total += dijkstra(graph, 1, deliver) * 2

    print("caso {}: {}".format(case + 1, total))

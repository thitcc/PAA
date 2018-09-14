from heapq import heappush, heappop


def initGraph(v):
    graph = []
    for _ in range(v):
        graph.append([])
    return graph


def addEdge(graph, source, destiny, weight):
    graph[source].append((weight, destiny))
    graph[destiny].append((weight, source))


def dijkstra(graph, origin):
    pq = []
    visited = [False] * len(graph)
    dist = [float('inf')] * len(graph)
    dist[origin] = 0
    heappush(pq, (0, origin))

    while len(pq) != 0:
        v = heappop(pq)
        e = v[1]

        if visited[e]:
            continue
        else:
            visited[e] = True

        for i in range(len(graph[e])):
            v = graph[e][i]
            if dist[e] + v[0] < dist[v[1]]:
                dist[v[1]] = dist[e] + v[0]
                heappush(pq, (dist[v[1]], v[1]))

    return dist


for case in range(1, int(input()) + 1):
    n, m = [int(x) for x in input().split()]
    graph = initGraph(n + 1)

    for _ in range(m):
        u, v, c = [int(x) for x in input().split()]
        addEdge(graph, u, v, c)

    k = int(input())
    deliveries = [int(x) for x in input().split()]
    dist = dijkstra(graph, 1)
    total = 0

    for deliver in deliveries:
        total += dist[deliver] * 2

    print("caso {}: {}".format(case, total))

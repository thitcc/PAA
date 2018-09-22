from queue import *

visited = []
dist = []


def bfs(u, n):
    dist[u] = 0
    visited[u] = True

    q = Queue()
    q.put(u)

    while not q.empty():
        v = q.get()

        for w in g[v]:
            if dist[w] == -1:
                dist[w] = dist[v] + 1
                visited[w] = True
                q.put(w)

    return dist[n]


def initGraph(v):
    graph = []
    for _ in range(v):
        graph.append([])
    return graph


def addEdge(graph, source, destiny):
    graph[source].append(destiny)
    graph[destiny].append(source)


for case in range(int(input())):
    n, m = [int(x) for x in input().split()]
    g = initGraph(n + 1)
    for _ in range(m):
        u, v = [int(x) for x in input().split()]
        addEdge(g, u, v)
    visited = [False] * (n + 1)
    dist = [-1] * (n + 1)
    print(bfs(1, n))

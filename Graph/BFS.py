from queue import *

visited = []
dist = []


def bfs(u, n):  # n as the last node
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

    return dist[n]  # Or something else

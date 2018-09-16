import sys
sys.setrecursionlimit(20000)


class Kingdom:
    """Nlogônia"""

    graph = []
    taxes = []

    def __init__(self, v):
        self.initGraph(v)
        self.initTaxes()

    def initTaxes(self):
        self.taxes = [0]
        for i in input().split():
            self.taxes.append(i)

    def initGraph(self, v):
        for _ in range(v):
            self.graph.append([])

    def addEdge(self, source, destiny, distance):
        self.graph[source].append((distance, destiny))
        self.graph[destiny].append((distance, source))


def dfs(u):
    global resp, carriage
    visited[u] = True

    if carriage + kingdom.taxes[u] > capacity:
        kingdom.taxes[u] += carriage
        carriage = 0
    else:
        carriage += kingdom.taxes[u]
        kingdom.taxes[u] = 0

    carriage = kingdom.taxes[u]

    for v in kingdom.graph[u]:
        resp += v[0]  # Distance
        if not visited[v[1]]:
            dfs(v[1])


n, capacity = [int(x) for x in input().split()]
visited = [False] * (n + 1)
kingdom = Kingdom(n + 1)

for _ in range(n - 1):
    a, b, dist = [int(x) for x in input().split()]
    kingdom.addEdge(a, b, dist)

carriage = 0
resp = 0
dfs(1)
print(resp)

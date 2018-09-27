from heapq import *

connections = []

def process(vtx):
    taken[vtx] = True
    for j in range(len(graph[vtx])):
        v = graph[vtx][j]
        if not taken[v[1]]:
            heappush(pq, (v[0], v[1], vtx))

def prim():
    process(0)
    mst_cost = 0

    while len(pq) != 0:
        v = heappop(pq)
        if not taken[v[1]]:
            mst_cost += v[0]
            connections.append((v[0], v[1], v[2]))
            process(v[1])

    return mst_cost

def initGraph(v):
    graph = []
    for _ in range(v):
        graph.append([])
    return graph

def addEdge(graph, source, destiny, weight):
    graph[source].append((weight, destiny))
    graph[destiny].append((weight, source))

v, e, r = [int(x) for x in input().split()]
graph = initGraph(v)
taken = [False] * v
pq = []

for i in range(e):
    v1, v2, w = [int(x) for x in input().split()]
    addEdge(graph, v1, v2, w)


print('########################\n'
      'Minimum Cost:\n' + str(prim()) + '\n'
      '########################')

connections.sort()

print('Connections:')

for i in connections:
    print(i[2], i[1])

print('########################')

print('Pings:')

for i in range(len(connections)):
    print(str(i+1) + ': ' + str(connections[i][0] * 2 / r))

from heapq import *

graph = []  # init graph and stuff
taken = [False] * 5  # 5 as graph length
pq = []

def process(vtx):
    taken[vtx] = True
    for j in range(len(graph[vtx])):
        v = graph[vtx][j]
        if not taken[v[1]]:
            heappush(pq, (v[0], v[1]))

def prim():
    process(0)
    mst_cost = 0

    while len(pq) != 0:
        v = heappop(pq)
        if not taken[v[1]]:
            mst_cost += v[0]
            process(v[1])

    return mst_cost


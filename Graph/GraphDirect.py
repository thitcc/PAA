def initGraphDirect(v):
    graph = []
    for i in range(v):
        graph.append([])
    graph[0].append((1, 2))
    graph[0].append((2, 6))
    graph[0].append((3, 1))
    print(graph)


initGraphDirect(4)

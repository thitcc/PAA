class Graph:
    """Non-Directional graph"""
    adjList = []

    def __init__(self, vertex):
        for _ in range(vertex):
            self.adjList.append([])

    def addEdge(self, source, destiny, weight):
        self.adjList[source].append((destiny, weight))
        self.adjList[destiny].append((source, weight))


graph = Graph(4)
graph.addEdge(0, 1, 3)
graph.addEdge(0, 2, 5)

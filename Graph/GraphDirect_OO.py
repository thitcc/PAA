class Graph:
    """Directional graph"""
    def __init__(self, vertex):
        self.adjList = [[] for _ in range(vertex)]

    def addEdge(self, first, second, weight):
        self.adjList[first].append()
        self.adjList[second].append()




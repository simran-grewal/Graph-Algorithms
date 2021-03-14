from collections import defaultdict


class Graph:
    def __init__(self):
        self.graph = defaultdict(list)
        self.vertex = set()

    def getNumberOfVertices(self):
        return len(self.vertex)

    def getVertices(self):
        return self.vertex

    def addItem(self, source, destination):
        self.graph[source].append(destination)
        self.graph[destination].append(source)
        self.vertex.update([source, destination])

    def addItemDirected(self, source, destination):
        self.graph[source].append(destination)
        self.vertex.update([source, destination])

    def printGraph(self):
        for each_node in self.graph.keys():
            print(
                f"Node  = {each_node} and Neighbours = {self.graph.get(each_node)}"
            )

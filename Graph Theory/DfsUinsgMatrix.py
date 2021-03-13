#DFS using Adjacency matrix

class Graph:

    def __init__(self, vertex):
        self.vertex = vertex
        self.adj = [ [0 for j in range(vertex)] for i in range(vertex)]

    def addEdge(self, source, destination):
        self.adj[source][destination] = 1
        self.adj[destination][source] = 1

    def findConnectedComponents(self):

        '''Dictionary to store component number and corresponding components'''
        connected_components = {}
        isVisited = [False]*self.vertex
        component = 1

        for i in range(vertex):
            if not isVisited[i]:
                connected_components[component] = []
                self.DFS(i, isVisited, connected_components, component)
                component += 1
        return connected_components
    def DFS(self, start, isVisited, connected_components, component):

        '''If node is already visited'''
        if isVisited[start]:
            return

        isVisited[start] = True
        connected_components[component].append(start)

        '''Iterate over the neighbours'''
        for i in range(self.vertex):
            if self.adj[start][i] == 1:
                self.DFS(i, isVisited, connected_components, component)
        


#Create a Graph
vertex = 8

G = Graph(vertex)
G.addEdge(0, 1)
G.addEdge(2, 3)
G.addEdge(4, 5)
G.addEdge(4, 6)
G.addEdge(7, 7)


#Connected Components
components = G.findConnectedComponents()
print(components)





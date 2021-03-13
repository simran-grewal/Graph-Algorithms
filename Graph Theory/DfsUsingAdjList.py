from Graph import Graph

def dfs(visited, node, graph):
    if node in visited:return
    visited.append(node)

    for neighbour in graph[node]:
        dfs(visited, neighbour, graph)


G = Graph()
G.addItem('A', 'B')
G.addItem('B', 'C')
G.addItem('B', 'E')
G.addItem('C', 'D')
G.addItem('E', 'F')
G.printGraph()
visited = list()
dfs(visited, 'F', G.graph)
print(visited)
from Graph import Graph


def solve(G, graph, source):

    parent_vertex = dict.fromkeys(G.getVertices(), None)
    visited = list()
    queue = [source]

    while queue:
        vertex = queue.pop(0)
        neighbours = graph.get(vertex, [])

        for neighbour in neighbours:
            if neighbour not in visited:

                visited.append(neighbour)
                queue.append(neighbour)
                parent_vertex[neighbour] = vertex

    return parent_vertex


def reconstructedPath(source, destination, parent_vertex):
    parent = destination
    path = [destination]
    while parent:
        if parent == source:
            break
        node = parent_vertex[parent]
        path.append(node)
        parent = node

    return path[::-1] if parent == source else []


def bfs(G, source, destination):

    parent_vertex = solve(G, G.graph, source)

    return reconstructedPath(source, destination, parent_vertex)


G = Graph()
G.addItemDirected('A', 'B')
G.addItemDirected('B', 'C')
G.addItemDirected('C', 'E')
G.addItemDirected('C', 'D')
G.addItemDirected('A', 'F')
G.addItemDirected('G', 'H')

path = bfs(G, 'A', 'D')
print(path)
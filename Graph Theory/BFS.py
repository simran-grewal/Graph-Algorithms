from Graph import Graph


def solve(source, visited, graph):
    visited = list()
    queue = [source]

    visited.append(source)
    while queue:
        node = queue.pop(0)
        neighbours = graph.get(node)

        if not neighbours:
            continue

        for neighbour in neighbours:
            if neighbour not in visited:
                queue.append(neighbour)
                visited.append(neighbour)

    return (visited)


def bfs(source, graph):
    visited = []
    visited = solve(source, visited, graph)
    print(visited)


G = Graph()
G.addItemDirected('A', 'B')
G.addItemDirected('B', 'C')
G.addItemDirected('C', 'E')
G.addItemDirected('C', 'D')
G.addItemDirected('A', 'F')

G.printGraph()

bfs('A', G.graph)

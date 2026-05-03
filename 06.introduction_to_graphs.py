# adjencently list

graph = [
    [],
    [2, 4],
    [3],
    [1],
    [2]
]

print([graph[1]])

# list of eges
graph = [
    (1, 2),
    (1, 4),
    (4, 2),
    (3, 1)
]
print(graph[3])

g = [
    [3, 6],
    [2, 3, 4, 5, 6],
    [1, 4, 5],
    [0, 1, 5],
    [1, 2, 6],
    [1, 2, 3],
    [0, 1, 4],
]
g[3].append(6)
print(g[3])
g[6].append(3)
print(g[6])
child_nodes = g[1]
print(child_nodes)

# adjencently matrix
graph = [
    [0, 0, 0, 1, 0, 0, 1],  # 0
    [0, 0, 1, 1, 1, 1, 1],  # 1
    [0, 1, 0, 0, 1, 1, 0],  # 2
    [1, 1, 0, 0, 0, 1, 0],  # 3
    [0, 1, 1, 0, 0, 0, 1],  # 4
    [0, 1, 1, 1, 0, 0, 0],  # 5
    [1, 1, 0, 0, 1, 0, 0],  # 6
]
# Add an edge [3][6]= 1
graph[3][6] = 1
# List the children of node 1
child_nodes = graph[1]
print(child_nodes)
print(graph)


class Edge:
    def __init__(self, parent, child):
        self.parent = parent
        self.child = child


graph = [
    Edge(0, 3),
    Edge(0, 6),
]
# Add an ege {3 -> 6}
graph.append(Edge(3, 6))
# List the children of node 1
graph.append(Edge(1, 5))
child_nodes = [e for e in graph if e.parent == 1]
print(child_nodes)

graph = {
    'Sofia': ['Plovdiv', 'Ruse', 'Varna'],
    'Plovdiv': ['Ruse', 'Sofia'],
    'Ruse': ['Plovdiv', 'Varna'],
    'Varna': ['Ruse', 'Sofia']
}

# Adding a new edge
graph['Varna'].append('Plovdiv')
graph['Plovdiv'].append('Varna')

# All neighbohrs of node with id 'Sofia'
child_nodes = graph['Sofia']
print(child_nodes)
child_nodes = graph['Varna']
print(child_nodes)


# Numbering Graph Nodes = map table
# OOP - sotial media

# Graphs Traversal

# Depth-First Search (DFS)

def dfs(node, graph, visited):
    if node in visited:
        return

    visited.add(node)

    for child in graph[node]:
        dfs(child, graph, visited)

    print(node, end=' ')


graph = {
    1: [19, 21, 14],
    19: [7, 12, 31, 21],
    7: [1],
    12: [],
    31: [21],
    21: [14],
    14: [6, 23],
    23: [21],
    6: [],
}

visited = set()

for node in graph:
    dfs(node, graph, visited)


def dfs(node, graph, visited):
    if visited[node]:
        return

    visited[node] = True
    for child in graph[node]:
        dfs(child, graph, visited)

    print(node, end=' ')


graph = [
    [3, 6],
    [3, 6, 4, 2, 5],
    [1, 4, 5],
    [5, 0, 1],
    [1, 2, 6],
    [2, 1, 3],
    [0, 1, 4]
]

visited = [False] * len(graph)

for node in range(len(graph)):
    dfs(node, graph, visited)

# breadth-First Search(BFS)
from collections import deque

from collections import deque


def bfs(node, graph, visited):
    if node in visited:
        return

    queue = deque([node])
    visited.add(node)

    while queue:
        current_node = queue.popleft()
        print(current_node, end=' ')

        for child in graph[current_node]:
            if child not in visited:
                visited.add(child)
                queue.append(child)


graph = {
    1: [19, 21, 14],
    19: [7, 12, 31, 21],
    7: [1],
    12: [],
    31: [21],
    21: [14],
    14: [6, 23],
    23: [21],
    6: [],
}

visited = set()

for node in graph:
    bfs(node, graph, visited)


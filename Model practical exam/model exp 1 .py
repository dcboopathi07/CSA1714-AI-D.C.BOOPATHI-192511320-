def dls(graph, node, goal, depth, path):
    if node == goal:
        print("Path:", path + [node])
        return True

    if depth <= 0:
        return False

    for child in graph[node]:
        if dls(graph, child, goal, depth - 1, path + [node]):
            return True

    return False


graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': [],
    'F': []
}

for depth in range(5):
    if dls(graph, 'A', 'F', depth, []):
        break

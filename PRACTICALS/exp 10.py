
# A* Search Algorithm

graph = {
    'A': [('B', 1), ('C', 3)],
    'B': [('D', 3), ('E', 1)],
    'C': [('F', 5)],
    'D': [],
    'E': [('G', 2)],
    'F': [('G', 2)],
    'G': []
}

h = {
    'A': 5, 'B': 4, 'C': 4,
    'D': 2, 'E': 1, 'F': 2, 'G': 0
}

def astar(start, goal):
    open_list = [(h[start], 0, start, [start])]
    visited = set()

    while open_list:
        open_list.sort()
        f, g, node, path = open_list.pop(0)

        if node == goal:
            print("Path:", path)
            print("Total Cost:", g)
            return

        if node in visited:
            continue
        visited.add(node)

        for neighbor, cost in graph[node]:
            if neighbor not in visited:
                new_g = g + cost
                new_f = new_g + h[neighbor]
                open_list.append(
                    (new_f, new_g, neighbor, path + [neighbor])
                )

    print("No path found")

astar('A', 'G')

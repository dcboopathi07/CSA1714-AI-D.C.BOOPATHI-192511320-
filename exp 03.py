
from collections import deque

def water_jug():
    capacity1 = 4
    capacity2 = 3
    target = 2

    queue = deque([(0, 0, [])])
    visited = set()

    while queue:
        x, y, path = queue.popleft()

        if (x, y) in visited:
            continue
        visited.add((x, y))

        path = path + [(x, y)]

        if x == target or y == target:
            print("Solution:")
            for state in path:
                print(state)
            return

        next_states = [
            (capacity1, y),  # Fill jug 1
            (x, capacity2),  # Fill jug 2
            (0, y),          # Empty jug 1
            (x, 0),          # Empty jug 2
            (x - min(x, capacity2-y), y + min(x, capacity2-y)),
            (x + min(y, capacity1-x), y - min(y, capacity1-x))
        ]

        for state in next_states:
            if state not in visited:
                queue.append((state[0], state[1], path))

water_jug()

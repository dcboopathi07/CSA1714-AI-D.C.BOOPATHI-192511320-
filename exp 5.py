from collections import deque

def is_valid(m, c):
    # Number of people must be within limits
    if m < 0 or m > 3 or c < 0 or c > 3:
        return False

    # Missionaries must not be outnumbered by cannibals
    if m > 0 and c > m:
        return False

    # On the other side
    m2 = 3 - m
    c2 = 3 - c

    if m2 > 0 and c2 > m2:
        return False

    return True


def solve():
    # State = (missionaries_left, cannibals_left, boat_position)
    # boat_position: 0 = left, 1 = right

    start = (3, 3, 0)
    goal = (0, 0, 1)

    queue = deque([(start, [start])])
    visited = {start}

    # Possible boat movements
    moves = [
        (1, 0),  # 1 missionary
        (2, 0),  # 2 missionaries
        (0, 1),  # 1 cannibal
        (0, 2),  # 2 cannibals
        (1, 1)   # 1 missionary + 1 cannibal
    ]

    while queue:
        state, path = queue.popleft()

        if state == goal:
            print("Solution:")
            for step in path:
                print(step)
            return

        m, c, boat = state

        for dm, dc in moves:

            if boat == 0:
                new_m = m - dm
                new_c = c - dc
                new_boat = 1
            else:
                new_m = m + dm
                new_c = c + dc
                new_boat = 0

            new_state = (new_m, new_c, new_boat)

            if is_valid(new_m, new_c) and new_state not in visited:
                visited.add(new_state)
                queue.append((new_state, path + [new_state]))

    print("No solution found.")


solve()

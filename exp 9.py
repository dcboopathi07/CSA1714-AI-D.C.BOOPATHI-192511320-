
# Travelling Salesman Problem

from itertools import permutations

dist = [
    [0, 10, 15, 20],
    [10, 0, 35, 25],
    [15, 35, 0, 30],
    [20, 25, 30, 0]
]

n = len(dist)
cities = range(1, n)

min_cost = float('inf')
best_path = []

for path in permutations(cities):
    cost = dist[0][path[0]]
    for i in range(len(path) - 1):
        cost += dist[path[i]][path[i + 1]]
    cost += dist[path[-1]][0]

    if cost < min_cost:
        min_cost = cost
        best_path = [0] + list(path) + [0]

print("Shortest Path:", best_path)
print("Minimum Cost:", min_cost)

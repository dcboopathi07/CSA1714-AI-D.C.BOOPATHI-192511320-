
# Map Coloring using CSP

colors = ['Red', 'Green', 'Blue']

regions = {
    'A': ['B', 'C'],
    'B': ['A', 'C', 'D'],
    'C': ['A', 'B', 'D'],
    'D': ['B', 'C']
}

assignment = {}

def is_valid(region, color):
    for neighbor in regions[region]:
        if assignment.get(neighbor) == color:
            return False
    return True

def solve():
    if len(assignment) == len(regions):
        return True

    region = next(r for r in regions if r not in assignment)

    for color in colors:
        if is_valid(region, color):
            assignment[region] = color

            if solve():
                return True

            del assignment[region]

    return False

if solve():
    print("Map Coloring Solution:")
    for region, color in assignment.items():
        print(region, ":", color)
else:
    print("No solution exists")

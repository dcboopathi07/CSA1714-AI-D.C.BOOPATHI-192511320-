def minimax(depth, nodeIndex, maximizingPlayer, values, targetDepth):
    if depth == targetDepth:
        return values[nodeIndex]

    if maximizingPlayer:
        best = float('-inf')
        for i in range(2):
            val = minimax(depth + 1, nodeIndex * 2 + i,
                          False, values, targetDepth)
            best = max(best, val)
        return best
    else:
        best = float('inf')
        for i in range(2):
            val = minimax(depth + 1, nodeIndex * 2 + i,
                          True, values, targetDepth)
            best = min(best, val)
        return best


values = [3, 5, 2, 9, 12, 5, 23, 23]
targetDepth = 3

result = minimax(0, 0, True, values, targetDepth)
print("The optimal value is:", result)

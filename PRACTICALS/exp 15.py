
def alphabeta(values):
    alpha = float('-inf')
    beta = float('inf')

    for i in values:
        alpha = max(alpha, i)
        if beta <= alpha:
            break

    return alpha

values = [3, 5, 2, 9, 1]
print("Best Value:", alphabeta(values))


import math

# Mini-Max Algorithm with Alpha-Beta Pruning
def minimax(depth, node, maximizingPlayer, alpha, beta):

    # Leaf node condition
    if depth == 3:
        return scores[node]

    if maximizingPlayer:
        best = -math.inf

        for i in range(2):
            value = minimax(depth + 1, node * 2 + i,
                            False, alpha, beta)

            best = max(best, value)
            alpha = max(alpha, best)

            if beta <= alpha:
                break

        return best

    else:
        best = math.inf

        for i in range(2):
            value = minimax(depth + 1, node * 2 + i,
                            True, alpha, beta)

            best = min(best, value)
            beta = min(beta, best)

            if beta <= alpha:
                break

        return best


# Racing route scores
scores = [3, 5, 6, 9, 1, 2, 0, -1]

# Main program
print("Racing Game")
print("Mini-Max Algorithm with Alpha-Beta Pruning")

best_score = minimax(0, 0, True, -math.inf, math.inf)

print("Best Route Score:", best_score)

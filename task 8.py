
def isSafe(board, row, col):

    # Check upper diagonal (left side)
    for i in range(row):
        if abs(board[i] - col) == abs(i - row):
            return False

    return True


# Main program
board = [0, 1]

print("Position of First Queen: (0,0)")
print("Position of Second Queen: (1,1)")

if isSafe(board, 1, 1):
    print("Second Queen is Safe")
else:
    print("Second Queen is Unsafe")
    print("Reason: Both queens are on the same diagonal.")

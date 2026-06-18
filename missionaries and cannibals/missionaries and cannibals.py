def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 5)

def is_winner(board, player):
    for row in board:
        if all(cell == player for cell in row):
            return True

    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True

    if all(board[i][i] == player for i in range(3)):
        return True

    if all(board[i][2 - i] == player for i in range(3)):
        return True

    return False

def is_full(board):
    return all(cell != " " for row in board for cell in row)

def minimax(board, is_max):
    if is_winner(board, "X"):
        return 1

    if is_winner(board, "O"):
        return -1

    if is_full(board):
        return 0

    if is_max:
        best = -100

        for i in range(3):
            for j in range(3):
                if board[i][j] == " ":
                    board[i][j] = "X"
                    best = max(best, minimax(board, False))
                    board[i][j] = " "

        return best

    else:
        best = 100

        for i in range(3):
            for j in range(3):
                if board[i][j] == " ":
                    board[i][j] = "O"
                    best = min(best, minimax(board, True))
                    board[i][j] = " "

        return best

def best_move(board):
    best_score = -100
    move = (-1, -1)

    for i in range(3):
        for j in range(3):
            if board[i][j] == " ":
                board[i][j] = "X"
                score = minimax(board, False)
                board[i][j] = " "

                if score > best_score:
                    best_score = score
                    move = (i, j)

    return move

board = [
    ["X", "O", "X"],
    ["O", "X", " "],
    [" ", " ", "O"]
]

print_board(board)

row, col = best_move(board)
print("Best Move:", row, col)
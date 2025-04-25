import numpy as np
def is_valid(board):
    n = len(board)
    for i in range(n):
        for j in range(i + 1, n):
            if board[i] == board[j]:
                return False
            if abs(board[i] - board[j]) == abs(i - j):
                return False
    return True
def random_8_queens():
    while True:
        board = np.random.permutation(8)
        if is_valid(board):
            print(board)
            return board
def print_board(board):
    n = len(board)
    chessboard = np.zeros((n, n), dtype=str)
    for i in range(8):
        for j in range(8):
            if i+j%2==0:
                chessboard[i,j] = 'B'
            else:
                chessboard[i,j] = 'W'
    for row in range(n):
        col = board[row]
        chessboard[row, col] = '👑'
    for row in chessboard:
        print(" ".join(row))
    print()
solution = random_8_queens()
print("Solution:")
print_board(solution)
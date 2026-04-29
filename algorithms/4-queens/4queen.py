from collections import deque

def is_valid(board, row, col):

    for i in range(row):
        if board[i] == col:
            return False

    for i in range(row):
        if abs(board[i] - col) == abs(i - row):
            return False

    return True

def solve_nqueens():
    queue = deque()
    queue.append([])  
    solutions = []

    while queue:
        board = queue.popleft()

        if len(board) == 4:
            solutions.append(board)
            continue

        row = len(board)

        for col in range(8):
            if is_valid(board, row, col):
                new_board = board + [col]
                queue.append(new_board)

    return solutions

solutions = solve_nqueens()

for index, solution in enumerate(solutions):
    board = [['.'] * 8 for _ in range(8)]
    for row, col in enumerate(solution):
        board[row][col] = 'Q'

    print(f"Solution {index+1}:")
    for row in board:
        print(' '.join(row))
    print()

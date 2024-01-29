#!/usr/bin/python3
"""
Program to solve n queens problem
"""
import sys

def is_safe(board, row, col):
    """Checks if a queen can be placed safely at a given position."""
    for i in range(col):
        if board[row][i] == 1:  # Check for queens in the same column
            return False

    # Check diagonals
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False
    for i, j in zip(range(row, len(board), 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    return True

def print_solution(board):
    """Prints the solution in the required format."""
    print([[i, row.index(1)] for i, row in enumerate(board)])

def solve_n_queens_util(board, col):
    """Recursively solves the N queens problem using backtracking."""
    if col >= len(board):
        print_solution(board)  # Print the solution
        return

    for i in range(len(board)):
        if is_safe(board, i, col):
            board[i][col] = 1
            solve_n_queens_util(board, col + 1)
            board[i][col] = 0  # Backtrack

def solve_n_queens(N):
    """Initializes the board and calls the recursive solver."""
    board = [[0 for _ in range(N)] for _ in range(N)]
    solve_n_queens_util(board, 0)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N", file=sys.stderr)
        sys.exit(1)

    try:
        N = int(sys.argv[1])
    except ValueError:
        print("N must be a number", file=sys.stderr)
        sys.exit(1)

    if N < 4:
        print("N must be at least 4", file=sys.stderr)
        sys.exit(1)

    solve_n_queens(N)

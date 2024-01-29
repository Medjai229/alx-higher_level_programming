#!/usr/bin/python3
"""
Program to solve n queens problem
"""
import sys

def is_safe(board, row, col, n):
    """
    checks if there is a queen in the same column
    """
    for i in range(row):
        if board[i] == col or \
            board[i] - 1 == col - row or \
            board[i] + 1 == col + row:
                return False
    return True

def print_solution(board):
    """
    print the output of the solution
    """
    n = len(board)
    solution = [[i, board[i]] for i in range(n)]
    print(solution)

def solve_nqueens_util(board, row, n):
    if row == n:
        print_solution(board)
        return

    for col in range(n):
        if is_safe(board, row, col, n):
            board[row] = col
            solve_nqueens_util(board, row + 1, n)

def solve_nqueens(n):
    if not isinstance(n, int):
        print("N must be a number")
        sys.exit(1)

    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    board = [-1] * n
    solve_nqueens_util(board, 0, n)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        N = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    solve_nqueens(N)

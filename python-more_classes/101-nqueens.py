#!/usr/bin/python3
"""
N Queens Problem Solver
Uses backtracking to find all valid solutions for placing N queens on an N×N board
"""

import sys


def is_safe(board, row, col):
    """
    Check if placing a queen at (row, col) is safe.
    A placement is safe if:
    - No queen exists in the same column
    - No queen exists on the same diagonals
    """
    # Check all previously placed queens (rows above current row)
    for i in range(row):
        # Check same column
        if board[i] == col:
            return False
        # Check diagonals (abs difference in rows == abs difference in cols)
        if abs(board[i] - col) == abs(i - row):
            return False
    return True


def solve(n, row, board, solutions):
    """
    Recursively solve N queens using backtracking.
    
    Args:
        n: Size of the board (N×N)
        row: Current row being processed
        board: List where board[i] = column position of queen in row i
        solutions: List to store all valid solutions
    """
    # Base case: all queens placed successfully
    if row == n:
        # Convert board representation to list of [row, col] positions
        solution = [[i, board[i]] for i in range(n)]
        solutions.append(solution)
        return

    # Try placing a queen in each column of the current row
    for col in range(n):
        if is_safe(board, row, col):
            # Place queen
            board[row] = col
            # Recurse to next row
            solve(n, row + 1, board, solutions)
            # Backtrack (implicit - no need to reset, next iteration will overwrite)


def main():
    # Validate number of arguments
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    # Validate N is a number
    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    # Validate N is at least 4
    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    # Initialize board: board[row] = column position of queen in that row
    board = [-1] * n
    solutions = []

    # Solve using backtracking
    solve(n, 0, board, solutions)

    # Print each solution
    for solution in solutions:
        print(solution)


if __name__ == "__main__":
    main()

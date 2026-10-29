#!/usr/bin/python3
"""
N Queens Solver using Backtracking.
"""
import sys


def validate_arguments():
    """Validates command line arguments."""
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    return n


def solve_nqueens(n):
    """Finds all solutions for the N Queens problem."""
    solutions = []

    def backtrack(row, current_solution):
        if row == n:
            solutions.append(list(current_solution))
            return

        for col in range(n):
            # Check if this column or diagonals conflict with existing queens
            safe = True
            for r, c in current_solution:
                # Same column or same diagonal check
                if c == col or abs(r - row) == abs(c - col):
                    safe = False
                    break

            if safe:
                current_solution.append([row, col])
                backtrack(row + 1, current_solution)
                current_solution.pop()

    backtrack(0, [])
    return solutions


if __name__ == "__main__":
    n = validate_arguments()
    solutions = solve_nqueens(n)
    for solution in solutions:
        print(solution)

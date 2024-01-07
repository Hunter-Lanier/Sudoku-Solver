import numpy as np

# Define the initial Sudoku board
board = np.array([[0,0,4,0,0,0,8,0,2],
                 [0,0,0,2,0,0,0,6,0],
                 [9,8,0,0,0,0,0,0,0],
                 [0,7,6,0,0,1,0,0,4],
                 [3,0,0,0,4,5,0,0,0],
                 [0,0,1,0,0,0,0,0,0],
                 [6,0,0,0,9,0,0,1,3],
                 [0,0,0,5,0,0,0,0,0],
                 [0,0,0,1,7,3,9,0,0]], dtype='object')

# Define the solved Sudoku board for comparison
solvedBoard = np.array([[5,6,4,7,1,9,8,3,2],
                        [7,1,3,2,5,8,4,6,9],
                        [9,8,2,4,3,6,1,7,5],
                        [2,7,6,9,8,1,3,5,4],
                        [3,9,8,6,4,5,7,2,1],
                        [4,5,1,3,2,7,6,9,8],
                        [6,4,7,8,9,2,5,1,3],
                        [1,3,9,5,6,4,2,8,7],
                        [8,2,5,1,7,3,9,4,6]], dtype='object')

def percentSolved(board, solvedBoard):
    """
    Calculate the percentage of the Sudoku board that has been solved.
    """
    count = 0
    for row in range(9):
        for col in range(9):
            if board[row][col] == solvedBoard[row][col]:
                count += 1
    return count / 81 * 100

def getAssociatedNumbers(board, row, col):
    """
    Get the numbers associated with a given cell in the Sudoku board.
    """
    associatedNumbers = []
    for i in range(9):
        if board[row][i] != 0:
            associatedNumbers.append(board[row][i])
    for i in range(9):
        if board[i][col] != 0:
            associatedNumbers.append(board[i][col])
    boxRow = row // 3
    boxCol = col // 3
    for i in range(boxRow * 3, boxRow * 3 + 3):
        for j in range(boxCol * 3, boxCol * 3 + 3):
            if board[i][j] != 0:
                associatedNumbers.append(board[i][j])

    return associatedNumbers


def solve(board):
    """
    Solve the Sudoku board using backtracking algorithm.
    """
    def is_valid(board, row, col, num):
        """
        Check if a number is valid to be placed in a given cell.
        """
        # Check row
        for i in range(9):
            if board[row][i] == num:
                return False
        # Check column
        for i in range(9):
            if board[i][col] == num:
                return False
        # Check box
        boxRow = (row // 3) * 3
        boxCol = (col // 3) * 3
        for i in range(boxRow, boxRow + 3):
            for j in range(boxCol, boxCol + 3):
                if board[i][j] == num:
                    return False
        return True

    def solve_helper(board):
        """
        Helper function to solve the Sudoku board recursively.
        """
        for row in range(9):
            for col in range(9):
                if board[row][col] == 0:
                    for num in range(1, 10):
                        if is_valid(board, row, col, num):
                            board[row][col] = num
                            if solve_helper(board):
                                return True
                            board[row][col] = 0
                    return False
        return True

    solve_helper(board)
    return board

# Solve the Sudoku board
board = solve(board)

# Print the solved board
print(board)

# Show percent accuracy
print(f"Accuracy: {percentSolved(board, solvedBoard)}%")

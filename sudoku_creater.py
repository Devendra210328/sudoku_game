
import numpy as np
import random
def is_valid(board, row, col, num):
    # Check if 'num' is not in the current row, column, and box
    return (
        all(num != board[row, i] for i in range(9)) and
        all(num != board[i, col] for i in range(9)) and
        all(num != board[i, j] for i in range(row - row % 3, row - row % 3 + 3) for j in range(col - col % 3, col - col % 3 + 3))
    )

def solve_sudoku(board):
    for i in range(9):
        for j in range(9):
            if board[i, j] == 0:
                for num in range(1, 10):
                    if is_valid(board, i, j, num):
                        board[i, j] = num
                        if solve_sudoku(board):
                            return True
                        board[i, j] = 0  # Backtrack if the current placement doesn't lead to a solution
                return False
    return True

def generate_sudoku(difficulty):
    # Create an empty Sudoku board (0 represents empty cells)
    board = np.zeros((9, 9), dtype=int)

    # create a list from 1 to 9 with randomness
    random_numbers = random.sample(range(1, 10), 9)
    
    for i in range(len(board[0])):
        board[0, i]=random_numbers[i]
    
    # Generate a solved Sudoku puzzle
    solve_sudoku(board)
    # print(board)
    # Remove numbers based on difficulty level
    cells_to_remove = (difficulty * 9)
    for _ in range(cells_to_remove):
        row, col = np.random.randint(0, 9, size=2)
        while board[row, col] == 0:
            row, col = np.random.randint(0, 9, size=2)
        board[row, col] = 0

    return board

# Example: Generate a Sudoku puzzle with difficulty level 3
# sudoku_puzzle = generate_sudoku(3)
# print(sudoku_puzzle)
# solved_sudoku=solve_sudoku(sudoku_puzzle)
# print(sudoku_puzzle)
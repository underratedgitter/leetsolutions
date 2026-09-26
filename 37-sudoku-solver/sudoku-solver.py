from typing import List, Optional, Tuple


class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        self.solve(board)

    def solve(self, board: List[List[str]]) -> bool:
        # Find the next empty cell
        row, col = self.find_empty(board)

        # If there are no empty cells, the puzzle is solved
        if row is None:
            return True

        # Try to place digits from 1 to 9 in the empty cell
        for digit in range(1, 10):
            if self.is_valid(board, row, col, str(digit)):
                board[row][col] = str(digit)

                # Recurse to solve the remaining puzzle
                if self.solve(board):
                    return True

                # If the recursion fails, backtrack and reset the cell
                board[row][col] = '.'

        # If no solution is found, return False
        return False

    def find_empty(self, board: List[List[str]]) -> Tuple[Optional[int], Optional[int]]:
        # Find the next empty cell
        for row in range(9):
            for col in range(9):
                if board[row][col] == '.':
                    return row, col
        return None, None

    def is_valid(self, board: List[List[str]], row: int, col: int, digit: str) -> bool:
        # Check if the digit is present in the same row or column
        if digit in board[row] or digit in [board[i][col] for i in range(9)]:
            return False

        # Check if the digit is present in the same 3x3 sub-box
        sub_row = (row // 3) * 3
        sub_col = (col // 3) * 3
        for i in range(sub_row, sub_row + 3):
            for j in range(sub_col, sub_col + 3):
                if board[i][j] == digit:
                    return False

        # If the digit is valid, return True
        return True
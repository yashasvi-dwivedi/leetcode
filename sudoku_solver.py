class Solution(object):
    def solveSudoku(self, board):
        # do not return anything, modify board in-place instead.
        def is_valid(board, row, col, num):
            # Check if the number is not in the current row
            for j in range(9):
                if board[row][j] == num:
                    return False

            # Check if the number is not in the current column
            for i in range(9):
                if board[i][col] == num:
                    return False

            # Check if the number is not in the current 3x3 box
            box_row_start = (row // 3) * 3
            box_col_start = (col // 3) * 3
            for i in range(box_row_start, box_row_start + 3):
                for j in range(box_col_start, box_col_start + 3):
                    if board[i][j] == num:
                        return False

            return True

        def solve(board):
            for i in range(9):
                for j in range(9):
                    if board[i][j] == ".":
                        for num in map(str, range(1, 10)):
                            if is_valid(board, i, j, num):
                                board[i][j] = num
                                if solve(board):
                                    return True
                                board[i][j] = "."
                        return False
            return True

        solve(board)


# Test the function
if __name__ == "__main__":
    board = [
        ["5", "3", ".", ".", "7", ".", ".", ".", "."],
        ["6", ".", ".", "1", "9", "5", ".", ".", "."],
        [".", "9", "8", ".", ".", ".", ".", "6", "."],
        ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
        ["4", ".", "6", "8", ".", "3", ".", ".", "1"],
        ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
        [".", "6", ".", ".", ".", "2", "8", ".", "."],
        [".", ".", ".", "4", "1", "9", ".", ".", "5"],
        [".", ".", ".", ".", "8", ".", ".", "7", "9"],
    ]
    solution = Solution()
    solution.solveSudoku(board)
    for row in board:
        print(row)
# Output:
# ['5', '3', '4', '6', '7', '8', '9', '1', '2']
# ['6', '7', '2', '1', '9', '5', '3', '4', '8']
# ['1', '9', '8', '3', '4', '2', '5', '6', '7']
# ['8', '5', '9', '7', '6', '1', '4', '2', '3']
# ['4', '2', '6', '8', '5', '3', '7', '9', '1']
# ['7', '1', '3', '9', '2', '4', '8', '5', '6']
# ['9', '6', '1', '5', '3', '7', '2', '8', '4']
# ['2', '8', '7', '4', '1', '9', '6', '3', '5']
# ['3', '4', '5', '2', '8', '6', '1', '7', '9']
# The above code solves the Sudoku puzzle and prints the solved board.

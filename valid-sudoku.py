# https://leetcode.com/problems/valid-sudoku/

# Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

#     Each row must contain the digits 1-9 without repetition.
#     Each column must contain the digits 1-9 without repetition.
#     Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.

# Note:

#     A Sudoku board (partially filled) could be valid but is not necessarily solvable.
#     Only the filled cells need to be validated according to the mentioned rules.

 

# Example 1:

# Input: board = 
# [["5","3",".",".","7",".",".",".","."]
# ,["6",".",".","1","9","5",".",".","."]
# ,[".","9","8",".",".",".",".","6","."]
# ,["8",".",".",".","6",".",".",".","3"]
# ,["4",".",".","8",".","3",".",".","1"]
# ,["7",".",".",".","2",".",".",".","6"]
# ,[".","6",".",".",".",".","2","8","."]
# ,[".",".",".","4","1","9",".",".","5"]
# ,[".",".",".",".","8",".",".","7","9"]]
# Output: true

# Example 2:

# Input: board = 
# [["8","3",".",".","7",".",".",".","."]
# ,["6",".",".","1","9","5",".",".","."]
# ,[".","9","8",".",".",".",".","6","."]
# ,["8",".",".",".","6",".",".",".","3"]
# ,["4",".",".","8",".","3",".",".","1"]
# ,["7",".",".",".","2",".",".",".","6"]
# ,[".","6",".",".",".",".","2","8","."]
# ,[".",".",".","4","1","9",".",".","5"]
# ,[".",".",".",".","8",".",".","7","9"]]
# Output: false
# Explanation: Same as Example 1, except with the 5 in the top left corner being modified to 8. Since there are two 8's in the top left 3x3 sub-box, it is invalid.

 

# Constraints:

#     board.length == 9
#     board[i].length == 9
#     board[i][j] is a digit 1-9 or '.'.

class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        valid_rows = self.is_valid_sudoku_on_rows(board)
        print(valid_rows)
        valid_cols = self.is_valid_sudoku_on_columns(board)
        print(valid_cols)
        valid_sub_boxes = self.is_valid_sudoku_on_sub_boxes(board)
        print(valid_sub_boxes)
        
        return valid_rows and \
            valid_cols and \
            valid_sub_boxes

    def is_valid_sudoku_on_rows(self, board):
        for row in board:
            if self.has_duplications(row) is True:
                return False
        return True

    def is_valid_sudoku_on_columns(self, board):
        for col_index in range(0, len(board[0])):
            nums_in_cols = []
            for row in board:
                nums_in_cols.append(row[col_index])
            if self.has_duplications(nums_in_cols) is True:
                print(nums_in_cols)
                return False
        return True

    def is_valid_sudoku_on_sub_boxes(self, board):
        row = 0
        col = 0
        # print(len(board))
        while row < len(board) and col < len(board[0]):
            box_nums = self.get_box_nums(board, col, row)
            
            if row >= 6:
                print(box_nums)

            if self.has_duplications(box_nums) is True:
                return False

            col += 3
            if col == len(board[0]):
                col = 0
                row += 3

            print(row)
            print(col)

        return True

    def get_box_nums(self, board, box_col, box_row):
        box_col_max = box_col + 3
        box_row_max = box_row + 3
        box_nums = []
        while box_col < box_col_max and box_row < box_row_max:
            box_nums.append(board[box_row][box_col])
            box_col += 1
            if box_col == box_col_max:
                box_col -= 3
                box_row += 1
        return box_nums


    def has_duplications(self, num_strs):
        for index in range(0, len(num_strs)):
            num_str = num_strs[index]
            if num_str >= "0" and num_str <= "9":
                if num_str in num_strs[index+1:len(num_strs)]:
                    return True
        return False
                

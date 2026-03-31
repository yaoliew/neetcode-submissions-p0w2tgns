class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # check each 3x3 square for repeats.
        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                square_contents = []
                for x in range(i, i+3):
                    for y in range(j, j+3):
                        if (board[x][y] != "."):
                            square_contents.append(board[x][y])
                if (len(square_contents) > len(set(square_contents))):
                    return False
        
        # check each column and row for repeats
        for i in range(len(board)):
            column_contents = []
            row_contents = []
            for j in range(len(board)):
                if (board[j][i] != "."):
                    column_contents.append(board[j][i])
                if (board[i][j] != "."):
                    row_contents.append(board[i][j])
            if (len(column_contents) > len(set(column_contents))):
                return False
            if (len(row_contents) > len(set(row_contents))):
                return False

        return True

    

class NumMatrix(object):

    def __init__(self, matrix):
        """
        :type matrix: List[List[int]]
        """
        ROWS,COLS = len(matrix), len(matrix[0])
        self.summatrix = [[0]* (COLS + 1) for i in range(0,ROWS+1)]
        for r in range(ROWS):
            prefix  = 0
            for c in range(COLS):
                prefix += matrix[r][c]
                above = self.summatrix[r][c+1]
                self.summatrix[r+1][c+1] = above + prefix


    def sumRegion(self, row1, col1, row2, col2):
        """
        :type row1: int
        :type col1: int
        :type row2: int
        :type col2: int
        :rtype: int
        """
        row1 = row1 + 1
        col1 = col1 + 1
        row2 = row2+ 1
        col2 = col2 + 1

        total = self.summatrix[row2][col2]
        top = self.summatrix[row1-1][col2]
        left = self.summatrix[row2][col1 - 1]
        topleft = self.summatrix[row1-1][col1-1]
        return total - top - left + topleft
        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)
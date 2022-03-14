class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        m, n = len(matrix), len(matrix[0]) if matrix else 0
        # 求前缀和
        self.pre_matrix = [(n + 1) * [0] for _ in range(m)]
        for i in range(m):
            for j in range(n):
                self.pre_matrix[i][j + 1] = self.pre_matrix[i][j] + matrix[i][j] 


    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        total = 0
        for row in range(row1, row2 + 1):
            total += self.pre_matrix[row][col2 + 1] - self.pre_matrix[row][col1]
        return total



# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)
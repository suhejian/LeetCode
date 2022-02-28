class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        total = 0
        for i in range(len(mat)):
            for j in range(len(mat)):
                # 主对角线
                if i == j:
                    total += mat[i][j]
                elif i + j == len(mat) - 1:
                    total += mat[i][j]
        return total
class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        n = len(matrix)
        # def find(matrix, index):
        #     dp = [[inf for i in range(n)] for j in range(n)]
        #     dp[0][index] = matrix[0][index]
        #     for i in range(1, n):
        #         for j in range(n):
        #             if j == 0:
        #                 # 只能由正上方或右上方移动过来
        #                 dp[i][j] = min(dp[i-1][j], dp[i-1][j+1]) + matrix[i][j]
        #             elif j == n-1:
        #                 # 只能由正上方或左上方移动过来
        #                 dp[i][j] = min(dp[i-1][j], dp[i-1][j-1]) + matrix[i][j]
        #             else:
        #                 dp[i][j] = min(dp[i-1][j], dp[i-1][j-1], dp[i-1][j+1]) + matrix[i][j]
        #     return min(dp[-1])
        # return min(find(matrix, index) for index in range(n))

        dp = [[inf for i in range(n)] for j in range(n)]
        for index in range(n):
            dp[0][index] = matrix[0][index]
        for i in range(1, n):
            for j in range(n):
                if j == 0:
                    # 只能由正上方或右上方移动过来
                    dp[i][j] = min(dp[i-1][j], dp[i-1][j+1]) + matrix[i][j]
                elif j == n-1:
                    # 只能由正上方或左上方移动过来
                    dp[i][j] = min(dp[i-1][j], dp[i-1][j-1]) + matrix[i][j]
                else:
                    dp[i][j] = min(dp[i-1][j], dp[i-1][j-1], dp[i-1][j+1]) + matrix[i][j]
        return min(dp[-1])
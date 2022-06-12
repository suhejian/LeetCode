class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        dp = [[0 for i in range(n)] for j in range(m)]
        dp[0][0] = grid[0][0]

        for i in range(m):
            for j in range(n):
                if i > 0 and j > 0:
                    dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + grid[i][j]
                elif i > 0:
                    # 只能向下移动
                    dp[i][j] = dp[i-1][j] + grid[i][j]
                elif j > 0:
                    dp[i][j] = dp[i][j-1] + grid[i][j]
        
        return dp[-1][-1]
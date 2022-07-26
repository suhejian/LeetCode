class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        visit = [[False] * n for _ in range(m)]

        def dfs(grid, r, c):
            # Bad case
            if r < 0 or r >= m or c < 0 or c >= n or grid[r][c] == 0 or visit[r][c]:
                return None
            visit[r][c] = True  # 该位置已经访问过
            for (x, y) in [(r-1, c), (r+1, c), (r, c-1), (r, c+1)]:
                dfs(grid, x, y)
        
        # 对边界进行dfs, 剩下的没访问过的陆地即为所求
        for i in range(m):
            dfs(grid, i, 0)
            dfs(grid, i, n-1)
        
        for j in range(n):
            dfs(grid, 0, j)
            dfs(grid, m-1, j)
        
        # 遍历网格, 统计有多少符合要求的陆地
        count = 0
        for i in range(m):
            for j in range(n):
                if not visit[i][j] and grid[i][j] == 1:
                    count += 1
        return count

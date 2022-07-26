class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        def isArea(grid, r, c):
            return 0 <= r < len(grid) and 0 <= c < len(grid[0])
        
        def dfs(grid, r, c):
            # 设置bad case
            if not isArea(grid, r, c):
                return 1
            # 海洋
            if grid[r][c] == 0:
                return 1
            # 已经遍历过的陆地
            if grid[r][c] != 1:
                return 0
            
            grid[r][c] = 2
            
            return dfs(grid, r-1, c) + dfs(grid, r+1, c) + dfs(grid, r, c-1) + dfs(grid, r, c+1)
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    return dfs(grid, i, j)
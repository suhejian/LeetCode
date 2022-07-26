class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        def isArea(grid, r, c):
            # r, c是否是有效位置
            if r >= 0 and r < len(grid) and c >= 0 and c < len(grid[0]):
                return True
            return False
        
        def dfs(grid, r, c):    # dfs求得岛屿面积
            # 设置bad case
            if not isArea(grid, r, c):
                return 0
            if grid[r][c] != 1:
                return 0
            
            grid[r][c] = 2  # 已经访问过的岛屿设置为2

            return 1 + dfs(grid, r, c-1) + dfs(grid, r, c+1) + dfs(grid, r-1, c) + dfs(grid, r+1, c)
        
        res = 0 # 表示最大的岛屿面积
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                res = max(res, dfs(grid, r, c))
        
        return res
            